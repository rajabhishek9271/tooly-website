# Generated by Django 3.0.6 on 2021-01-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0005_auto_20210110_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='is_accepted',
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]