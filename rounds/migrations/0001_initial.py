# Generated by Django 4.0 on 2022-08-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants', models.JSONField()),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
            ],
        ),
    ]