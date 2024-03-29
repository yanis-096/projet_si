# Generated by Django 5.0.1 on 2024-01-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0012_medecin_adresse_cabinet_medecin_date_embauche_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='adresse_cabinet',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
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
            name='adresse',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_naissance',
            field=models.DateField(default='2020-01-01'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, default='example@example.com', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tele',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
