# Generated by Django 2.0.2 on 2018-02-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Log Message',
                'verbose_name_plural': 'Log Messages',
            },
        ),
    ]