# Generated by Django 3.0.3 on 2020-07-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merlindjango', '0025_auto_20200718_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gsmmodels',
            old_name='artigo',
            new_name='publication',
        ),
    ]
