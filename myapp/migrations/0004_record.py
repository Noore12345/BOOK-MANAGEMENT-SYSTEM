# Generated by Django 5.0.1 on 2024-02-28 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('issusID', models.IntegerField(primary_key=True, serialize=False)),
                ('issudate', models.DateField()),
                ('returndate', models.DateField()),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book')),
            ],
        ),
    ]
