# Generated by Django 4.1.5 on 2023-05-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='allergies',
            field=models.TextField(default='None Known', max_length=256),
        ),
    ]
