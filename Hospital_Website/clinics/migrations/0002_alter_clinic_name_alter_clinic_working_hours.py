# Generated by Django 5.0.7 on 2024-08-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='working_hours',
            field=models.CharField(choices=[('09:00 - 12:00', '09:00 - 12:00'), ('12:00 - 15:00', '12:00 - 15:00'), ('15:00 - 18:00', '15:00 - 18:00')], max_length=50),
        ),
    ]
