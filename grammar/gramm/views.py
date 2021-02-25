from django.shortcuts import render
from gramm.models import Grammar
from django.views.generic import ListView, DetailView


class GrammarListView(ListView):  # представление в виде списка
    model = Grammar                   # модель для представления


class GrammarDetailView(DetailView):  # детализированное представление модели
    model = Grammar
