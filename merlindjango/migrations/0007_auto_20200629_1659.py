# Generated by Django 3.0.3 on 2020-06-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlindjango', '0006_auto_20200629_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='models',
            name='id',
        ),
        migrations.AlterField(
            model_name='models',
            name='id_modelo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
