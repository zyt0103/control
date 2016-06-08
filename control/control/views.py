# coding = utf-8
__author__ = 'houjincheng'

from django.conf import settings
# from django.shortcuts import render_to_response
from django.shortcuts import render
# from django.shortcuts import RequestContext
from django.views.generic import View
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

        return render(request, "index/newIndex.html")
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
            temp.update({'type': u'method_1', 'ant_type': 'single_type',
                         'protocol': 'default', 'sync_type': 'sotdma',
                         'mod_type':'gmsk'})
            dict_obj['demo_list'].append(temp)
        return render(request, "index/addModalType.html",dict_obj)