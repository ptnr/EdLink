# Generated by Django 3.0.3 on 2020-03-02 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200302_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]