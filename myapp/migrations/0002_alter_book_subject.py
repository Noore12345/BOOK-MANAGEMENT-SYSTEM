# Generated by Django 5.0.1 on 2024-02-25 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.CharField(max_length=20),
        ),
    ]
