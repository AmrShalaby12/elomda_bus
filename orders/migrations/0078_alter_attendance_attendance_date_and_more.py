# Generated by Django 5.0.7 on 2024-09-07 13:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0077_alter_attendance_attendance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('انصراف', 'انصراف'), ('غياب', 'غياب')], default='غياب', max_length=10, verbose_name='حالة الحضور'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='departure_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('انصراف', 'انصراف'), ('غياب', 'غياب')], default='غياب', max_length=10, verbose_name='حالة الانصراف'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
    ]
