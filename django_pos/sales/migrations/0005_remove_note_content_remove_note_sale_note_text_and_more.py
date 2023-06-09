# Generated by Django 4.1.5 on 2023-06-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_remove_sale_note_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='content',
        ),
        migrations.RemoveField(
            model_name='note',
            name='sale',
        ),
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='note',
            table=None,
        ),
    ]
