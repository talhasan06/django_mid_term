# Generated by Django 4.2.7 on 2023-12-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_task_assign_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_assign_date',
            field=models.DateTimeField(),
        ),
    ]