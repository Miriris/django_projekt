# Generated by Django 4.0.3 on 2022-04-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='office_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
