from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializer import *
from .models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# @api_view(['GET'])
# def assessment_list(request):
#     if request.method == 'GET':
#         assessment = Assessment.objects.all()
#         serializer = AssessmentSerializers(assessment, many=True)
#         return Response(serializer.data)


@api_view(['GET'])
def assessment_list(request):
    """ List all assessments or create a new assessment (Teacher only) """
    if request.method == 'GET':
        assessments = Assessment.objects.all()
        data = []

        for assessment in assessments:
            data.append({
                'id': assessment.id,
                'title': assessment.title,
                'type': assessment.type,
                'status': assessment.status,
                'instructions': assessment.instructions,
                'time_limit': assessment.time_limit,
                'num_attempts': assessment.num_attempts,
                'immediate_feedback': assessment.immediate_feedback,
                'publish_date': assessment.publish_date,
                'popularity': assessment.popularity,
                'completion_rate': assessment.completion_rate,
                'feedback_message': assessment.feedback_message,
                'course': {
                    'id': assessment.course.id,
                    'name': assessment.course.name
                },
                'created_by': {
                    'id': assessment.created_by.id,
                    'name': assessment.created_by.username
                }
            })

        return Response(data)