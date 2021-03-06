# Generated by Django 3.1 on 2020-12-23 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representative_position', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=300)),
                ('company_logo', models.ImageField(upload_to='companies/logos')),
                ('company_description', models.CharField(max_length=1000)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('employees_number', models.BigIntegerField(blank=True, null=True)),
                ('company_email', models.EmailField(max_length=254)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(max_length=100)),
                ('phone_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=1000)),
                ('job_category', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('expires_on', models.DateTimeField(blank=True, null=True)),
                ('education_level', models.CharField(max_length=100)),
                ('vaccancies', models.IntegerField(blank=True, null=True)),
                ('no_of_applicants', models.IntegerField(blank=True, null=True)),
                ('salary', models.BigIntegerField()),
                ('skills', models.CharField(max_length=300)),
                ('about_job', models.CharField(max_length=800)),
                ('keywords', models.CharField(max_length=300)),
                ('extra_description', models.CharField(blank=True, max_length=500, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.company')),
            ],
        ),
    ]
