# Generated by Django 5.1.1 on 2024-09-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('titles', models.IntegerField(blank=True, default=0, null=True)),
                ('top_scorer', models.CharField(max_length=50)),
                ('fifa_code', models.CharField(max_length=3)),
                ('first_cup', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
