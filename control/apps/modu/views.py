# # coding=utf-8
# from django.shortcuts import render
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# from .serializer import CreateSignalValidator
# # Create your views here.
#
# class CreateSignal(APIView):
#     """
#     创建信号
#     """
#     def post(self, request, *args, **kwargs):
#         req_data = request.data
#         validator = CreateSignalValidator(data=req_data, request=request)
#         if not validator.is_valid():
#             return Response()
#         error_map = validator.save()
#         if error_map:
#             return Response()
#         return Response()