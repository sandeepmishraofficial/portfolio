from django.urls import path
from . import views

app_name = 'resume_toolkit'

urlpatterns = [
    path('',           views.index,     name='index'),
    path('analyze/',   views.analyze,   name='analyze'),
    path('ats-score/', views.ats_score, name='ats_score'),
    path('editor/',    views.editor,    name='editor'),
    path('converter/', views.converter, name='converter'),
]
