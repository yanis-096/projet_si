# Generated by Django 5.0.1 on 2024-01-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0003_alter_medecin_date_naissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='date_embauche',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_naissance',
            field=models.DateField(default='2020-01-01'),
        ),
    ]
