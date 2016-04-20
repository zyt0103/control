# encoding=utf-8

from rest_framework import serializers
from django.utils.translation import ugettext as _

from .models import DistriModel
from .models import PartableModel
from .models import TimetableModel
from .models import SignalModel

from control.control.logger import getLogger

logger = getLogger(__name__)

DISTRI_MODE = {
    "default": True,
    "random": True,
    "uniform": True
}

def distri_id_validator(value):
    if isinstance(value, list):
        for k in value:
            if not DistriModel.distri_exist_by_id(k):
                raise serializers.ValidationError(_(u"%s not exist" %k))
    if not DistriModel.distri_exist_by_id(distri_id=value):
        raise serializers.ValidationError(_(u"%s not exist" %value))


def distri_mode_validator(value):
    if not value or value not in DISTRI_MODE:
        raise serializers.ValidationError(_(u"distri_mode参数错误"))