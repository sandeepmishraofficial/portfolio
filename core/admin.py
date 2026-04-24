from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import PersonalInfo, AboutCard, Highlight, Statistic, SkillCategory, Skill, ProjectTag, Project, VisitorLog

@admin.register(PersonalInfo)
class PersonalInfoAdmin(ModelAdmin):
    list_display = ('name', 'job_title', 'email')

@admin.register(AboutCard)
class AboutCardAdmin(ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(Highlight)
class HighlightAdmin(ModelAdmin):
    list_display = ('text', 'order')
    list_editable = ('order',)

@admin.register(Statistic)
class StatisticAdmin(ModelAdmin):
    list_display = ('label', 'value', 'order')
    list_editable = ('order',)

@admin.register(SkillCategory)
class SkillCategoryAdmin(ModelAdmin):
    list_display = ('name', 'data_cat', 'is_active_default', 'order')
    list_editable = ('is_active_default', 'order')

@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('name', 'category', 'level', 'order')
    list_filter = ('category',)
    list_editable = ('order',)

@admin.register(ProjectTag)
class ProjectTagAdmin(ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    filter_horizontal = ('tags',)

@admin.register(VisitorLog)
class VisitorLogAdmin(ModelAdmin):
    list_display = ('ip_address', 'path', 'method', 'timestamp')
    list_filter = ('method', 'timestamp')
    search_fields = ('ip_address', 'path', 'user_agent')
    readonly_fields = ('ip_address', 'user_agent', 'path', 'method', 'timestamp')
