# Generated by Django 3.2.9 on 2021-11-30 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora_nutricional', '0004_auto_20211129_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='email_usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='nombre_usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='password',
            new_name='password_usuario',
        ),
    ]