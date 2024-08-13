from django.views.generic import ListView
from .models import Aluno

class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno_list.html'
    context_object_name = 'alunos'
