# Generated by Django 4.0.1 on 2022-02-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_alter_tasks_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
