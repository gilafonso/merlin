# Generated by Django 3.0.3 on 2020-07-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlindjango', '0022_auto_20200712_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='imagem_noticia',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]