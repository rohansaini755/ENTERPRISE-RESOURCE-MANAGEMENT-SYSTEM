import datetime
import pytz
from django.http import HttpResponseForbidden,HttpResponseNotAllowed
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.response import Response

from django.contrib.sessions.models import Session

class SessionMiddleware:
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '*':
            response = self.get_response(request)
            return response
        else:
            if request.path == '/api/checksession/':
                request.session.modified = False
            else:
                request.session.modified = True

            response = self.get_response(request)

            session_key = request.headers.get('bid')
            if session_key:
                session = Session.objects.filter(session_key=session_key).first()

                if session:
                    if session.expire_date < timezone.now():
                        return HttpResponseForbidden("Your session has expired.")
                else:
                    return HttpResponseNotAllowed("Invalid session key.")

            return response
