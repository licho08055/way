from django.shortcuts import  render,reverse


from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Active
from .forms import ActiveForm 




class list_view(ListView):
    template_name = 'bone/list.html'
    model = Active
    
    
class detail_view(DetailView):
    template_name = 'bone/detail.html'
    object_context_name = 'active'
    model = Active
    
    
class create_view(CreateView):
    template_name = 'bone/create.html'
    form_class = ActiveForm
    
    def get_success_url(self):
        return reverse('bone:list')
    
    
class update_view(UpdateView):
    template_name = 'bone/update.html'
    model = Active
    form_class = ActiveForm
    
    def get_success_url(self):
        return reverse('bone:list')
    
class delete_view(DeleteView):
    template_name = 'bone/delete.html'
    model = Active
    object_context_name = 'active'
    
    def get_success_url(self):
        return reverse('bone:list')