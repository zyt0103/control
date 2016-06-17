# coding=utf-8

from .validator import *

from control.control.logger import getLogger
logger = getLogger(__name__)


class DemodSignalSerializer(serializers.Serializer):
    """
    解调序列化函数
    """
    signal_id = serializers.CharField(
        max_length=20,
        required=True,
        validators=[signal_id_validator]
    )

    demod_type_id = serializers.CharField(
        max_length=20,
        required=False,
        validators=[demod_type_id_validator]
    )



class DemodTypeSerializer(serializers.Serializer):
    """
    解调方式序列化函数
    """
    demod_type_name = serializers.CharField(
        max_length=20
    )

    ant_num = serializers.IntegerField(
        validators=[ant_num_validator]
    )

    protocol = serializers.CharField(
        max_length=20,
        required=False,
        validators=[protocol_validator]
    )

    sync_type = serializers.CharField(
        max_length=20,
        required=False,
        validators=[sync_type_validator]
    )