from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'inbound', views.voice, name='voice'),
    url(r'choice', views.choices, name='digit_choice'),
    url(r'voicemail', views.mail, name='leave_voicemail'),
]
