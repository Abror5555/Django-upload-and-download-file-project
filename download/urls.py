from django.urls import path
from download.views import IndexView
app_name = 'download'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
