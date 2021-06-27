from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'age', 'gender', 'created_at', 'modified_at']
