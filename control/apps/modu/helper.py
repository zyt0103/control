# coding=utf-8
from copy import deepcopy
import os
from django.conf import settings

# from .models import DistriModel, PartableModel, TimetableModel, SignalModel
from .models import *
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
        if not DistriModel.partable_exist_by_id(partable_id):
            return partable_id
def make_timetable_id():
    while True:
        timetable_id = "%s-%s" % (settings.TIMETABLE_PREFIX, randomname_maker())
        if not DistriModel.timetable_exist_by_id(timetable_id):
            return timetable_id
def make_aisdata_id():
    while True:
        aisdata_id = "%s-%s" % (settings.AISDATA_PREFIX, randomname_maker())
        if not DistriModel.aisdata_exist_by_id(aisdata_id):
            return aisdata_id
def make_signal_id():
    while True:
        signal_id = "%s-%s" % (settings.SIGNAL_PREFIX, randomname_maker())
        if not DistriModel.signal_exist_by_id(signal_id):
            return signal_id

def create_ves_distri(payload):
    """
    产生船舶分布矩阵
    :param payload:包含需要产生船舶分布信息的参数
    :return: distri_id 存储船舶分布矩阵的路径
    """
    lon = payload.get("distri_lon", None)
    lat = payload.get("distri_lat", None)
    height = payload.get("distri_height", None)
    vesNum = payload.get("distri_ves_num", None)
    mode = payload.get("distri_mode", None)
    username = payload.get("owner")
    distri_id = make_distri_id()

    sub_payload = {
        "action": "create_ves_distri",
        "Lon": lon,
        "Lat": lat,
        "Height": height,
        "VesNum": vesNum,
        "Mode": mode,
        "distri_id": distri_id,
        "owner": username
    }

    distri_model, error = DistriModel.objects.create(user=username,
                                                       distri_id=distri_id,
                                                       distri_lon=lon,
                                                       distri_lat=lat,
                                                       distri_height=height,
                                                       distri_ves_num=vesNum,
                                                       distri_mode=mode
                                                       )
    if not distri_model:
        logger.error("Save distri Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.DISTRI_SAVED_FAILED,
                                msg=error)

    matlab_create_ves_distri(sub_payload)
    return control_response(code=0, msg="distri running", ret_set=[distri_id])

def create_ves_parTalb(payload):
    """
    产生船舶功率频偏时延DOA参数
    :param payload:包含需要产生船舶分布信息的参数
    :return: parTable_id 船舶参数矩阵的id
    """
    pitch = payload.get("pitch", None)
    azimuth = payload.get("azimuth", None)
    height = payload.get("Height", None)
    antenna_type = payload.get("antenna_type", None)
    channel_type = payload.get("channel_type", None)
    distri_id = payload.get("distri_id", None)
    partable_id = make_partable_id()

    sub_payload = {
        "action": create_ves_parTalb,
        "height": height,
        "pitch": pitch,
        "azimuth": azimuth,
        "antenna_type": antenna_type,
        "channel_type": channel_type,
        "distri_id": distri_id,
        "partable_id": partable_id
    }


    parTable_model, error = PartableModel.objects.create(distri_id=distri_id,
                                                         partable_id=partable_id,
                                                         pitch=pitch,
                                                         azimuth=azimuth,
                                                         antenna_type=antenna_type,
                                                         channel_type=channel_type
                                                         )

    if not parTable_model:
        logger.error("Save parTable Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.PARTABLE_SAVED_FAILED,
                                msg=error)
    matlab_create_ves_parTable(sub_payload)
    return control_response(code=0, msg="parTable running", ret_set=[partable_id])


def create_time_table(payload):
    """
    产生timetable
    :param: payload 包含必要的关于产生timetable的参数
    :return: timeTable_id 存储timeTable的id
    """

    obtime = payload.get("obtime", None)
    protocol = payload.get("protocol", None)
    distri_id = payload.get("distri_id", None)
    partable_id = payload.get("partable_id", None)
    timetable_id = make_timetable_id()

    sub_payload = {
        "action": "create_time_table",
        "obtime": obtime,
        "protocol": protocol,
        "distri_id": distri_id,
        "partalbe_id": partable_id,
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
                                msg=error)
    matlab_create_ves_parTable(sub_payload)
    return control_response(code=0, msg="timetable running", ret_set=[timetable_id])

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
                                 msg=error)
    matlab_create_ves_data(sub_payload)
    return control_response(code=0, msg="aisdate running", ret_set=[aisdata_id])


def create_aissig(payload):
    """
    产生AIS信号
    :param payload: 包含必要的关于产生timetable的参数
    :return: aisSig_Path 存储AISSig的路径
    """
    partable_id = payload.get("partable_id", None)
    timetable_id = payload.get("timetable_id", None)
    aisdata_id = payload.get("aisdata_id", None)
    snr = payload.get("snr")
    signal_id = make_signal_id()
#    zeroNum = payload.get("zeroNum", None)

    sub_payload = {
        "action": "create_aissig",
        "partable_id": partable_id,
        "timetable_id": timetable_id,
        "aisdata_id": aisdata_id,
        "signal_id": signal_id,
        "snr": snr
#       "zeroNum": zeroNum
    }
    signal_model, error = SignalModel.objects.create(partable_id=partable_id,
                                                        timetable_id=timetable_id,
                                                        aisdata_id = aisdata_id,
                                                        signal_id=signal_id,
                                                        snr=snr
                                                        )
    if not signal_model:
        logger.error("Save signal Failed: %s" % str(error))
        return control_response(code=ModuErrorCode.SIGNAL_SAVED_FAILED,
                                 msg=error)
    matlab_create_aisSig(sub_payload)
    return control_response(code=0, msg="signal running", ret_set=[signal_id])
