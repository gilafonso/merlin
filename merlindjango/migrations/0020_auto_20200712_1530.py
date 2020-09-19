# Generated by Django 3.0.3 on 2020-07-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlindjango', '0019_noticias_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='downloadableFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_versao', models.CharField(max_length=500)),
                ('update_ficheiro', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='noticias',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Notícias'},
        ),
    ]