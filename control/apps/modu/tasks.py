# coding=utf-8
import matlab.engine
import os

from control.control.base import control_response
from control.control.err_msg import ModuErrorCode
from celery import shared_task

"""
创建matlab引擎， 调用matlab函数
"""

@shared_task
def matlab_create_ves_distri(payload):
    """
    调用matlab产生船舶分布矩阵
    :param payload:包含需要产生船舶分布信息的参数
    :return: distri_id 船舶分布矩阵的id
    :uid_sid: 用户ID以及信号ID
    """

    action = payload.get("action", None)
    lon = payload.get("lon", None)
    lat = payload.get("lat", None)
    height = payload.get("height", None)
    vesNum = payload.get("vesNum", None)
    distri_mode = payload.get("distri_mode", None)
    distri_id = payload.get("distri_id", None)
    os.chdir('../../../AIS')
    eng = matlab.engine.start_matlab()
    try:
        eng.F_gendistri(lon, lat, height, vesNum, distri_mode, distri_id)
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=0, msg="distri running success", ret_set=[distri_id],
                                )
    except Exception as exp:
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=ModuErrorCode.DISTRI_RUNNING_FAILED,
                                msg=exp)

def matlab_create_ves_parTable(payload):
    """
    调用matlab产生parTable
    :param payload:包含需要产生船舶分布信息的参数
    :return: parTable_id 存储parTable的id
    :uid 用户ID
    """

    action = payload.get("action", None)
    height = payload.get("height", None)
    ant_pitch = payload.get("ant_pitch", None)
    ant_azimuth = payload.get("ant_azimuth", None)
    antenna_type = payload.get("antenna_type", None)
    channel_type = payload.get("channel_type")
    distri_id = payload.get("distri_id", None)
    partable_id = payload.get("parTable_id", None)
    os.chdir('../../../AIS')
    eng = matlab.engine.start_matlab()
    try:
        eng.F_calAreaPar(height, ant_pitch, ant_azimuth, antenna_type, channel_type, distri_id, partable_id)
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=0, msg="partable running success", ret_set=[partable_id],
                                )
    except Exception as exp:
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=ModuErrorCode.PARTABLE_RUNNING_FAILED,
                                msg=exp)


def matlab_create_time_table(payload):
    """
    调用matlab产生parTable
    :param payload:包含需要产生船舶分布信息的参数
    :return: parTable_id 存储parTable的id
    """
    action = payload.get("action", None)
    obtime = payload.get("obtime", None)
    protocol = payload.get("protocol", None)
    height = payload.get("height", None)
    distri_id = payload.get("distri_id", None)
    partable_id = payload.get("partable_id", None)
    timetable_id = payload.get("timetable_id", None)
    os.chdir('../../../AIS')
    eng = matlab.engine.start_matlab()
    try:
        eng.F_genTimeTable(obtime, protocol, height, distri_id, partable_id, timetable_id)
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=0, msg="timetable running success", ret_set=[timetable_id],
                                )
    except Exception as exp:
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=ModuErrorCode.TIMETABLE_RUNNING_FAILED,
                                msg=exp)

def matlab_create_ves_data(payload):
    """
    调用matlab产生AISData
    :param payload:包含需要产生船舶分布信息的参数
    :return: send_data_id 存储AISData的id
    :uid_sid: 用户ID以及信号ID
    """
    action = payload.get("action", None)
    distri_id = payload.get("distri_id", None)
    timetable_id = payload.get("timetable_id", None)
    aisdata_id = payload.get("aisdata_id", None)
    os.chdir('../../../AIS')
    eng = matlab.engine.start_matlab() # 启动matlab程序
    try:
        eng.F_genAISData(distri_id, timetable_id, aisdata_id)
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=0, msg="aisdata running success", ret_set=[aisdata_id],
                                )
    except Exception as exp:
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=ModuErrorCode.AISDATA_RUNNING_FAILED,
                                msg=exp)


def matlab_create_aisSig(payload):
    """
    调用matlab产生ais_Singal
    :param payload:包含需要产生船舶分布信息的参数
    :return: aisSig_id 存储AIS_Signal的id
    """
    action = payload.get("action", None)
    obtime = payload.get("obtime", None)
    vesnum = payload.get("vesnum", None)
    height = payload.get("height", None)
    snr = payload.get("snr", None)
    # zeroNum = payload.get("zeroNum", None)   # 此处也可以将zeroNum存放在send_data里边
    parTable_id = payload.get("parTable_id", None)
    timetable_id = payload.get("timetable_id", None)
    aisdata_id = payload.get("aisdata_id", None)
    signal_id = payload.get("signal_id", None)
    os.chdir('../../../AIS')
    eng = matlab.engine.start_matlab()
    try:
        eng.F_genAISSig(obtime, vesnum, height, parTable_id, timetable_id, aisdata_id, signal_id)
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=0, msg="signal running success", ret_set=[signal_id],
                                )
    except Exception as exp:
        eng.quit()
        os.chdir('../control/apps/modu')
        return control_response(code=ModuErrorCode.SIGNAL_RUNNING_FAILED,
                                msg=exp)
