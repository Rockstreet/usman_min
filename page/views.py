from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.mail import send_mail


from django import http
from django.views.generic import View

from .models import Page, Sliders


class DetailView(generic.DetailView):
    model = Page
    template_name = 'page/page.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)


        context['carousel_block'] = Sliders.objects.all()

        context['slug'] = self.kwargs['slug']

        return context

class SendMailCls(View):
    def post(self,request):

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        send_message = '<h2>Сообщение с сайта CAIMAN </h2>'
        send_message = send_message+'<b>Имя:</b> '+name+'<br><br>'
        send_message = send_message+'<b>Телефон:</b> '+phone+'<br><br>'
        send_message = send_message+'<b>Сообщение:</b><br> '+message+'<br>'
        send_mail('Письмо с сайта CAIMAN', send_message, 'sendfromsite@caimanfishing.ru', ['ivan.tolkachev@gmail.com','orders@caimanfishing.ru'], fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=send_message)

        return HttpResponseRedirect('/page/goodpost')







