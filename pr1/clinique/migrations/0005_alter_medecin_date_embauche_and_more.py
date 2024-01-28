# Generated by Django 5.0.1 on 2024-01-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinique', '0004_alter_medecin_date_embauche_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='date_embauche',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='date_naissance',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='medecin',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_naissance',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
