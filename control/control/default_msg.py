# coding=utf-8

class Defaultvalue(object):


    DEFAULT_VALUE = {
        "action_all": True,
            "action": None,
            "owner": "user-uio9m8on",
            "lon": 102.0,
            "lat": 31.8029,
            "height": 600,
            "vesnum": 500,
            "obtime": 12,
            "ant_pitch": 0,
            "ant_azimuth": 0,
            "ant_type": "yagi",
            "channel_type": "free space loss",
            "protocol": "SOTDMA",
            "snr": 0,
            "distri_mode": "random",
            "distri_id": None,
            "partable_id": None,
            "timetable_id": None,
            "aisdata_id": None,
            "signal_id": None
    }

    def __init__(self, payload):
        self.payload = payload

    def set_default_payload(self):
        payload = self.payload
        for key in payload.keys():
            if payload[key] is None:
                payload[key] = self.DEFAULT_VALUE[key]

        return payload
# DEFAULT_VALUE = {
#         "action_all": True,
#             "action": None,
#             "owner": "user-uio9m8on",
#             "lon": 102.0,
#             "lat": 31.8029,
#             "height": 600,
#             "vesnum": 500,
#             "obtime": 12,
#             "ant_pitch": 0,
#             "ant_azimuth": 0,
#             "ant_type": "yagi",
#             "channel_type": "free space loss",
#             "protocol": "SOTDMA",
#             "snr": 0,
#             "distri_mode": "random",
#             "distri_id": None,
#             "partable_id": None,
#             "timetable_id": None,
#             "aisdata_id": None,
#             "signal_id": None
#     }
#
#
# def set_default_payload(payload):
#     for key in payload.keys():
#         if payload[key] is None:
#             payload[key] = DEFAULT_VALUE[key]
#
#     return payload