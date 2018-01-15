from django.contrib import admin
from django.conf.urls import url
from django.urls import path
import grade_horaria_pdf_service_admin.views
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('pdf/(?P<grade_oid>[\w\-]+)/$', grade_horaria_pdf_service_admin.views.index),
    url(r'^clear_cache/', grade_horaria_pdf_service_admin.views.clear_cache),
]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]
