# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 17:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(help_text='Address 1', max_length=128)),
                ('address_2', models.CharField(blank=True, help_text='Address 2', max_length=255)),
                ('city', models.CharField(help_text='City', max_length=60)),
                ('state', models.CharField(choices=[('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('TG', 'Telangana'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chattisgarh'), ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Orissa'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'), ('UA', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Pondicherry')], help_text='State', max_length=30)),
                ('country', django_countries.fields.CountryField(help_text='Country', max_length=2)),
                ('zip_code', models.CharField(help_text='Zip Code', max_length=6, validators=[django.core.validators.RegexValidator(message='Only digits allowed.', regex='^[0-9]*$')])),
                ('raw', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Center Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=50)),
                ('last_name', models.CharField(help_text='Last Name', max_length=50)),
                ('date_of_birth', models.DateField(help_text='Date Of Birth')),
                ('mobile', models.CharField(help_text='Mobile Number. Add +91 prefix', max_length=15, validators=[django.core.validators.RegexValidator(message="Mobile Number must be entered in the format:                    '+999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=6)),
                ('other_center', models.CharField(blank=True, help_text='Center name if not available above', max_length=50)),
                ('father_name', models.CharField(help_text="Father's Name", max_length=50)),
                ('father_mobile', models.CharField(help_text="Father's Mobile Number. Add +91 prefix", max_length=15, validators=[django.core.validators.RegexValidator(message="Mobile Number must be entered in the format:                    '+999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, help_text='Email', max_length=254)),
                ('mother_name', models.CharField(blank=True, help_text="Mother's Name", max_length=50)),
                ('mother_mobile', models.CharField(blank=True, help_text="Mother's Mobile Number. Add +91 prefix", max_length=15, validators=[django.core.validators.RegexValidator(message="Mobile Number must be entered in the format:                    '+999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('center', models.ForeignKey(help_text='Center', on_delete=django.db.models.deletion.CASCADE, to='base.Center')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Female'), ('female', 'Male')], default='female', max_length=6)),
                ('mobile', models.CharField(blank=True, help_text='Mobile Number. Add +91 prefix', max_length=15, validators=[django.core.validators.RegexValidator(message="Mobile Number must be entered in the format:                    '+999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('min_age', models.CharField(help_text='Age Group lower limit', max_length=2, validators=[django.core.validators.RegexValidator(message='Only digits allowed.', regex='^[0-9]*$')])),
                ('max_age', models.CharField(help_text='Age Group Upper limit', max_length=2, validators=[django.core.validators.RegexValidator(message='Only digits allowed.', regex='^[0-9]*$')])),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Center')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]