# Generated by Django 3.0.3 on 2020-06-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlindjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_modelo', models.IntegerField()),
                ('nome', models.CharField(max_length=500)),
                ('organismo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=500)),
                ('artigo', models.TextField()),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='about',
        ),
        migrations.DeleteModel(
            name='descricao',
        ),
        migrations.DeleteModel(
            name='home',
        ),
        migrations.RemoveField(
            model_name='link_download',
            name='ficheiro',
        ),
        migrations.RemoveField(
            model_name='link_imagem',
            name='ficheiro',
        ),
        migrations.DeleteModel(
            name='team',
        ),
        migrations.RemoveField(
            model_name='todas_noticias',
            name='noticias',
        ),
        migrations.AddField(
            model_name='noticias',
            name='autor',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='downloads',
        ),
        migrations.DeleteModel(
            name='link_download',
        ),
        migrations.DeleteModel(
            name='link_imagem',
        ),
        migrations.DeleteModel(
            name='todas_noticias',
        ),
        migrations.DeleteModel(
            name='tutorial',
        ),
    ]