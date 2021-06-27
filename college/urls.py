from django.conf.urls import url

from college.views import CollegeListAPIView


urlpatterns = [
    url(r'^list$', CollegeListAPIView.as_view(), name='colleges'),
]
