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
# Create your views here.


class CreateSignal(APIView):
    """
    创建信号
    """
    action = "CreateSignal"

    def post(self, request, *args, **kwargs):
        req_data = request.data
        validator = CreateDistriSerializer(data=req_data)
        if not validator.is_valid():
            code, msg = control_code(validator)
            return Response(control_response(code=code, msg=msg),
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
            "distri_lon": distri_lon,
            "distri_lat": distri_lat,
            "distri_height": distri_height,
            "distri_ves_num": distri_ves_num,
            "distri_mode": distri_mode
        }
        resp = create_ves_distri(payload=payload)

        return Response(resp, status=status.HTTP_200_OK)
