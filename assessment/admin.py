from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(Profile)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ['get_username', 'get_email', 'is_teacher']
#     list_filter = ['is_teacher']

#     def get_username(self, obj):
#         return obj.user.username

#     def get_email(self, obj):
#         return obj.user.email

#     get_username.admin_order_field = 'user__username'  # Allows column order sorting
#     get_username.short_description = 'Username'  # Renames column head
#     get_email.admin_order_field = 'user__email'
#     get_email.short_description = 'Email'

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_teacher']
    list_filter = ['is_teacher']



admin.site.register(Course)
admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(QuestionBank)
admin.site.register(StudentCourse)