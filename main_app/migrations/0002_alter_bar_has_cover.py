# Generated by Django 4.2 on 2023-04-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='has_cover',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
