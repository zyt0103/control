# coding=utf-8

from django.conf import settings

from control.control.base import control_response
from control.control.err_msg import DemodErrorCode

from .models import DemodModel, DemodType, DemodResult
from .tasks import Demod_single_ant
from .tasks import Demod_double_ant
from .tasks import Demod_four_ant

from control.control.logger import getLogger

logger = getLogger(__name__)


class Router():
    def __init__(self, payload):
        self.payload = payload

    def Ant_select(self):
        """
        选择解调的方式(天线数量)
        :return:
        """
        payload = self.payload
        demod_type_id = payload.get("demod_type_id")
        signal_id = payload.get("signal_id")
        logger.info("payload is %s" % payload)
        demod_model, error = DemodModel.objects.create(signal_id=signal_id,
                                                       demod_type_id=demod_type_id,
                                                       demod_prob_theory=None,
                                                       demod_prob_fact=None)
        if not demod_model:
            return control_response(code=DemodErrorCode.DEMOD_SAVE_FAILED, msg=error)

        demod_type = DemodType.get_demodtype_by_id(demodType_id=demod_type_id)
        ant_num = demod_type.ant_num
        protocol = demod_type.protocol
        sync_type = demod_type.sync_type

        # 根据天线数量选择解调方式
        if ant_num == 1:
            sub_payload = {
                "signal_id": signal_id,
                "protocol": protocol,
                "sync_type": sync_type
            }
            logger.info("The sub_payload is %s" % sub_payload)
            if settings.IF_RUN_MATLAB == 'True':
                Demod_single_ant.apply_async([sub_payload])

        if ant_num == 2:
            sub_payload = {
                "signal_id": signal_id,
                "protocol": protocol,
                "sync_type": sync_type
            }
            if settings.IF_RUN_MATLAB == 'True':
                Demod_double_ant.apply_async([sub_payload])

        if ant_num == 4:
            sub_payload = {
                "signal_id": signal_id,
                "protocol": protocol,
                "sync_type": sync_type
            }
            if settings.IF_RUN_MATLAB == 'True':
                Demod_four_ant.apply_async([sub_payload])
        return control_response(code=0, msg="Demod is running!")


def create_demod_type(payload):
    """
    创建解调方式
    :param payload:
    :return:
    """
    user_id = payload.get("user_id")
    demod_type_id = payload.get("demod_type_id")
    demod_type_name = payload.get("demod_type_name")
    ant_num = payload.get("ant_num")
    protocol = payload.get("protocol")
    sync_type = payload.get("sync_type")

    demod_type, error = DemodType.objects.create(user_id=user_id,
                                                demod_type_id=demod_type_id,
                                                demod_type_name=demod_type_name,
                                                ant_num=ant_num,
                                                protocol=protocol,
                                                sync_type=sync_type)

    if error:
        return control_response(code=DemodErrorCode.DEMOD_TYPE_SAVE_FAILED, msg=error)

    return control_response(code=0, msg="Demod Type create succ")

def delete_demod_type(payload):
    """
    删除解调方式
    :param payload:
    :return:
    """
    demod_type_id = payload.get("demod_type_id")
    if not isinstance(demod_type_id, list):
        demod_type_id = [demod_type_id]
    err_msg = ""
    for id in demod_type_id:
        if not DemodType.demodtype_exist_by_id(id):
            logger.info("Delete DemodType error, demod_type_id %s is not exist" % id)
            err_msg += id + ": " + "the demod_type is not exist"
            continue
        code, err = DemodType.delete_demodtype_by_id(id)
        if not code:
            err_msg += id + ": " + "the demod_type_id can not be deleted, exp: " + err
            continue
    return control_response(code=0 if not err_msg else DemodErrorCode.DEMOD_TYPE_DELETE_FAILED,
                            msg=err_msg if err_msg else "succ")

def list_demod_result(payload):
    signal_id = payload.get("signal_id", None)
    demod_type_id = payload.get("demod_type_id", None)
    demodresut, exp = DemodResult.describe_demod_result_by_id(signal_id=signal_id, demod_type_id=demod_type_id)
    if exp:
        return control_response(code=DemodErrorCode.DEMOD_TYPE_DESCRIBE_FAILED, msg=exp)

    return control_response(code=0, msg="Demod result describe succ")