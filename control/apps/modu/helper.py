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
