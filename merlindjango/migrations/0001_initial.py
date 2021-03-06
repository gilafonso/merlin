# Generated by Django 3.0.3 on 2020-03-30 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('subtitulo', models.CharField(max_length=250)),
                ('subtitulo_2', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='descricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_principal', models.CharField(max_length=250)),
                ('titulo_secundario', models.CharField(max_length=250)),
                ('imagem', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='downloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('subtitulo', models.CharField(max_length=500)),
                ('imagem_noticia', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('imagem', models.FileField(upload_to='')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_noticia', models.CharField(max_length=500)),
                ('imagem_noticia', models.FileField(upload_to='')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacao', models.CharField(max_length=250)),
                ('nome', models.CharField(max_length=250)),
                ('imagem_dev', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('subtitulo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='todas_noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ficheiro', models.CharField(max_length=10)),
                ('sub_titulo', models.CharField(max_length=250)),
                ('noticias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merlindjango.Noticias')),
            ],
        ),
        migrations.CreateModel(
            name='link_imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('ficheiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merlindjango.tutorial')),
            ],
        ),
        migrations.CreateModel(
            name='link_download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('ficheiro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merlindjango.downloads')),
            ],
        ),
    ]
