# Generated by Django 4.2.3 on 2023-08-03 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 8, 3, 23, 52, 26, 108700, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]