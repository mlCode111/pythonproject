# Generated by Django 2.2.4 on 2019-08-22 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_website_acc_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='acc_date',
        ),
    ]