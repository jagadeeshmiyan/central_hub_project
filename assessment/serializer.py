from rest_framework import serializers
from .models import *


class AssessmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SubmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'name'