# coding=utf-8

from django.utils.translation import ugettext as _
from rest_framework import serializers

from control.apps.modu.models import SignalModel



ANT_TYPE = {
    "single_ant": True,
    "double_ant": True,
    "four_ant": True
}


def signal_id_validator(signal_id):
    """
    validate signal_id
    :param signal_id:
    :return:
    """
    if isinstance(signal_id, list):
        for key_signal_id in signal_id:
            if not SignalModel.signal_exist_by_id(key_signal_id):
                raise serializers.ValidationError(u"%s is not exist in SignalModel!" % key_signal_id)
    if not SignalModel.signal_exist_by_id(signal_id):
        raise serializers.ValidationError(u"%s is not exist in SignalModel!" % signal_id)

def ant_type_validator(ant_type):
    if isinstance(ant_type, list):
        for key_ant_type in ant_type:
            if key_ant_type not in ANT_TYPE:
                raise serializers.ValidationError(u"%s is invalid!" % key_ant_type)
    if ant_type not in ANT_TYPE:
        raise serializers.ValidationError(u"%s is invalid!" % ant_type)