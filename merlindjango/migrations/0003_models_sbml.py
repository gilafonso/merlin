# Generated by Django 3.0.3 on 2020-06-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlindjango', '0002_auto_20200626_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='sbml',
            field=models.FileField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
