from django.urls import path
from .views import MatriculaListView, MatriculaCreateView

urlpatterns = [
    # Se quiser que a página inicial já seja a lista, deixe o path vazio ''
    path('', MatriculaListView.as_view(), name='matricula_list'),
    path('matricula/nova/', MatriculaCreateView.as_view(), name='matricula_create'),
]