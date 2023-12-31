# Generated by Django 3.2 on 2023-11-15 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=255)),
                ('matricule', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackendApp.car')),
            ],
        ),
    ]
