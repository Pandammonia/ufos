# Generated by Django 4.0.5 on 2022-06-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Details', models.TextField()),
                ('Name', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
