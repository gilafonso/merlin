# Generated by Django 3.0.3 on 2020-07-12 13:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('merlindjango', '0018_remove_noticias_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
