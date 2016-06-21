# coding=utf-8
from django.db import models

from control.apps.modu.models import BaseModel
from control.control.base import getLogger

logger = getLogger(__name__)


class DemodModelManager(models.Manager):
    def create(self,
               signal_id,
               demod_type_id,
               demod_prob_fact,
               demod_prob_theory):
        try:
            demod = DemodModel(signal_id=signal_id,
                                       demod_type_id=demod_type_id,
                                       demod_prob_fact=demod_prob_fact,
                                       demod_prob_theory=demod_prob_theory)
            demod.save()
            return demod, None
        except Exception as exp:
            logger.error("DemodResult save error: %s" % exp)
            return None, exp

class DemodTypeManager(models.Manager):
    def create(self,
               user_id,
               demod_type_id,
               demod_type_name,
               ant_num,
               protocol,
               sync_type):
        try:
            demod_type = DemodType(user_id=user_id,
                                   demod_type_id=demod_type_id,
                                   demod_type_name=demod_type_name,
                                   ant_num=ant_num,
                                   protocol=protocol,
                                   sync_type=sync_type)

            demod_type.save()
            return demod_type, None
        except Exception as exp:
            logger.error("demodType save error: %s" % exp)
            return None, exp


class DemodResultManager(models.Manager):
    def create(self,
               signal_id,
               demod_type_id,
               signal_demoded):
        try:
            signal_res = DemodResult(signal_id=signal_id,
                                     demod_type_id=demod_type_id,
                                     signal_demoded=signal_demoded)
            signal_res.save()
            return signal_res, None
        except Exception as exp:
            logger.error("demodResult save error: %s" % exp)
            return None, exp


class DemodModel(BaseModel):
    """
        Demodulate
    """
    class Meta:
        db_table = 'demod'
    signal_id = models.CharField(
        max_length=20,
        null=False,
        unique=False
    )

    demod_type_id = models.CharField(
        max_length=20,
        null=False
    )

    status = models.IntegerField(
        verbose_name=u"解调状态",
        null=True
    )
    demod_prob_fact = models.IntegerField(
        verbose_name=u"实际检测概率",
        blank=False,
        null=True
    )

    demod_prob_theory = models.IntegerField(
        verbose_name=u"理论检测概率",
        blank=False,
        null=True
    )

    objects = DemodModelManager()

    @classmethod
    def demod_exist_by_id(cls, signal_id, demod_type_id, deleted=False):
        """
        验证demod_model 是否存在
        :param signal_id:
        :return:
        """
        try:
            return DemodModel.objects.filter(deleted=deleted).filter(signal_id=signal_id).filter(demod_type_id).exists()
        except Exception as exp:
            logger.warning("demod exist error: %s" % exp)
            return False

    @classmethod
    def delete_demod_result_by_id(cls, signal_id, demod_type_id):
        try:
            if signal_id and demod_type_id:
                res = DemodModel.objects.filter(signal_id=signal_id).filter(demod_type_id=demod_type_id)
                if res:
                    res.delete()
            elif signal_id and not demod_type_id:
                res = DemodModel.objects.filter(signal_id=signal_id)
                if res:
                    res.delete()
            elif not signal_id and demod_type_id:
                res = DemodModel.objects.filter(demod_type_id=demod_type_id)
                if res:
                    res.delete()
            return True, None
        except Exception as exp:
            logger.warning("delete demodResult error %s" % exp)
            return False, exp

    @classmethod
    def update_fact_demod_result_by_id(cls, signal_id, demod_type_id, demod_prob_fact):
        try:
            res = DemodResult.objects.filter(signal_id=signal_id).get(demod_prob_fact=demod_prob_fact)
            res.demod_prob_fact = demod_prob_fact
            res.save()
        except Exception as exp:
            logger.error("update fact demodResult error %s" % exp)
            return False, exp


class DemodType(BaseModel):
    """
        解调方式创建
    """
    class Meta:
        db_table = 'demodtype'

    PROTOCOL_TYPE = (
        (1, u"GMSK"),
    )

    SYNC_TYPE = (
        (1, u"时频联合同步"),
    )
    user_id = models.CharField(
        max_length=20,
        null=False
    )

    demod_type_id = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )

    demod_type_name = models.CharField(
        max_length=80,
        null=False,
        blank=True
    )

    ant_num = models.IntegerField(
        null=False,
        unique=False
    )

    protocol = models.IntegerField(
        choices=PROTOCOL_TYPE,
        null=False,
        unique=False
    )

    sync_type = models.IntegerField(
        choices=SYNC_TYPE,
        null=False,
        unique=False
    )

    objects = DemodTypeManager()

    @classmethod
    def delete_demodtype_by_id(cls, demodType_id, deleted=False):
        try:
            DemodType.objects.filter(deleted=deleted).get(demod_type_id=demodType_id).delete()
            return True
        except Exception as exp:
            logger.error("delete demodtype error: %s" % exp)
            return False

    @classmethod
    def get_demodtype_by_id(cls,demodType_id, deleted=False):
        try:
            return DemodType.objects.filter(deleted=deleted).get(demod_type_id=demodType_id)
        except Exception as exp:
            return None

    @classmethod
    def filter_demodtype_by_antNum_lte(cls, antNum, deleted=False):
        try:
            return DemodType.objects.filter(deleted=deleted).filter(ant_num__lte=antNum)
        except Exception as exp:
            logger.warning("filter demodType error: %s" % exp)
            return []

    @classmethod
    def demodtype_exist_by_id(cls, demod_type_id, deleted=False):
        try:
            return DemodType.objects.filter(demod_type_id=demod_type_id).exists()
        except Exception as exp:
            return False


class DemodResult(BaseModel):
    class Meta:
        db_table = "demodresult"

    signal_id = models.CharField(max_length=20, null=False)
    demod_type_id = models.CharField(max_length=20, null=False)
    signal_demoded = models.CharField(max_length=200, null=False)

    objects = DemodResultManager()

    @classmethod
    def delete_demod_result_by_id(cls, signal_id, demod_type_id):
        try:
            if signal_id and demod_type_id:
                res = DemodResult.objects.filter(signal_id=signal_id).filter(demod_type_id=demod_type_id)
                if res:
                    res.delete()
            elif signal_id and not demod_type_id:
                res = DemodResult.objects.filter(signal_id=signal_id)
                if res:
                    res.delete()
            elif not signal_id and demod_type_id:
                res = DemodResult.objects.filter(demod_type_id=demod_type_id)
                if res:
                    res.delete()
            return True, None
        except Exception as exp:
            logger.warning("delete demodResult error %s" % exp)
            return False, exp


    @classmethod
    def describe_demod_result_by_id(cls, signal_id, demod_type_id):
        try:
            res = DemodResult.objects.filter(signal_id=signal_id).filter(demod_type_id=demod_type_id).order_by('create_datetime')
            return res, None
        except Exception as exp:
            logger.error("update fact demodResult error %s" % exp)
            return None, exp