# Generated by Django 5.0.1 on 2024-02-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_book_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.IntegerField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=220)),
                ('mobile', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('branch', models.CharField(max_length=30)),
            ],
        ),
    ]
