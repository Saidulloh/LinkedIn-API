from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.users.models import WorkExperience, Skills, Education


User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_at')

admin.site.register(User, UserAdmin)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Skills, SkillsAdmin)


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(WorkExperience, WorkExperienceAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Education, EducationAdmin)
