# coding=utf-8

import os
import matlab.engine

from celery import shared_task
from control.control.settings import DATABASES

from control.control.base import get_path
from control.control.logger import getLogger

logger = getLogger(__name__)


matlab_single_ant_path = get_path.MATLAB_DEMOD_SINGLE_ANT_PATH
matlab_double_ant_path = get_path.MATLAB_DEMOD_DOUBLE_ANT_PATH
matlab_four_ant_path = get_path.MATLAB_DEMOD_FOUR_ANT_PATH
celery_path = get_path.CELERY_PATH


@shared_task()
def Demod_single_ant(payload):
    """
    单天线解调
    :param payload: 解调所需参数
    :return:
    """
    signal_id = payload.get("signal_id", None)
    demod_type_id = payload.get("demod_type_id", None)
    protocol = payload.get("protocol", None)
    sync_type = payload.get("sync_type", None)
    db_usr = DATABASES.get("default").get("USER")
    db_pwd = DATABASES.get("default").get("PASSWORD")
    os.chdir(matlab_single_ant_path)
    logger.info("the current path is %s" % os.getcwd())
    eng = matlab.engine.start_matlab()
    try:
        logger.info("payload is %s, %s, %s" % (signal_id, protocol, sync_type))
        logger.info("start matlab single_ant demode")
        eng.Main(signal_id, demod_type_id, protocol, sync_type, db_usr, db_pwd)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("single_ant demode error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False


@shared_task()
def Demod_double_ant(payload):
    """
    双天线解调
    :param payload:
    :return:
    """
    signal_id = payload.get("signal_id", None)
    demod_type_id = payload.get("demod_type_id", None)
    protocol = payload.get("protocol", None)
    sync_type = payload.get("sync_type", None)
    db_usr = DATABASES.get("DEFAULT").get("USER")
    db_pwd = DATABASES.get("DEFAULT").get("PASSWORD")
    os.chdir(matlab_double_ant_path)
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab double_ant demode")
        eng.Main(signal_id, demod_type_id, protocol, sync_type, db_usr, db_pwd)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("double_ant demode error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False


@shared_task()
def Demod_four_ant(payload):
    """
    双天线解调
    :param payload:
    :return:
    """
    signal_id = payload.get("signal_id", None)
    demod_type_id = payload.get("demod_type_id", None)
    protocol = payload.get("protocol", None)
    sync_type = payload.get("sync_type", None)
    db_usr = DATABASES.get("DEFAULT").get("USER")
    db_pwd = DATABASES.get("DEFAULT").get("PASSWORD")

    os.chdir(matlab_four_ant_path)
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab four_ant demode")
        eng.Main(signal_id, demod_type_id, protocol, sync_type, db_usr, db_pwd)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("four_ant demode error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False
