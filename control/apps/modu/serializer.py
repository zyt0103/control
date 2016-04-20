# coding=utf-8
from rest_framework import serializers
from .validator import distri_id_validator
from .validator import distri_mode_validator

# class CreateSignalSerializer(serializers.Serializer):
#     """
#     创建信号
#     """
#

class CreateDistriSerializer(serializers.Serializer):
    """
    产生船舶分布矩阵
    """
    distri_id = serializers.CharField(
        required=False,
        max_length=20,
        validators=[distri_id_validator]
    )

    distri_lon = serializers.FloatField(
        required=True,
        validators=[]
    )

    distri_lat = serializers.FloatField(
        required=True,
        validators=[]
    )

    distri_height = serializers.IntegerField(
        required=True,
        validators=[]
    )

    distri_mode = serializers.CharField(
        required=True,
        validators=[distri_mode_validator]
    )

