# Generated by Django 5.0.1 on 2024-01-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0019_rendezvous_date_rdv_rendezvous_heure_rdv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medecin',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]