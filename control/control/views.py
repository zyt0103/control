# coding = utf-8
__author__ = 'houjincheng'
from django.template import Context
from django.conf import settings
# from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import RequestContext
from django.views.generic import View
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from control.apps.modu.models import SignalModel
from control.apps.modu.sub_view import SaveSignalInfo

from control.apps.demod.models import DemodType

from control.control.base import getLogger
logger = getLogger(__name__)


class Index(View):
    def get(self, request, *args, **kwargs):
        # return render_to_response("index/index.html",
        #                           context_instance=RequestContext(request, locals()))
        return render(request, "index/index.html")


class test(View):
    def get(self, request, *args, **kwargs):
        # return render_to_response("index/index.html",
        #                           context_instance=RequestContext(request, locals()))
        return render(request, "index/test.html")


class plot(View):
    def get(self, request, *args, **kwargs):
        # return render_to_response("index/index.html",
        #                           context_instance=RequestContext(request, locals()))
        return render(request, "index/plot.html")


class drag(View):
    def get(self, request, *args, **kwargs):
        # return render_to_response("index/index.html",
        #                           context_instance=RequestContext(request, locals()))
        return render(request, "index/drag.html")


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
                           "create_time": signal[i].create_datetime
                           }
            info.append(signal_info)
        return render(request, "index/newIndex.html", Context({"Info": info, "topics": signal}))


class demodul(View):

    def get(self, request):
        user_id = request.REQUEST.get("user_id", "user-safoewfw")
        demod_type = DemodType.objects.filter(deleted=False).filter(user_id=user_id)
        paginator = Paginator(demod_type, 12)
        page = request.REQUEST.get("page", 1)

        try:
            demod_type = paginator.page(page)
        except PageNotAnInteger:
            demod_type = paginator.page(1)
        except EmptyPage:
            demod_type = paginator.page(paginator.num_pages)

        return render(request, "index/demodul.html", {"topics": demod_type})


class analysis(View):

    def get(self, request):

        return render(request, "index/analysis.html")

class addmodal(View):
    def get(self, request):

        return render(request, "index/addmodal.html")


class addmodalDemodul(View):
    def get(self, request):

        return render(request, "index/addModalDemodul.html")


class addmodalType(View):
    def get(self, request):
        dict_obj = {}
        dict_obj['demo_list'] = []
        for i in range(0, 4):
            temp = {}
            temp.update({'type_name_de': u'method_1', 'ant_type_de': 'single_ant',
                         'protocol_de': 'SOTDMA', 'sync_type': 'DEFAULT',
                         'mod_type':'gmsk'})
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
