# Generated by Django 3.2.9 on 2022-06-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Course_Number', models.IntegerField(blank=True)),
                ('Instructor', models.CharField(blank=True, max_length=50)),
                ('Duration', models.FloatField(blank=True)),
            ],
        ),
    ]
