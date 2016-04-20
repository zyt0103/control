# coding=utf-8
from django.utils.translation import ugettext as _
from control.control.err_msg import PARAMETER_CODE


def convert_to_string(data):
    """
    Convert dict/list to string by:
        geting the firt item of firt value
    """
    if isinstance(data, dict):
        return convert_to_string(data.values()[0])
    elif isinstance(data, list):
        return convert_to_string(data[0])
    elif not isinstance(data, basestring):
        return str(data)
    return data

def is_simple_string_list(data):
    """
    Check if data is a string list.
    """
    if not isinstance(data, list):
        return False

    for ret in data:
        if not isinstance(ret, basestring):
            return False

    return True

def get_code_by_parameter(parameter):
    return PARAMETER_CODE.get(parameter)


def control_code(validator):
    if not validator:
        return -1, ""
    errors = validator.errors
    if errors.keys():
        parameter = errors.keys()[0]
        msg = errors.get(parameter)[0]
        code = get_code_by_parameter(parameter)
        return code, msg
    else:
        return -1, ""


def control_response(code=0,
                     msg=_(u"服务器相应成功"),
                     total_count=0,
                     ret_set=None,
                     action_record=None, **kwargs):
    msg = convert_to_string(msg)

    if code == 0:
        parameter_msg = _(u"服务器响应成功")
    else:
        parameter_msg = _(u"服务器响应失败")

    ret = {"ret_code": code, "msg": msg}
    ret["ret_msg"] = parameter_msg  # temp msg

    if code == 0 or total_count != 0:
        ret["total_count"] = total_count
        ret["ret_set"] = ret_set or []

    if action_record is not None:
        if is_simple_string_list(action_record):
            action_record = ','.join(action_record)
        ret["action_record"] = action_record
    ret.update(kwargs)

    return ret