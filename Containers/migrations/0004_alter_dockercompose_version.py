# Generated by Django 4.1.1 on 2022-09-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Containers', '0003_rename_comandos_dockerfile_command_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockercompose',
            name='version',
            field=models.FloatField(),
        ),
    ]
