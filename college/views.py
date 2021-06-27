from rest_framework import generics

from college.models import College
from college.serializers import CollegeSerializer
from django_multiple_dbs.pagination import StandardResultSetPagination


class CollegeListAPIView(generics.ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    pagination_class = StandardResultSetPagination
