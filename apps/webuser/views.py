import logging

from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
# from gargoyle import gargoyle
from jsonview.decorators import json_view

from webuser.forms import LoginForm
from django.utils.translation import ugettext as _


@require_http_methods(["POST"])
@json_view
def sign_up(request):

    result = {'succ': False}
    form = LoginForm(request.POST)

    if not form.is_valid():
        return result

    name = form.cleaned_data.get("name")

    signature, pubkey = form.cleaned_data.get("sign"), form.cleaned_data.get("public_key")
    sign_data = form.cleaned_data.get("sign_data")
    source = form.cleaned_data.get("source")
    to_sign = form.cleaned_data.get("to_sign")

    if source == 1 and name != to_sign:
        result['msg'] = _('Account exception')
        return result

    msg = sign_data

    user = authenticate(msg=msg, to_sign=to_sign, sig=signature, pubkey=pubkey, name=name, source=source)
    if user:
        login(request, user)
        result['succ'] = True

    return result


def log_out(request):
    logout(request)
    return JsonResponse({'succ': True})


def login_page(request):
    return render(request, 'page/test.html', locals())
