# coding=utf-8
from django.shortcuts import render

from control.control.base import control_code
from control.control.base import control_response
from control.control.base import username_temp
# from control.control.default_msg import set_default_payload
from control.control.default_msg import Defaultvalue

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import CreateSignalSerializer
# from .sub_view import Createsignals
# from .helper import create_ves_distri
from control.control.logger import getLogger
from .sub_view import Router

logger = getLogger(__name__)

# Create your views here.


class CreateSignal(APIView):
    """
    创建信号
    """
    # action = "CreateSignal"

    def post(self, request, *args, **kwargs):
        req_data = request.data
        logger.info(req_data)
        validator = CreateSignalSerializer(data=req_data)
        logger.error("validator is valid: %s" % validator.is_valid())
        if not validator.is_valid():
            code, msg = control_code(validator)
            logger.error(str(validator.errors))
            return Response(control_response(code=code, msg=msg),
                            status=status.HTTP_200_OK)

        action_all = validator.validated_data.get("action_all", None)
        action = validator.validated_data.get("action", None)
        lon = validator.validated_data.get("lon", None)
        lat = validator.validated_data.get("lat", None)
        height = validator.validated_data.get("height", None)
        vesnum = validator.validated_data.get("vesnum", None)
        obtime = validator.validated_data.get("obtime", None)
        ant_pitch = validator.validated_data.get("ant_pitch", None)
        ant_azimuth = validator.validated_data.get("ant_azimuth", None)
        ant_type = validator.validated_data.get("ant_type", None)
        channel_tpye = validator.validated_data.get("channel_type", None)
        protocol = validator.validated_data.get("protocol", None)
        snr = validator.validated_data.get("snr", None)
        distri_mode = validator.validated_data.get("distri_mode", None)
        distri_id = validator.validated_data.get("distri_id", None)
        partable_id = validator.validated_data.get("partable_id", None)
        timetable_id = validator.validated_data.get("timetable_id", None)
        aisdata_id = validator.validated_data.get("aisdata_id", None)
        signal_id = validator.validated_data.get("signal_id", None)
        owner = username_temp()

        payload = {
            # "action": self.action,
            "action_all": action_all,
            "action": action,
            "owner": owner,
            "lon": lon,
            "lat": lat,
            "height": height,
            "vesnum": vesnum,
            "obtime": obtime,
            "ant_pitch": ant_pitch,
            "ant_azimuth": ant_azimuth,
            "ant_type": ant_type,
            "channel_type": channel_tpye,
            "protocol": protocol,
            "snr": snr,
            "distri_mode": distri_mode,
            "distri_id": distri_id,
            "partable_id": partable_id,
            "timetable_id": timetable_id,
            "aisdata_id": aisdata_id,
            "signal_id": signal_id
        }
        payload_default = Defaultvalue(payload)
        payload = payload_default.set_default_payload()
        # payload = set_default_payload(payload)

        logger.info(payload)
        # resp = Router.Actionrouter(payload)
        route = Router(payload)
        resp = route.Actionrouter()

        # resp = Createsignals().Creatdistri(payload)
        return Response(resp, status=status.HTTP_200_OK)
        # distri_id = validator.validated_data.get("distri_id", None)
        # distri_lon = validator.validated_data.get("distri_lon", None)
        # distri_lat = validator.validated_data.get("distri_lat", None)
        # distri_height = validator.validated_data.get("distri_height", None)
        # distri_ves_num = validator.validated_data.get("distri_ves_num", None)
        # distri_mode = validator.validated_data.get("distri_mode", None)
        # owner = username_temp()
        #
        # payload = {
        #     "action": self.action,
        #     "owner": owner,
        #     "distri_id": distri_id,
        #     "lon": distri_lon,
        #     "lat": distri_lat,
        #     "height": distri_height,
        #     "vesnum": distri_ves_num,
        #     "distri_mode": distri_mode
        # }
        #resp = create_ves_distri(payload=payload)




# class CreateSignal(APIView):
#     """
#     创建信号
#     """
#     action = "CreateSignal"
#
#     def post(self, request, *args, **kwargs):
#         req_data = request.data
#         logger.info(req_data)
#         validator = CreateDistriSerializer(data=req_data)
#         logger.error("validator is vialid : %s" % validator.is_valid())
#         if not validator.is_valid():
#             code, msg = control_code(validator)
#             # logger.info("validator is invalide")
#             return Response(control_response(code=code, msg=msg),
#             # return Response(control_response(code=code, msg='validator error'),
#                             status=status.HTTP_200_OK)
#         distri_id = validator.validated_data.get("distri_id", None)
#         distri_lon = validator.validated_data.get("distri_lon", None)
#         distri_lat = validator.validated_data.get("distri_lat", None)
#         distri_height = validator.validated_data.get("distri_height", None)
#         distri_ves_num = validator.validated_data.get("distri_ves_num", None)
#         distri_mode = validator.validated_data.get("distri_mode", None)
#         owner = username_temp()
#
#
#
#     def creatdistri(payload):
#         lat = payload.get()
#         subpayload = {}
#         create_ves_distri(subpayload)
#
#
