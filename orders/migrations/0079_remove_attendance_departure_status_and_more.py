# Generated by Django 5.0.7 on 2024-09-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0078_alter_attendance_attendance_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='departure_status',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('انصراف', 'انصراف'), ('غياب', 'غياب')], default='حضور', max_length=10),
        ),
    ]
