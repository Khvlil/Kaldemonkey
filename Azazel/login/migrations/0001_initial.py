# Generated by Django 4.0 on 2021-12-31 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('repassword', models.CharField(max_length=30)),
            ],
        ),
    ]
