# Generated by Django 5.0.1 on 2024-01-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0013_alter_medecin_adresse_cabinet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='date_embauche',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='date_naissance',
           field=models.DateField(default='2020-01-01'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_naissance',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]