# Generated by Django 5.0.7 on 2024-09-07 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0061_alter_attendance_attendance_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_status',
        ),
        migrations.AddField(
            model_name='attendance',
            name='arrival_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('انصراف', 'انصراف'), ('غياب', 'غياب')], default='غياب', max_length=10, verbose_name='Arrival Status'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='departure_status',
            field=models.CharField(choices=[('حضور', 'حضور'), ('انصراف', 'انصراف'), ('غياب', 'غياب')], default='غياب', max_length=10, verbose_name='Departure Status'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
