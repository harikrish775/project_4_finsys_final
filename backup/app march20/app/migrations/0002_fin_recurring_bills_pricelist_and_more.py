# Generated by Django 4.2.6 on 2024-03-19 11:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fin_recurring_bills',
            name='pricelist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.fin_price_list'),
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 19)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 19)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 19)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 19)),
        ),
    ]
