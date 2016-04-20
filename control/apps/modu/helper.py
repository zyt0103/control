# coding=utf-8
from copy import deepcopy
import os
from django.conf import settings

from .models import DistriModel
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
    return control_response(code=0, msg="distri running",ret_set=[distri_id])
#
# def create_ves_parTalb(payload):
#      """
#     产生船舶功率频偏时延DOA参数
#     :param payload:包含需要产生船舶分布信息的参数
#     :return: parTable_id 船舶参数矩阵的id
#     """
#     height = payload.get("Height", None)
#     uid = payload.get("uid", None)
#     distri_id = payload.get("distri_id", None)
#
#     if not height or not distri_id or not uid:
#         return Response()
#     sub_payload = {
#     "action": create_ves_parTalb,
#     "height": height,
#     "uid": uid,
#     "distri_id": distri_id
#      }
#
#      parTable_id, error = matlab_create_ves_parTable(sub_payload)
#      if error:
#         return Response()
#
#     return Response()
#
#
# def create_ves_data(payload):
#     """
#     产生船舶发送数据
#     :param: payload 包含必要的输入信息
#     :return: send_data_id 发送信息表的id
#     """
#     distri_id = payload.get("distri_id", None)
#     real_ves_num = payload.get("real_ves_num", None)   # 可以不用
#     uid = payload.get("uid", None)
#     if not distri_id or not real_ves_num or not uid:
#
#     sub_payload = {
#         "action": "create_ves_data",
#         "distri_id": distri_id,
#         "real_ves_num": real_ves_num,   #这个参数可以采用其他的方式进行改变
#         "uid": uid
#     }
#
#     send_data_id, error = matlab_create_ves_data(sub_payload)
#
#     if error:
#         return Response()
#
#     return Response()
#
#
# def create_time_table(payload):
#     """
#     产生timetable
#     :param: payload 包含必要的关于产生timetable的参数
#     :return: timeTable_id 存储timeTable的id
#     """
#     distri_id = payload.get("distri_id", None)
#     obtime = payload.get("obtime", None)
#     ant_mode = payload.get("ant_mode")
#     uid = payload.get("uid", None)
#     if not distri_id or not obtime or not uid:
#         return Response()
#
#     sub_payload = {
#         "action": "create_time_table",
#         "distri_id": distri_id,
#         "obtime": obtime,
#         "ant_mode"j: ant_mode,
#         "uid": uid
#     }
#
#     timeTable_id, error = matlab_create_time_table(sub_payload)
#
#     if error:
#         return Response();
#
#     return Response();
# def create_aissig(payload):
#     """
#     产生AIS信号
#     :param payload: 包含必要的关于产生timetable的参数
#     :return: aisSig_Path 存储AISSig的路径
#     """
#     distri_id = payload.get("distri_id", None)
#     parTable_id = payload.get("parTable_id", None)
#     send_data_id = payload.get("send_data_id", None)
#     obtime = payload.get("obtime", None)
#     zeroNum = payload.get("zeroNum", None)
#     uid = payload.get("uid")
#
#     if not distri_id or not parTable_id or not send_data_id or not obtime or not zeroNum or not uid:
#         return Response()
#     sub_payload = {
#     "action": "create_aissig",
#     "distri_id": distri_id,
#     "parTable_id": parTable_id,
#     "send_data_id": send_data_id,
#     "obtime": obtime,
#     "zeroNum": zeroNum,
#     "uid": uid
#     }
#
#     aisSig_id, error = matlab_create_aisSig(sub_payload)

# # coding=utf-8
# from copy import deepcopy
#
#
# def create_ves_distri(payload):
#     """
#     产生船舶分布矩阵
#     :param payload:包含需要产生船舶分布信息的参数
#     :return: distri_id 船舶分布矩阵的id
#     """
#     lon = payload.get("Lon", None)
#     lat = payload.get("Lat", None)
#     height = payload.get("Height", None)
#     vesNum = payload.get("VesNum", None)
#     mode = payload.get("Mode", None)
#
#     #此处使用not 进行判断(更高级的话使用serializer和validator)
#     if not lon or not lat or not height or not vesNum or not mode:
#         return Response()
#
#     sub_payload = {
#         "action": "create_ves_distri",
#         "Lon": lon,
#         "Lat": lat,
#         "Height": height,
#         "VesNum": vesNum,
#         "Mode": mode
#     }
#
#     distri_id, error = matlab_create_ves_distri(sub_payload)
#     if error:
#         return Response()
#
#     return Response()
#
#
# def create_ves_data(payload):
#     """
#     产生船舶发送数据
#     :param payload:包含必要的输入信息
#     :return: 发送信息表的id
#     """
#     distri_id = payload.get("distri_id", None)
#     real_ves_num = payload.get("real_ves_num", None)
#
#     if not distri_id or not real_ves_num:
#         return Response()
#
#     sub_payload = {
#         "action": "create_ves_data",
#         "distri_id": distri_id,
#         "real_ves_num": real_ves_num   #这个参数可以采用其他的方式进行改变
#     }
#
#     send_data_id, error = matlab_create_ves_data(sub_payload)
#
#     if error:
#         return Response()
#
#     return Response()
#
#
# def create_time_table(payload):
#     """
#     产生timetable
#     :param payload: 包含必要的关于产生timetable的参数
#     :return: timetable的id
#     """
#     distri_id = payload.get("distri_id", None)
#     obtime = payload.get("obtime", None)
#
#     if not distri_id or not obtime:
#         return Response()
#
#     sub_payload = {
#         "action": "create_time_table",
#         "distri_id": distri_id,
#         "obtime": obtime
#     }
#
#     time_tabel_id, error = matlab_create_time_table(sub_payload)
#
#     if error:
#         return Response();
#
#     return Response();
