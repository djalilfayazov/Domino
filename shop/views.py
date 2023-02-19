from django.shortcuts import render
from .models import *

from django.db.models import Q
from django.views.generic import TemplateView
from django.views.generic.list import ListView



def home(request):
	return render(request, 'base.html')


class SearchResultsView(ListView):
    #model = Products
    template_name = 'shop/search.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        #object_list = Products.objects.filter(Q(key__icontains=query))
        #return object_list