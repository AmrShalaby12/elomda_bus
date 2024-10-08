# Generated by Django 5.0.7 on 2024-09-07 04:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0064_alter_attendance_attendance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attendance_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('انصراف', 'انصراف')], default='حضور', max_length=10),
        ),
    ]
