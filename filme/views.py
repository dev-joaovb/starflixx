from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomePage
from django.views.generic import TemplateView, CreateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def homepage(request):
#     return render(request, 'homepage.html')

class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomePage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarConta')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario estiver logado
            return redirect('filme:homepage_filmes')  #redirecionar para a homepage filmes
        else:
            return super().get(request, *args, **kwargs)

class HomeFilmes(LoginRequiredMixin ,ListView):
    template_name = 'homepage_filmes.html'
    model = Filme
    #object_list

class DetalhesFilme(LoginRequiredMixin ,DetailView):
    template_name = 'detalhesFilme.html'
    model = Filme
    #object

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()

        usuario = request.user
        usuario.filmes_vistos.add(filme)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(LoginRequiredMixin ,ListView):
    template_name = 'pesquisa.html'
    model = Filme
    #object_list

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return  object_list
        else:
            return None

class PaginaPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarPerfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']
    def get_success_url(self):
        return reverse('filme:homepage_filmes')

class CriarConta(FormView):
    template_name = 'criarConta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')