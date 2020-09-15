# Generated by Django 3.0.4 on 2020-09-15 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDO', '0002_task_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Era',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='era',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ToDO.Era'),
        ),
    ]
