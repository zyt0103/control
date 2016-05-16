# encoding=utf-8

from django.utils.translation import ugettext as _
from django.contrib.auth.admin import User
from rest_framework import serializers

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

ACTION_LIST = [
    "distri",
    "partable",
    "timetable",
    "aisdata",
    "signal"
]



def action_all_validator(action_all):
    """
    validate action_all
    :param action_all: 是否产生所有的信号
    :return:
    """
    if not action_all:
        logger.error(u"action_all is not exist")
        raise serializers.ValidationError(u"action_all is not exist！")


def action_validator(action):
    """
    validate action
    :param action: 所需产生动作
    :return:
    """
    if not action or action not in ACTION_LIST:
        logger.error(u"action is not exist")
        raise serializers.ValidationError(u"action is not exist or is invalid!")


def username_validator(username):
    """
    validate username
    :param username: username
    :return: 异常
    """
    if not User.objects.filter(username=username).exist():
        raise serializers.ValidationError(u"The username is already exist in database!")


def distri_id_validator(distri_id):
    """
    validate distri_id
    :param distri_id:
    :return:
    """
    if isinstance(distri_id, list):
        for k in distri_id:
            if not DistriModel.distri_exist_by_id(k):
                logger.error("%s is not exist" % distri_id)
                raise serializers.ValidationError(_(u"%s not exist in DistriModel" % k))
    if not DistriModel.distri_exist_by_id(distri_id=distri_id):
        logger.error("%s is not exist" % distri_id)
        raise serializers.ValidationError(_(u"%s not exist in DistriModel" % distri_id))
        # return value


def distri_mode_validator(distri_mode):
    """
    validate distri_mode
    :param distri_mode:
    :return:
    """
    if not distri_mode or distri_mode not in DISTRI_MODE:
        # logger.info("distri_mode is %s"%value
        logger.error("%s is not exist" % distri_mode)
        raise serializers.ValidationError(_(u"distri_mode参数错误"))


def partable_id_validator(partable_id):
    """
    validate partable_id
    :param partable_id:
    :return:
    """
    if isinstance(partable_id, list):
        for k in partable_id:
            if not PartableModel.partable_exist_by_id(k):
                logger.error("%s is not exist" % partable_id)
                raise serializers.ValidationError(_(u"%s not exist in PartableModel" % k))
    if not PartableModel.partable_exist_by_id(partable_id=partable_id):
        logger.error("%s is not exist" % partable_id)
        raise serializers.ValidationError(_(u"%s not exist in PartableModel" % partable_id))


def timetable_id_validator(timetable_id):
    """
    validate timetable_id
    :param timetable_id:
    :return:
    """
    if isinstance(timetable_id, list):
        for k in timetable_id:
            if not TimetableModel.timetable_exist_by_id(k):
                logger.error("%s is not exist" % timetable_id)
                raise serializers.ValidationError(_(u"%s not exist in TimetableModel" % k))
    if not TimetableModel.timetable_exist_by_id(timetable_id=timetable_id):
        logger.error("%s is not exist" % timetable_id)
        raise serializers.ValidationError(_(u"%s not exist in TimetableModel" % timetable_id))


def aisdata_id_validator(aisdata_id):
    """
    validate aisdate_id
    :param aisdata_id:
    :return:
    """
    logger.info("the aisdata is %s" % aisdata_id )
    if isinstance(aisdata_id, list):
        logger.info("the aisdata list is ")
        for k in aisdata_id:
            if not AisdataModel.aisdata_exist_by_id(k):
                logger.error("%s is not exist" % aisdata_id)
                raise serializers.ValidationError(_(u"%s not exist in AisdataModel" % k))
    if not AisdataModel.aisdata_exist_by_id(aisdata_id=aisdata_id):
        logger.error("%s is not exist" % aisdata_id)
        raise serializers.ValidationError(_(u"%s not exist in AisdataModel" %aisdata_id))


def signal_id_validator(signal_id):
    """
    validata signal_id
    :param signal_id:
    :return:
    """
    if isinstance(signal_id, list):
        for k in signal_id:
            if not SignalModel.signal_exist_by_id(k):
                logger.error("%s is not exist" % signal_id)
                raise serializers.ValidationError(_(u"%s not exist in SignalModel" % k))
    if not SignalModel.signal_exist_by_id(signal_id=signal_id):
        logger.error("%s is not exist" % signal_id)
        raise serializers.ValidationError(_(u"%s not exist in SignalModel" % signal_id))


def lat_validator(lat):
    """
    validate lat
    :param lat:
    :return:
    """
    if lat < -90 or lat > 90:
        logger.error("%s parameter error" % lat)
        raise serializers.ValidationError(_(u"lat 参数错误！"))


def lon_validator(lon):
    """
    validate lon
    :param lon:
    :return:
    """
    if lon < -180 or lon > 180:
        logger.error("%s parameter error" % lon)
        raise serializers.ValidationError(_(u"lon 参数错误！"))


def height_validator(height):
    """
    validate height
    :param height:
    :return:
    """
    if height < 0:
        logger.error("%s parameter error" % height)
        raise serializers.ValidationError(_(u"height 参数错误！"))

def vesnum_validator(vesnum):
    """
    validate vesnum
    :param vesnum:
    :return:
    """
    if vesnum < 0:
        logger.error("%s parameter error" % vesnum)
        raise serializers.ValidationError(_(u"vesnum 参数错误！"))


def obtime_validator(obtime):
    """
    validate obtime
    :param obtime:
    :return:
    """
    if obtime < 0:
        logger.error("%s parameter error" % obtime)
        raise serializers.ValidationError(_(u"obtime 参数错误！"))


def ant_pitch_validator(ant_pitch):
    """
    validate ant_pitch
    :param ant_pitch:
    :return:
    """
    logger.info("here")
    if ant_pitch < -180 or ant_pitch > 180:
        logger.error("%s parameter error" % ant_pitch)
        raise serializers.ValidationError(_(u"ant_pitch 参数错误！"))


def ant_azimuth_validator(ant_azimuth):
    """
    validate ant_azimuth
    :param ant_azimuth:
    :return:
    """
    if ant_azimuth < 0 or ant_azimuth > 360:
        logger.error("%s parameter error" % ant_azimuth)
        raise serializers.ValidationError(_(u"ant_azimuth 参数错误！"))


def ant_type_validator(ant_type):
    """
    validate ant_type
    :param ant_type:
    :return:
    """
    if not ant_type or ant_type not in ANT_TYPE:
        logger.error("%s parameter error" % ant_type)
        raise serializers.ValidationError(_(u"ant_type 参数错误！"))


def channel_type_validator(channel_type):
    """
    validate channel_type
    :param channel_type:
    :return:
    """
    if not channel_type or channel_type not in CHANNEL_TYPE:
        logger.error("%s parameter error" % channel_type)
        raise serializers.ValidationError(_(u"channel_type 参数错误！"))


def protocol_validator(protocol):
    """
    validate protocol
    :param protocol:
    :return:
    """
    if not protocol or protocol not in PROTOCOL:
        logger.error("%s parameter error" % protocol)
        raise serializers.ValidationError(u"protocol 参数错误！")


def snr_validator(snr):
    """
    validate snr
    :param snr:
    :return:
    """
    if snr < 0:
        logger.error("%s parameter error" % snr)
        raise serializers.ValidationError(u"snr 参数错误！")