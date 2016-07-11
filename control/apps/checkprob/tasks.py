# coding=utf-8

import os
import matlab.engine

from celery import shared_task

from control.control.base import get_path
from control.control.logger import getLogger

logger = getLogger(__name__)

matlab_checkprob_path = get_path.MATALB_CHECKPROB_PATH
matlab_theoryCheckProb_path = get_path.MATLAB_METHOD_CHECKPROB_PATH
celery_path = get_path.CELERY_PATH


@shared_task()
def CheckProb(payload):
    """
    解调概率
    :param payload: 解调所需参数
    :return:
    """
    demodSignal_id = payload.get("demodSignal_id", None)
    action = payload.get("action", None)
    os.chdir(matlab_checkprob_path)
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab checkprob")
        eng.checkprob(demodSignal_id)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("checkprob error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False

@shared_task()
def TheoryCheckProb(payload):
    """
    理论解调概率
    :param payload: 解调所需参数
    :return:
    """
    signal_id = payload.get("signal_id", None)
    action = payload.get("action", None)
    os.chdir(matlab_theoryCheckProb_path)
    eng = matlab.engine.start_matlab()
    try:
        logger.info("start matlab theory checkprob")
        eng.checkprob(signal_id, action)
        eng.quit()
        os.chdir(celery_path)
        return True
    except Exception as exp:
        logger.error("theory checkprob error: %s" % str(exp))
        eng.quit()
        os.chdir(celery_path)
        return False

