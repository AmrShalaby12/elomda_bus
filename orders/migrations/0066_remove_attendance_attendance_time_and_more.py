# Generated by Django 5.0.7 on 2024-09-07 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0065_attendance_attendance_time_attendance_departure_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_time',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='departure_time',
        ),
        migrations.AddField(
            model_name='attendance',
            name='departure_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('غياب', 'غياب')], default='غياب', max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('غياب', 'غياب')], default='غياب', max_length=10),
        ),
    ]
