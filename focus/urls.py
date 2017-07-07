from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addtodo', views.addtodo, name='addtodo'),
    url(r'^tododelete/(?P<id>[0-9]+)$', views.tododelete, name='delete'),
    url(r'^edittodo/(?P<id>[0-9]+)$', views.edittodo, name='edit'),
    url(r'^finishtodo/(?P<id>[0-9]+)$', views.finishtodo, name='finish'),
    url(r'^backtodo/(?P<id>[0-9]+)$', views.backtodo, name='back'),
]
