# Generated by Django 3.2.4 on 2021-06-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]
