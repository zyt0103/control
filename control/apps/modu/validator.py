# encoding=utf-8

from rest_framework import serializers
from django.utils.translation import ugettext as _

from .models import DistriModel
from .models import PartableModel
from .models import TimetableModel
from .models import AisdataModel
from .models import SignalModel

from control.control.logger import getLogger

logger = getLogger(__name__)

DISTRI_MODE = {
    "default": True,
    "random": True,
    "uniform": True
}
ANT_TYPE = {
    "default": True,
    "yagi": True
}
CHANNEL_TYPE = {
    "default": True,
    "free space loss": True
}
PROTOCOL = {
    "default": True,
    "SOTDMA": True
}

ACTION = {
    "distri": True,
    "partable": True,
    "timetable": True,
    "aisdata": True,
    "signal": True
}



def action_all_validator(value):

    if not value:
        raise serializers.ValidationError(u"action_all is not exist！")


def action_validator(value):

    if not value or value not in ACTION:
        raise serializers.ValidationError(u"action is not exist or is invalid!")


def distri_id_validator(value):

    if isinstance(value, list):
        for k in value:
            if not DistriModel.distri_exist_by_id(k):
                raise serializers.ValidationError(_(u"%s not exist" % k))
    if not DistriModel.distri_exist_by_id(distri_id=value):
        raise serializers.ValidationError(_(u"%s not exist" % value))
        # return value


def distri_mode_validator(value):

    if not value or value not in DISTRI_MODE:
        raise serializers.ValidationError(_(u"distri_mode参数错误"))


def partable_id_validator(value):

    if isinstance(value, list):
        for k in value:
            if not PartableModel.partable_exist_by_id(k):
                raise serializers.ValidationError(_(u"%s not exist" % k))
    if not PartableModel.partable_exist_by_id(partable_id=value):
        raise serializers.ValidationError(_(u"%s not exist" % value))


def timetable_id_validator(value):

    if isinstance(value, list):
        for k in value:
            if not TimetableModel.timetable_exist_by_id(k):
                raise serializers.ValidationError(_(u"%s not exist" % k))
    if not TimetableModel.timetable_exist_by_id(timetable_id=value):
        raise serializers.ValidationError(_(u"%s not exist" % value))


def aisdata_id_validator(value):

    if isinstance(value, list):
        for k in value:
            if not AisdataModel.aisdata_exist_by_id(k):
                raise serializers.ValidationError(_(u"%s not exist" % k))
    if not AisdataModel.partable.aisdata_exist_by_id(aisdata_id=value):
        raise serializers.ValidationError(_(u"%s not exist" % value))


def signal_id_validator(value):

    if isinstance(value, list):
        for k in value:
            if not SignalModel.signal_exist_by_id(k):
                raise serializers.ValidationError(_(u"%s not exist" % k))
    if not SignalModel.signal_exist_by_id(signal_id=value):
        raise serializers.ValidationError(_(u"%s not exist" % value))


def lat_validator(value):

    if value < -90 or value > 90:
        raise serializers.ValidationError(_(u"lat 参数错误！"))


def lon_validator(value):

    if value < -180 or value > 180:
        raise serializers.ValidationError(_(u"lon 参数错误！"))


def height_validator(value):

    if value < 0:
        raise serializers.ValidationError(_(u"height 参数错误！"))

def vesnum_validator(value):
    if value < 0:
        raise serializers.ValidationError(_(u"vesnum 参数错误！"))


def obtime_validator(value):

    if value < 0:
        raise serializers.ValidationError(_(u"obtime 参数错误！"))


def ant_pitch_validator(value):
    logger.info("here")
    if value < -180 or value > 180:
        raise serializers.ValidationError(_(u"ant_pitch 参数错误！"))


def ant_azimuth_validator(value):

    if value < 0 or value > 360:
        raise serializers.ValidationError(_(u"ant_azimuth 参数错误！"))


def ant_type_validator(value):

    if not value or value not in ANT_TYPE:
        raise serializers.ValidationError(_(u"ant_type 参数错误！"))


def channel_type_validator(value):

    if not value or value not in CHANNEL_TYPE:
        raise serializers.ValidationError(_(u"channel_type 参数错误！"))


def protocol_validator(value):

    if not value or value not in PROTOCOL:
        raise serializers.ValidationError(u"protocol 参数错误！")


def snr_validator(value):

    if value < 0:
        raise serializers.ValidationError(u"snr 参数错误！")