# Generated by Django 3.2.9 on 2021-11-30 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora_nutricional', '0005_auto_20211130_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='email_usuario',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='password_usuario',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre_usuario',
            new_name='user_name',
        ),
    ]