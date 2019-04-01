from django.conf.urls import url

from webuser import views

urlpatterns = [
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^login_page$', views.login_page, name='login_page'),
    url(r'^logout$', views.log_out, name='logout'),
]
