# coding=utf-8

import os
import matlab.engine

from datetime import time
from os.path import getsize
from os.path import join

from celery import shared_task

from control.control import settings
from control.control.base import get_path
from control.control.base import control_response

from .models import PartableModel
from .models import SignalModel
from .models import ScheduleModel

from control.control.logger import getLogger
logger = getLogger(__name__)

"""
创建matlab引擎， 调用matlab函数
"""


matlab_path = get_path.MATLAB_FILE_PATH
celery_path = get_path.CELERY_PATH


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
    os.chdir(matlab_path)
    logger.info(os.getcwd())
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab_distri")
        eng.F_genDistri(lon, lat, height, vesNum, distri_mode, distri_id)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("distri running error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False


@shared_task
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
    partable_id = payload.get("partable_id", None)
    os.chdir(matlab_path)
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab_partable")
        eng.F_genParTable(height, ant_pitch, ant_azimuth, antenna_type, channel_type, distri_id, partable_id)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("partable running error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False


@shared_task
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
    transInterval = payload.get("transInterval", None)
    distri_id = payload.get("distri_id", None)
    partable_id = payload.get("partable_id", None)
    timetable_id = payload.get("timetable_id", None)
    os.chdir(matlab_path)
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab_timetable")
        eng.F_genTimeTable(obtime, protocol, height, transInterval, distri_id, partable_id, timetable_id)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("timetable running error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False


@shared_task
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
    os.chdir(matlab_path)
    eng = matlab.engine.start_matlab() # 启动matlab程序
    try:
        logger.info("start matlab_aisdata")
        eng.F_genAISData(distri_id, timetable_id, aisdata_id)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("aisdata running error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False


@shared_task
def matlab_create_aisSig(payload):
    """
    调用matlab产生Singal
    :param payload:包含需要产生船舶分布信息的参数
    :return: aisSig_id 存储AIS_Signal的id
    """
    action = payload.get("action", None)
    obtime = payload.get("obtime", None)
    vesnum = payload.get("vesnum", None)
    height = payload.get("height", None)
    snr = payload.get("snr", None)
    channel_num = payload.get("channel_num", None)
    distri_id = payload.get("distri_id", None)
    partable_id = payload.get("partable_id", None)
    timetable_id = payload.get("timetable_id", None)
    aisdata_id = payload.get("aisdata_id", None)
    signal_id = payload.get("signal_id", None)
    os.chdir(matlab_path)
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab_signal")
        eng.F_genAISSig(obtime, vesnum, height, snr, channel_num, distri_id, partable_id, timetable_id, aisdata_id, signal_id)
        getPicHtml(signal_id=signal_id, eng=eng)
        eng.quit()
        os.chdir(celery_path)

        return True
    except Exception as exp:
        logger.error("signal running error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False


def getPicHtml(signal_id, eng):
    """
    获取html文件
    :return:
    """
    actionList = ["power", "doppler", "delay", "DOA"]
    for action in actionList:
        path_plot = get_plot_data_file(action, signal_id)
        # os.chdir(matlab_path)
        try:
            logger.info("start matlab_plot")
            logger.info(action + path_plot + signal_id)
            eng.matlab_to_html(action, path_plot, signal_id)
            # os.chdir(celery_path)
        except Exception as exp:
            logger.error("get plot data error: %s" % str(exp))
            return False
    return True


def get_plot_data_file(action, signal_id):
    """
    获取画图所需数据的文件名
    :param action:
    :param siganl_id:
    :return:
    """
    if action == "distri":
        try:
            partable_id = SignalModel.get_partable_id_by_signal_id(signal_id=signal_id)
            distri_id = PartableModel.get_distri_id_by_partable_id(partable_id=partable_id)
            ret_path = os.path.join(matlab_path, "DATA", "distribution", "%s.mat" % distri_id)
            return ret_path
        except Exception as exp:
            logger.error("get plot data distri error: %s" % str(exp))
            return None
    if action == "power" or action == "doppler" or action == "delay" or action == "DOA":
        try:
            partable_id = SignalModel.get_partable_id_by_signal_id(signal_id=signal_id)
            ret_path = os.path.join(matlab_path, "DATA", "parTable", "%s.mat" % partable_id)
            logger.info("ret_path is %s" % ret_path)
            return ret_path
        except Exception as exp:
            logger.error("get plot data partable error: %s" % str(exp))
            return None