from django.shortcuts import render
from django.urls import reverse
from .models import Post, PontuacaoQuizz
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from matplotlib import pyplot as plt
import matplotlib
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

matplotlib.use('Agg')


def home_view(request):
    return render(request, 'portfolio/home.html')


def apresentacao_view(request):
    return render(request, 'portfolio/apresentacao.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')


def licenciatura_view(request):
    return render(request, 'portfolio/licenciatura.html')


def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def novo_post_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/new_post.html', context)


def edita_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edit_post.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def pontuacao_quizz(request):
    score = 0
    operatorsList = request.POST.getlist('p1')

    if '--' in operatorsList:
        score -= 1

    if '%=' in operatorsList:
        score += 1

    if '//=' in operatorsList:
        score += 1

    if '++' in operatorsList:
        score -= 1

    if '/=' in operatorsList:
        score += 1

    if request.POST['p2'] == 'typ':
        score += 1

    if request.POST['p3'] == 'Bom_Dia':
        score += 1

    if request.POST['p4'] == 'r1q4':
        score += 1

    if score < 0:
        score = 0

    return score


def quizz(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
    desenha_grafico_resultados(request)
    return render(request, 'portfolio/quizz.html')


def desenha_grafico_resultados(request):
    pontuacoes = PontuacaoQuizz.objects.all()
    pontuacao_sorted = sorted(pontuacoes, key=lambda objeto: objeto.pontuacao, reverse=False)
    listaNomes = []
    listapontuacao = []

    for person in pontuacao_sorted:
        listaNomes.append(person.nome)
        listapontuacao.append(person.pontuacao)

    plt.barh(listaNomes, listapontuacao)
    plt.savefig('portfolio/static/portfolio/images/graf.png', bbox_inches='tight')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })
