from django.conf.urls import url

from . import views

app_name = 'ACUser'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doLoginOrRegister$', views.do_login_or_register, name='doLoginOrRegister'),
    url(r'^user$', views.user_detail, name='user'),
    url(r'^renew/(?P<minutes>(0|[1-9][0-9]*))$', views.renew, name='renew'),
    url(r'^stop_all$', views.stop_all, name='stopAll'),
]
