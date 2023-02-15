from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class BooksView(View):
    def __init__(self):
        return;

    def get(self, request):
        return HttpResponse('Result - GET');

    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     # <process form cleaned data>
        #     return HttpResponseRedirect('/success/')
        #
        # return render(request, self.template_name, {'form': form})
        return HttpResponse('Result - POST');


