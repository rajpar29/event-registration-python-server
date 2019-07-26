# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 17:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Event Name', max_length=50)),
                ('start_date', models.DateField(help_text='Event Start Date')),
                ('end_date', models.DateField(help_text='Event End Date')),
                ('last_date_of_registration', models.DateField(help_text='Last Date of Registration')),
                ('fees', models.DecimalField(decimal_places=2, help_text='Event Fees', max_digits=10)),
                ('late_fees', models.DecimalField(decimal_places=2, help_text='Late Registration Fees', max_digits=10)),
                ('accommodation_provided', models.BooleanField(help_text='Is Accommodation Provided?')),
                ('event_code', models.CharField(help_text='Event Code', max_length=20, unique=True)),
                ('min_age', models.CharField(help_text='Age Group Lower limit', max_length=2, validators=[django.core.validators.RegexValidator(message='Only digits allowed.', regex='^[0-9]*$')])),
                ('max_age', models.CharField(help_text='Age Group Upper limit', max_length=2, validators=[django.core.validators.RegexValidator(message='Only digits allowed.', regex='^[0-9]*$')])),
                ('rules', models.TextField(blank=True, help_text='Any Rules')),
                ('remarks', models.TextField(blank=True, help_text='Any Remarks')),
                ('center', models.ForeignKey(help_text='Center', on_delete=django.db.models.deletion.CASCADE, related_name='center', to='base.Center')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Address')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(help_text='Registration Number', max_length=20, unique=True)),
                ('accommodation', models.BooleanField(help_text='Is Accommodation Required?')),
                ('payment_status', models.BooleanField(help_text='Has paid?')),
                ('amount_paid', models.DecimalField(decimal_places=2, help_text='Amount Paid', max_digits=10)),
                ('cashier', models.CharField(blank=True, help_text='Cashier', max_length=50)),
                ('big_buddy', models.CharField(blank=True, help_text='Big Buddy', max_length=50)),
                ('goal_achievement', models.CharField(blank=True, help_text='Goal Achievement', max_length=100)),
                ('role', models.CharField(choices=[('participant', 'Participant'), ('helper', 'Helper'), ('coordinator', 'Coordinator')], help_text='Role', max_length=12)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('event_center', models.ForeignKey(blank=True, help_text='Event Center', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_center', to='base.Center')),
                ('home_center', models.ForeignKey(help_text='Home Center', on_delete=django.db.models.deletion.CASCADE, related_name='home_center', to='base.Center')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Participant')),
            ],
        ),
    ]