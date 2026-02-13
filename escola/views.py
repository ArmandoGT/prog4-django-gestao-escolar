from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Matricula
from .forms import MatriculaForm


# Listar as matrículas realizadas
class MatriculaListView(ListView):
    model = Matricula
    template_name = 'escola/matricula_list.html'
    context_object_name = 'matriculas'


# Criar nova matrícula (Gerenciar o processo)
class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'escola/matricula_form.html'
    success_url = reverse_lazy('matricula_list')  # Redireciona para a lista após sucesso

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Nova Matrícula'
        return context