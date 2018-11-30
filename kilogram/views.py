from django.shortcuts import render,render_to_response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import *
from django.urls import reverse_lazy
from .models import *
from django.template import RequestContext

# Create your views here.

class IndexView(TemplateView):
    template_name='kilogram/index.html'

class CreateUserView(CreateView):
    template_name='registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisterView(TemplateView):
    template_name = 'registration/signup_done.html'

def simple_list(request):
    queryset = User.objects.all()
    queryset1 = GroupA.objects.all()
    table = SimpleTable(queryset)
    table1 =ProfileTable(queryset1)

    getuser=User.models.get(id=1)
    userfiltered = User.objects.select_related()
    table2 = Related(userfiltered)

    context = {
        'table':table,
        'table1':table1,
        'table2': table2
    }
    return render(request, "kilogram/simple_list.html",context)