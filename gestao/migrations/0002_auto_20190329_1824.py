# Generated by Django 2.1.7 on 2019-03-29 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computador',
            old_name='nome',
            new_name='linha',
        ),
        migrations.RemoveField(
            model_name='computador',
            name='data_fabricacao',
        ),
    ]
