from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
#
# from django_testing.settings import MAX_STUDENTS_PER_COURSE
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'students')

    # def validate(self, data):
    #     """Метод для валидации. Вызывается при создании и обновлении."""
    #     if len(self.initial_data.get('students')) > MAX_STUDENTS_PER_COURSE:
    #         raise ValidationError(f'максимальное число студентов на курсе – 20')
    #     return data
