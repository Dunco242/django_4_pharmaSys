# Generated by Django 4.1.5 on 2023-06-05 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_sale_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='note',
        ),
        migrations.AddField(
            model_name='sale',
            name='allergies',
            field=models.TextField(blank=True, max_length=1056),
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]