# coding=utf-8
from django.utils.translation import ugettext as _
from control.control.logger import getLogger

logger = getLogger(__name__)

PARAMETER_CODE = {
    # distri
    "distri_id": 10001,
    "distri_lon": 10002,
    "distri_lat": 10003,
    "distri_height": 10004,
    "distri_ves_num": 10005,
    "distri_mode": 10006
}

PARAMETER_MSG = {
    10001: _(u"参数distri_id不合法"),
    10002: _(u"参数distri_lon不合法"),
    10003: _(u"参数distri_lat不合法"),
    10004: _(u"参数distri_height不合法"),
    10005: _(u"参数distri_ves_num不合法"),
    10006: _(u"参数distri_mode不合法")
}