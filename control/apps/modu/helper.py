# coding=utf-8
from copy import deepcopy
import os
from django.conf import settings

from .models import DistriModel, PartableModel, TimetableModel, AisdataModel, SignalModel
# from .models import *

from control.control.err_msg import ModuErrorCode
from control.control.base import control_response
from control.control.base import randomname_maker
from control.control.logger import getLogger

logger = getLogger(__name__)

from .tasks import *


def make_distri_id():
    while True:
        distri_id = "%s-%s" % (settings.DISTRI_PREFIX, randomname_maker())
        if not DistriModel.distri_exist_by_id(distri_id):
            return distri_id


def make_partable_id():
    while True:

        partable_id = "%s-%s" % (settings.PARTABLE_PREFIX, randomname_maker())
        logger.info("partable_id is %s" % partable_id)
        if not PartableModel.partable_exist_by_id(partable_id):
            return partable_id


def make_timetable_id():
    while True:
        timetable_id = "%s-%s" % (settings.TIMETABLE_PREFIX, randomname_maker())
        if not TimetableModel.timetable_exist_by_id(timetable_id):
            return timetable_id
def make_aisdata_id():
    while True:
        aisdata_id = "%s-%s" % (settings.AISDATA_PREFIX, randomname_maker())
        if not AisdataModel.aisdata_exist_by_id(aisdata_id):
            return aisdata_id


def make_signal_id():
    while True:
        signal_id = "%s-%s" % (settings.SIGNAL_PREFIX, randomname_maker())
        logger.info("signal_id is %s" % signal_id)
        if not SignalModel.signal_exist_by_id(signal_id):
            return signal_id


def create_ves_distri(payload):
    """
    产生船舶分布矩阵
    :param payload:包含需要产生船舶分布信息的参数
    :return:
    """
    lon = payload.get("lon", None)
    lat = payload.get("lat", None)
    height = payload.get("height", None)
    vesNum = payload.get("vesnum", None)
    distri_mode = payload.get("distri_mode", None)
    username = payload.get("owner")
    distri_id = make_distri_id()

    sub_payload = {
        "action": "create_ves_distri",
        "lon": lon,
        "lat": lat,
        "height": height,
        "vesNum": vesNum,
        "distri_mode": distri_mode,
        "distri_id": distri_id,
        "owner": username
    }
    distri_model, error = DistriModel.objects.create(user=username,
                                                       distri_id=distri_id,
                                                       distri_lon=lon,
                                                       distri_lat=lat,
                                                       distri_height=height,
                                                       distri_ves_num=vesNum,
                                                       distri_mode=distri_mode
                                                       )
    logger.info("distri_model is :%s" % distri_model)
    if not distri_model:
        logger.error("Save distri Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.DISTRI_SAVED_FAILED,
                                msg=error, ret_name_id="distri_id")


    run_failed = matlab_create_ves_distri(sub_payload)
    # logger.info(control_response(code=0, msg="distri running", ret_set=[distri_id]))
    if not run_failed:
        return control_response(code=0, msg="distri running", ret_set=[distri_id], ret_name_id="distri_id")
    return control_response(code=ModuErrorCode.DISTRI_RUNNING_FAILED, msg=run_failed, ret_set=[distri_id], ret_name_id="distri_id")

def create_ves_parTalb(payload):
    """
    产生船舶功率频偏时延DOA参数
    :param payload:包含需要产生船舶分布信息的参数
    :return: parTable_id 船舶参数矩阵的id
    """

    height = payload.get("height", None)
    vesnum = payload.get("vesnum", None)
    ant_pitch = payload.get("ant_pitch", None)
    ant_azimuth = payload.get("ant_azimuth", None)
    distri_mode = payload.get("distri_mode", None)
    antenna_type = payload.get("antenna_type", None)
    channel_type = payload.get("channel_type", None)
    distri_id = payload.get("distri_id", None)

    partable_id = make_partable_id()
    logger.info("partable_payload is %s" % payload)
    sub_payload = {
        "action": create_ves_parTalb,
        "height": height,
        "vesnum": vesnum,
        "ant_pitch": ant_pitch,
        "ant_azimuth": ant_azimuth,
        "antenna_type": antenna_type,
        "channel_type": channel_type,
        "distri_mode": distri_mode,
        "distri_id": distri_id,
        "partable_id": partable_id
    }

    logger.info("partable_payload is %s"%payload)
    parTable_model, error = PartableModel.objects.create(distri_id=distri_id,
                                                         partable_id=partable_id,
                                                         pitch=ant_pitch,
                                                         azimuth=ant_azimuth,
                                                         antenna_type=antenna_type,
                                                         channel_type=channel_type
                                                         )

    if not parTable_model:
        logger.error("Save parTable Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.PARTABLE_SAVED_FAILED,
                                msg=error, ret_name_id="partable_id")
    run_failed = matlab_create_ves_parTable(sub_payload)
    if not run_failed:
        return control_response(code=0, msg="parTable running", ret_set=[partable_id], ret_name_id="partable_id")
    return control_response(code=ModuErrorCode.PARTABLE_RUNNING_FAILED, msg=run_failed, ret_set=[partable_id], ret_name_id="partable_id")


def create_time_table(payload):
    """
    产生timetable
    :param: payload 包含必要的关于产生timetable的参数
    :return: timeTable_id 存储timeTable的id
    """

    obtime = payload.get("obtime", None)
    height = payload.get("height", None)
    protocol = payload.get("protocol", None)
    distri_id = payload.get("distri_id", None)
    partable_id = payload.get("partable_id", None)
    timetable_id = make_timetable_id()

    logger.info("partable_id is %s"%partable_id)
    sub_payload = {
        "action": "create_time_table",
        "obtime": obtime,
        "height": height,
        "protocol": protocol,
        "distri_id": distri_id,
        "partable_id": partable_id,
        "timetable_id": timetable_id
    }

    timetable_model, error = TimetableModel.objects.create(distri_id=distri_id,
                                                           partable_id=partable_id,
                                                           timetable_id=timetable_id,
                                                           obtime=obtime,
                                                           protocol=protocol
                                                          )

    if not timetable_model:
        logger.error("Save timetable Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.TIMETABLE_SAVED_FAILED,
                                msg=error, ret_name_id="timetable_id")
    run_failed = matlab_create_time_table(sub_payload)
    if not run_failed:
        return control_response(code=0, msg="timetable running", ret_set=[timetable_id], ret_name_id="timetable_id")
    return control_response(code=ModuErrorCode.TIMETABLE_RUNNING_FAILED, msg=run_failed, ret_set=[timetable_id], ret_name_id="timetable_id")

def create_ves_data(payload):
    """
    产生船舶发送数据
    :param: payload 包含必要的输入信息
    :return: send_data_id 发送信息表的id
    """
    distri_id = payload.get("distri_id", None)
    timetable_id = payload.get("timetable_id", None)
    aisdata_id = make_aisdata_id()

    sub_payload = {
        "action": "create_ves_data",
        "distri_id": distri_id,
        "timetable_id": timetable_id,
        "aisdata_id": aisdata_id
    }

    aisdata_model, error = AisdataModel.objects.create(distri_id=distri_id,
                                                       timetable_id=timetable_id,
                                                       aisdata_id=aisdata_id
                                                       )
    if not aisdata_model:
        logger.error("Save aisdata Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.AISDATA_SAVED_FAILED,
                                 msg=error, ret_name_id="aisdata_id")
    run_failed = matlab_create_ves_data(sub_payload)
    if run_failed:
        return control_response(code=0, msg="aisdate running", ret_set=[aisdata_id], ret_name_id="aisdata_id")
    return control_response(code=ModuErrorCode.AISDATA_RUNNING_FAILED, msg=run_failed, ret_set=[aisdata_id], ret_name_id="aisdata_id")

def create_aissig(payload):
    """
    产生AIS信号
    :param payload: 包含必要的关于产生timetable的参数
    :return: aisSig_Path 存储AISSig的路径
    """
    obtime = payload.get("obtime", None)
    vesnum = payload.get("vesnum", None)
    height = payload.get("height", None)
    partable_id = payload.get("partable_id", None)
    timetable_id = payload.get("timetable_id", None)
    aisdata_id = payload.get("aisdata_id", None)
    snr = payload.get("snr")
    logger.info("payload is %s"%payload)
    signal_id = make_signal_id()

    sub_payload = {
        "action": "create_aissig",
        "obtime": obtime,
        "vesnum": vesnum,
        "height": height,
        "partable_id": partable_id,
        "timetable_id": timetable_id,
        "aisdata_id": aisdata_id,
        "signal_id": signal_id,
        "snr": snr
#       "zeroNum": zeroNum
    }
    logger.info("signal_id is %s"%signal_id)
    signal_model, error = SignalModel.objects.create(partable_id=partable_id,
                                                        timetable_id=timetable_id,
                                                        aisdata_id = aisdata_id,
                                                        signal_id=signal_id,
                                                        snr=snr
                                                        )
    if not signal_model:
        logger.error("Save signal Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.SIGNAL_SAVED_FAILED,
                                 msg=error, ret_name_id="signal_id")
    run_failed = matlab_create_aisSig(sub_payload)
    if run_failed:
        return control_response(code=0, msg="signal running", ret_set=[signal_id], ret_name_id="signal_id")
    return control_response(code=ModuErrorCode.SIGNAL_RUNNING_FAILED, msg=run_failed, ret_set=[signal_id], ret_name_id="signal_id")
