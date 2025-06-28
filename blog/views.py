from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BuscaPostForm
from .models import Post

def home(request):
    return render(request, 'blog/base.html')

def criar_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Novo Autor'})

def criar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Nova Categoria'})

def criar_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog/form.html', {'form': form, 'titulo': 'Novo Post'})

def buscar_post(request):
    resultados = None
    if request.method == 'POST':
        form = BuscaPostForm(request.POST)
        if form.is_valid():
            termo = form.cleaned_data['busca']
            resultados = Post.objects.filter(titulo__icontains=termo)
    else:
        form = BuscaPostForm()
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})
