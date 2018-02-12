from django.shortcuts import render
from django.views.generic import TemplateView


class BlogTemplateView(TemplateView):
    template_name = 'about.html'

