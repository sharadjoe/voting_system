# Generated by Django 2.0.3 on 2018-03-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=1000)),
                ('OId', models.CharField(max_length=1000)),
                ('LTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Image', models.CharField(max_length=10000)),
                ('Bot', models.CharField(max_length=10000)),
                ('Members', models.CharField(max_length=1000)),
                ('Desc', models.TextField()),
                ('Backers', models.ManyToManyField(to='poll.Backer')),
            ],
        ),
    ]
