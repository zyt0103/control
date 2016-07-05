# coding=utf-8

from django.utils.translation import ugettext as _
from rest_framework import serializers

from control.apps.modu.models import SignalModel
from control.apps.demod.models import DemodType


ANT_NUM = {
    1: 1,
    2: 2,
    4: 4
}

PROTOCOL_TYPE = {
    "1": "GMSK"
}

SYNC_TYPE = {
    "1": "时频联合同步"
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
    elif not SignalModel.signal_exist_by_id(signal_id):
        raise serializers.ValidationError(u"%s is not exist in SignalModel!" % signal_id)

def demod_type_id_validator(demod_type_id):
    if isinstance(demod_type_id, list):
        for key_demod_type_id in demod_type_id:
            if not DemodType.demodtype_exist_by_id(key_demod_type_id):
                raise serializers.ValidationError(u"%s is not exist in DemodType!" % key_demod_type_id)
    elif not DemodType.demodtype_exist_by_id(demod_type_id):
        raise serializers.ValidationError(u"%s is not exist in DemodType!" % demod_type_id)

def ant_num_validator(ant_num):
    if ant_num not in ANT_NUM:
        raise serializers.ValidationError(u"ant_num is invalid!")

def protocol_validator(protocol_type):
    """
    validator protocol
    :return:
    """
    if isinstance(protocol_type, list):
        for key_protocol_type in protocol_type:
            if key_protocol_type not in PROTOCOL_TYPE:
                raise serializers.ValidationError(u"protocol_type is invalid!")
    elif protocol_type not in PROTOCOL_TYPE:
        raise serializers.ValidationError(u"protocol_type is invalid")

def sync_type_validator(sync_type):
    """
    validate sync_type
    :param sync_type:
    :return:
    """
    if isinstance(sync_type, list):
        for key_sync_type in sync_type:
            if key_sync_type not in SYNC_TYPE:
                raise serializers.ValidationError(u"sync_type is invalid!")
    elif sync_type not in SYNC_TYPE:
        raise serializers.ValidationError(u"sync_type is invalid!")
