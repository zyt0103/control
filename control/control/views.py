# coding = utf-8
__author__ = 'houjincheng'
from django.template import Context
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.admin import User

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from control.apps.modu.models import SignalModel
from control.apps.modu.sub_view import SaveSignalInfo

from control.apps.demod.models import DemodType, DemodModel

from control.control.base import getLogger
logger = getLogger(__name__)


class newindex(View):
    def get(self, request):
        user_id = request.REQUEST.get("user_id", "user-safoewfw")
        signal = SignalModel.objects.filter(deleted=False).filter(partable__distri__user__username=user_id)
        paginator = Paginator(signal, 12)
        page = request.REQUEST.get("page", 1)
        try:
            signal = paginator.page(page)
        except PageNotAnInteger:
            signal = paginator.page(1)
        except EmptyPage:
            signal = paginator.page(paginator.num_pages)

        for signal_index in signal:
            if signal_index.schedule != 1 or signal_index.signal_size == 0:
                SaveSignalInfo(signal_index.signal_id)
        info = []
        for i in range(len(signal)):
            signal_info = {"name_signal": signal[i].name_signal,
                           "signal_id": signal[i].signal_id,
                           "size": int(signal[i].signal_size),
                           "status": signal[i].schedule * 100,
                           "create_time": signal[i].create_datetime,
                           "channel_num": signal[i].channel_num
                           }
            info.append(signal_info)
        return render(request, "index/newIndex.html", Context({"Info": info, "topics": signal}))


class demodul(View):

    def get(self, request):
        user_id = request.GET.get("user_id", "user-safoewfw")
        demod_type = DemodType.objects.filter(deleted=False).filter(user_id=user_id)
        paginator = Paginator(demod_type, 12)
        page = request.GET.get("page", 1)

        try:
            demod_type = paginator.page(page)
        except PageNotAnInteger:
            demod_type = paginator.page(1)
        except EmptyPage:
            demod_type = paginator.page(paginator.num_pages)

        dict_obj = {}
        dict_obj['demo_list'] = []
        for type in demod_type:
            temp = {}
            temp.update({'demod_type_name': type.demod_type_name, 'ant_num': type.ant_num,
                         'protocol': type.PROTOCOL_TYPE[int(type.protocol)-1][1], 'sync_type': type.SYNC_TYPE[int(type.sync_type)-1][1],
                         'demod_type_id': type.demod_type_id})
            dict_obj['demo_list'].append(temp)
        return render(request, "index/demodul.html", dict_obj)


class analysis(View):

    def get(self, request):
        analysis_list = DemodModel.objects.all()
        paginator = Paginator(analysis_list, 12)
        page = request.GET.get("page", 1)

        try:
            analysis_list = paginator.page(page)
        except PageNotAnInteger:
            analysis_list = paginator.page(1)
        except EmptyPage:
            analysis_list = paginator.page(paginator.num_pages)

        dict_obj = {}
        dict_obj['analysis_list'] = []
        for type in analysis_list:
            temp = {}
            temp.update({'signal_id': type.signal_id, 'demod_type_id': type.demod_type_id, 'status': type.status,
                         'demod_prob_fact': type.demod_prob_fact, 'demod_prob_theory': type.demod_prob_theory})
            dict_obj['analysis_list'].append(temp)
        return render(request, "index/analysis.html", dict_obj)

class addmodal(View):
    def get(self, request):

        return render(request, "index/addmodal.html")


class addmodalDemodul(View):
    def get(self, request):

        return render(request, "index/addModalDemodul.html")


class addmodalType(View):
    def get(self, request):
        min_ant_num = request.GET.get('minAntNum', 4)
        demodType = DemodType.filter_demodtype_by_antNum_lte(min_ant_num)
        dict_obj = {}
        dict_obj['demo_list'] = []
        for type in demodType:
            temp = {}
            temp.update({'demod_type_name': type.demod_type_name, 'ant_num': type.ant_num,
                         'protocol': type.PROTOCOL_TYPE[int(type.protocol)-1][1], 'sync_type': type.SYNC_TYPE[int(type.sync_type)-1][1],
                         'demod_type_id': type.demod_type_id})
            dict_obj['demo_list'].append(temp)
        return render(request, "index/addModalType.html", dict_obj)


class paramAnalysis(View):
    def get(self, request):

        return render(request, "index/paramAnalysis.html")

class demodulResult(View):
    def get(self, request):
        return render(request, "index/demodulResult.html")

class checkPro(View):
    def get(self, request):

        return render(request, "index/checkPro.html")

class pic(View):
    def get(self, request):

        return render(request, "index/pic.html")
