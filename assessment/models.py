from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.conf import settings


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_teacher = models.BooleanField(default=False)
#     # Add any other fields you need

#     def __str__(self):
#         return self.user.username

class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f"{self.name} is handeled by {self.teacher}"


class Assessment(models.Model):
    TYPE_CHOICES = [
        ('quiz', 'Quiz'),
        ('assignment', 'Assignment'),
        ('survey', 'Survey'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assessments')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    instructions = models.TextField(blank=True, null=True)
    time_limit = models.IntegerField(null=True, blank=True, help_text="Time limit in minutes")
    num_attempts = models.IntegerField(default=1)
    immediate_feedback = models.BooleanField(default=True, help_text="Provide immediate feedback after submission")
    publish_date = models.DateTimeField(null=True, blank=True)
    popularity = models.IntegerField(default=0)
    completion_rate = models.FloatField(default=0)  # Track completion rates
    feedback_message = models.TextField(null=True, blank=True)  # Specific feedback for students

    def __str__(self):
        return self.title

    def calculate_completion_rate(self):
        total_submissions = self.submissions.count()
        completed_submissions = self.submissions.filter(graded=True).count()
        if total_submissions == 0:
            return 0
        return (completed_submissions / total_submissions) * 100


class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('mcq', 'Multiple Choice'),
        ('short_answer', 'Short Answer'),
        ('essay', 'Essay'),
        ('true_false', 'True/False'),
    ]

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)
    options = models.JSONField(null=True, blank=True, help_text="Use for MCQ options")
    correct_answer = models.TextField(null=True, blank=True, help_text="Correct answer for the question")
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text


class Submission(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    graded = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.username} - {self.assessment.title}'


class QuestionBank(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='question_banks')
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.teacher.username} - {self.question.question_text}'


class StudentCourse(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_students')

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.name}'

