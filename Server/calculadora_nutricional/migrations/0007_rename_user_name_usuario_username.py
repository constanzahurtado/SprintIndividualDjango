# Generated by Django 3.2.9 on 2021-11-30 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora_nutricional', '0006_auto_20211130_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='user_name',
            new_name='username',
        ),
    ]
