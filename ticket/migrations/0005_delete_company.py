# Generated by Django 5.1.6 on 2025-02-14 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_company_alter_companyregistration_vehicle_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]
