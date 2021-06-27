from rest_framework import generics

from student.models import Student
from student.serializers import StudentSerializer
from django_multiple_dbs.pagination import StandardResultSetPagination


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StandardResultSetPagination
