from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from .models import PersonalInfo, AboutCard, Highlight, Statistic, SkillCategory, Project

def home(request):
    personal_info = PersonalInfo.objects.first()
    about_cards = AboutCard.objects.all()
    highlights = Highlight.objects.all()
    statistics = Statistic.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.prefetch_related('tags').all()

    context = {
        'personal_info': personal_info,
        'about_cards': about_cards,
        'highlights': highlights,
        'statistics': statistics,
        'skill_categories': skill_categories,
        'projects': projects,
    }
    return render(request, 'core/index.html', context)


def service_worker(request):
    """
    Serve the Service Worker JS file from root scope (/serviceworker.js).
    The Service-Worker-Allowed header grants it control over the entire origin.
    """
    sw_path = finders.find('core/serviceworker.js')
    with open(sw_path, 'r') as f:
        content = f.read()

    response = HttpResponse(content, content_type='application/javascript')
    response['Service-Worker-Allowed'] = '/'
    return response
