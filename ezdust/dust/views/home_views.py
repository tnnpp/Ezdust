from django.shortcuts import render
from django.views import generic
from ..models import OutdoorAir, IndoorAir, Health


class HomePageView(generic.ListView):
    """View for the home page displaying data of air quality in each district in bangkok."""
    template_name = 'dust/home_page.html'
    context_object_name: str = 'indoor'

    def get_queryset(self):
        """
        Return all OutdoorAir in bangkok
        """
        all_indoor = IndoorAir.objects.all()
        return all_indoor

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Health'] = Health.objects.all()
        return context

