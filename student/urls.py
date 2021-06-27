from django.conf.urls import url

from student.views import StudentListAPIView


urlpatterns = [
    url(r'^list$', StudentListAPIView.as_view(), name='students'),
]
