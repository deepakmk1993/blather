from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Blat

# Create your views here.
# def home(request):
#   return render(request, 'blat/blat.html', {'message': 'Hello World'})

class IndexView(generic.ListView):
  template_name = 'blat/home.html'
  context_object_name = 'blat_list'

  def get_queryset(self):
    return Blat.objects.select_related('created_by').order_by('-created_on')[:10]


class DetailView(generic.DetailView):
  model = Blat
  template_name = 'blat/detail.html'
  context_object_name = 'blat'


class MyView(IndexView):

  def get_queryset(self):
    return Blat.objects.filter(created_by=self.request.user.id).order_by('-created_on')[:10]

  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super(MyView, self).dispatch(*args, **kwargs)

class NewBlatView(generic.edit.CreateView):
  model = Blat
  fields = ['text', 'via']
  success_url = "/My-blats/"
  
  def form_valid(self, form):
    form.instance.created_by = self.request.user
    return super(NewBlatView, self).form_valid(form)

class EditBlatView(generic.edit.UpdateView):
  model = Blat
  fields = ['text', 'via']
  success_url = "/My-blats/"
  
  def get_queryset(self):
    base_qs = super(EditBlatView, self).get_queryset()
    return base_qs.filter(created_by=self.request.user)