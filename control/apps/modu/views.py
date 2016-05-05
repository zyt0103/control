# coding=utf-8
from django.shortcuts import render

from control.control.base import control_code
from control.control.base import control_response
from control.control.base import username_temp

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import CreateDistriSerializer
from .helper import create_ves_distri
from control.control.logger import getLogger

logger = getLogger(__name__)

# Create your views here.


class CreateSignal(APIView):
    """
    创建信号
    """
    action = "CreateSignal"

    def post(self, request, *args, **kwargs):
        req_data = request.data
        logger.info(req_data)
        validator = CreateDistriSerializer(data=req_data)
        logger.error("validator is valid: %s" % validator.is_valid())
        if not validator.is_valid():
            code, msg = control_code(validator)
            # logger.info("validator is invalide")
            return Response(control_response(code=code, msg=msg),
            # return Response(control_response(code=code, msg='validator error'),
                            status=status.HTTP_200_OK)
        distri_id = validator.validated_data.get("distri_id", None)
        distri_lon = validator.validated_data.get("distri_lon")
        distri_lat = validator.validated_data.get("distri_lat")
        distri_height = validator.validated_data.get("distri_height")
        distri_ves_num = validator.validated_data.get("distri_ves_num")
        distri_mode = validator.validated_data.get("distri_mode")
        owner = username_temp()

        payload = {
            "action": self.action,
            "owner": owner,
            "distri_id": distri_id,
            "lon": distri_lon,
            "lat": distri_lat,
            "height": distri_height,
            "vesnum": distri_ves_num,
            "distri_mode": distri_mode
        }
        resp = create_ves_distri(payload=payload)

        return Response(resp, status=status.HTTP_200_OK)
