# Generated by Django 4.0.4 on 2022-06-06 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('linkedin', models.URLField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=40)),
                ('titulo', models.CharField(max_length=70)),
                ('descricao', models.TextField(max_length=250)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField(blank=True, max_length=400)),
                ('imagem', models.ImageField(blank=True, upload_to='pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ano', models.IntegerField(default=1)),
                ('anoLetivo', models.CharField(blank=True, max_length=10)),
                ('semestre', models.IntegerField(default=1)),
                ('ects', models.IntegerField(default=1)),
                ('rank', models.IntegerField(default=1)),
                ('descricao', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('professor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa')),
            ],
        ),
    ]
