# coding=utf-8
import matlab.engine
import os

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
    lon = payload.get("Lon", None)
    lat = payload.get("Lat", None)
    height = payload.get("Height", None)
    vesNum = payload.get("VesNum", None)
    mode = payload.get("Mode", None)
    user_id = payload.get("owner", None)
    distri_id = payload.get("distri_id")
    os.chdir('../AIS')
    eng = matlab.engine.start_matlab() 
    error = eng.F_genParameter(lon, lat, height, vesNum, mode, distri_id)
    eng.quit()

# def matlab_create_ves_data(pyload):
#     """
#     调用matlab产生AISData
#     :param payload:包含需要产生船舶分布信息的参数
#     :return: send_data_id 存储AISData的id
#     :uid_sid: 用户ID以及信号ID
#     """
#
#     real_ves_num = payload.get("real_ves_num", None)
#     send_data_id = getId.get("send_data_id")
#     os.chdir('../AIS')
#     eng = matlab.engine.start_matlab() # 启动matlab程序
#     error = eng.F_genAISData(real_ves_num)
#     return (send_data_id, error)
#
# def matlab_create_ves_parTable(sub_payload):
#     """
#     调用matlab产生parTable
#     :param payload:包含需要产生船舶分布信息的参数
#     :return: parTable_id 存储parTable的id
#     :uid 用户ID
#     """
#     height = payload.get("Height", None)
#     uid = payload.get("uid", None)
#     distri_id = payload.get("distri_id", None)
#     parTable_id = getId.get("parTable_id", None)
#     os.chdir('../AIS')
#     eng = matlab.engine.start_matlab()
#     error = eng.F_calAreaPar(height, uid, distri_id)
#     return (parTable_id, error)
#
# def matlab_create_time_table(payload):
#     """
#     调用matlab产生parTable
#     :param payload:包含需要产生船舶分布信息的参数
#     :return: parTable_id 存储parTable的id
#     """
#     obtime = payload.get("obtime", None)
#     ant_mode = payload.get("ant_mode", None)
#     distri_id = payload.get("distri_id", None)
#     parTable_id = payload.get("parTable_id", None)
#     uid = payload.get("uid", None)
#     timeTalbe_id = getId.get("timeTable_id", None)
#     os.chdir('../AIS')
#     eng = matlab.engine.start_matlab()
#     error = eng.F_genTimeTable(obtime, ant_mode, distri_id, parTable_id, uid)
#     return (timeTable_id, error)
#
# def matlab_create_aisSig(payload):
#     """
#     调用matlab产生ais_Singal
#     :param payload:包含需要产生船舶分布信息的参数
#     :return: aisSig_id 存储AIS_Signal的id
#     """
#     obtime = payload.get("obtime", None)
#     zeroNum = payload.get("zeroNum", None)   # 此处也可以将zeroNum存放在send_data里边
#     distri_id = payload.get("distri_id", None)
#     parTable_id = payload.get("parTable_id", None)
#     send_data_id = payload.get("send_data_id", None)
#     uid = payload.get("uid", None)
#     aisSig_id = send_data_id
#     os.chdir('../AIS')
#     eng = matlab.engine.start_matlab()
#     error = eng.F_genAISSig(obtime, zeroNum, distri_id, parTable_id, send_data_id, uid, aisSig_id)