# Generated by Django 4.2.5 on 2023-12-28 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]