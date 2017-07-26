# -*- coding: utf-8 -*-
"""UI view definitions."""

import urllib

from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


def login(request):
    if not request.user.is_authenticated():
        # perserve redirects ("next" in request.GET)
        return redirect(
            reverse('osm:begin', args=['openstreetmap']) + '?' +
            urllib.urlencode(request.GET))
    else:
        return redirect('/v3/')


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/v3/')


def v3(request):
    return render(request, 'ui/v3.html')


def require_email(request):
    """
    View to handle email collection for new user logging in with OSM account.
    """
    return render(request, 'osm/email.html')


# error views


@require_http_methods(['GET'])
def create_error_view(request):
    return render(request, 'ui/error.html', status=500)


def internal_error_view(request):
    return render(request, 'ui/500.html', status=500)


def not_found_error_view(request):
    return render(request, 'ui/404.html', status=404)


def not_allowed_error_view(request):
    return render(request, 'ui/403.html', status=403)
