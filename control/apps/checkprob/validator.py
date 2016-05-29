# coding=utf-8

from django.utils.translation import ugettext as _
from rest_framework import serializers

from control.apps.demod.models import DemodModel


def demodSignal_id_validator(demodSignal_id):
    """
    validate demodSignal_id
    :param demodSignal_id:
    :return:
    """
    if isinstance(demodSignal_id, list):
        for key_demodSignal_id in demodSignal_id:
            if DemodModel.demod_exist_by_id(key_demodSignal_id):
                raise serializers.ValidationError(u"demodSignal_id is not exist in DemodModel!")
    if DemodModel.demod_exist_by_id(demodSignal_id):
        raise serializers.ValidationError(u"demodSignal_id is not exist in DemodModel!")


