# coding=utf-8

from control.control.base import control_code
from control.control.base import control_response

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import DemodSignalSerializer
from .serializer import DemodTypeSerializer
from .serializer import DemodResultSerializer
from .helper import Router
from .helper import create_demod_type, list_demod_result

from control.control.logger import getLogger
from control.control.base import get_path, user_temp

from control.apps.modu.helper import make_id

logger = getLogger(__name__)


class DemodSignal(APIView):
    """
    Demode signals
    """
    def post(self, request, *args, **kwargs):
        """
        接受post请求数据并处理
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        req_data = request.data
        logger.info(req_data)
        validator = DemodSignalSerializer(data=req_data)
        logger.info("validator is valid: %s" % validator.is_valid())
        if not validator.is_valid():
            code, msg = control_code(validator)
            logger.debug(str(validator.errors))
            return Response(control_response(code=code, msg=msg),
                            status=status.HTTP_200_OK)

        signal_id = validator.validated_data.get("signal_id", None)
        demod_type_id = validator.validated_data.get("demod_type_id", None)

        payload = {
            "signal_id": signal_id,
            "demod_type_id": demod_type_id
        }
        logger.info("The main payload is %s" % payload)
        router = Router(payload)
        resp = router.Ant_select()

        return Response(resp, status=status.HTTP_200_OK)

class DemodTypeCreate(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        logger.info("Cur request data is %s" % data)
        validator = DemodTypeSerializer(data=data)
        logger.info("validator is valid: %s" % validator.is_valid())
        if not validator.is_valid():
            code, msg = control_code(validator)
            logger.debug(str(validator.errors))
            return Response(control_response(code=code, msg=msg),
                            status=status.HTTP_200_OK)
        user_id = user_temp()
        demod_type_id = make_id("demod_type")
        ant_num = validator.validated_data.get("ant_num", None)
        protocol = validator.validated_data.get("protocol", None)
        sync_type = validator.validated_data.get("sync_type", None)
        demod_type_name = validator.validated_data.get("demod_type_name", None)

        pay_load = {
            "user_id": user_id,
            "demod_type_id": demod_type_id,
            "demod_type_name": demod_type_name,
            "ant_num": ant_num,
            "protocol": protocol,
            "sync_type": sync_type
        }
        logger.info("payload is %s" % pay_load)
        resp = create_demod_type(pay_load)
        return Response(resp, status=status.HTTP_200_OK)


class DemodResultList(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        logger.info("Cur request data is %s" % data)
        validator = DemodResultSerializer(data=data)
        if not validator.is_valid():
            code, msg = control_code(validator)
            return Response(control_response(code=code, msg=msg),
                            status=status.HTTP_200_OK)
        signal_id = validator.validated_data.get("signal_id", None)
        demod_type_id = validator.validated_data.get("demod_type_id", None)

        pay_load = {
            "signal_id": signal_id,
            "demod_type_id": demod_type_id
        }
        logger.info("payload is %s" % pay_load)
        resp = list_demod_result(pay_load)
        return Response(resp, status=status.HTTP_200_OK)