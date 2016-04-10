# coding=utf-8
from rest_framework import serializers

class CreateSignalValidator(serializers.Serializer):
    """
    创建信号
    """
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CreateSignalValidator, self).__init__(*args, **kwargs)


    def create(self, validata_data):
