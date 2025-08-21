
from django.urls import path
from website.views import *


urlpatterns = [
    path('', index_view),
    path('', about_view),
    path('contact', contact_view)
]
