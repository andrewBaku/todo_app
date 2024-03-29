# Generated by Django 4.2.2 on 2023-06-29 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_subtask_created_date_subtask_task_subtask_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='categ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.category'),
        ),
    ]
