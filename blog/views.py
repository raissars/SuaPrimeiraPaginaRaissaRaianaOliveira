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
    form = BuscaPostForm()
    resultados = None

    if request.method == 'GET' and 'busca' in request.GET:
        termo = request.GET.get('busca')
        print(f"🔎 Buscando por: {termo}")  # <-- ADICIONE ESTA LINHA
        resultados = Post.objects.filter(titulo__icontains=termo)

    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})

