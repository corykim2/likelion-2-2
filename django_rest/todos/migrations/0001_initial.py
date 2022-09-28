# Generated by Django 4.1.1 on 2022-09-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]