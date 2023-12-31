# Generated by Django 4.2.3 on 2023-08-07 00:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('success', 'low'), ('info', 'normal'), ('danger', 'high')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
