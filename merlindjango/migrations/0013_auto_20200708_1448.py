# Generated by Django 3.0.3 on 2020-07-08 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merlindjango', '0012_auto_20200701_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gsmmodels',
            options={'verbose_name_plural': 'GSMModels'},
        ),
        migrations.AlterModelOptions(
            name='noticias',
            options={'verbose_name_plural': 'Notícias'},
        ),
        migrations.AlterField(
            model_name='gsmmodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
