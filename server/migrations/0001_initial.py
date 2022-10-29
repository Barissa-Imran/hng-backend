# Generated by Django 4.1.2 on 2022-10-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=150)),
                ('backend', models.BooleanField(default=True)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
    ]
