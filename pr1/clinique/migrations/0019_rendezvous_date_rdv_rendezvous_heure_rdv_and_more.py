# Generated by Django 5.0.1 on 2024-01-28 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0018_remove_rendezvous_date_remove_rendezvous_heure_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='date_rdv',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='heure_rdv',
            field=models.TimeField(default='08:00'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='medecin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinique.medecin'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinique.patient'),
        ),
    ]
