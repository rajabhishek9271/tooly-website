# Generated by Django 3.1 on 2020-12-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_auto_20201225_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='address',
            new_name='address_line1',
        ),
        migrations.AddField(
            model_name='applicant',
            name='address_line2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
