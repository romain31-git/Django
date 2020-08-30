from django.conf.urls import url
from . import views
from .views import StudentCreateView, Edit, absent
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^student/edit/(?P<pk>\d+)$', Edit.as_view(), name='edit_student'),
    url(r'^student/absence/$', absent.as_view(), name='absence'),
]
