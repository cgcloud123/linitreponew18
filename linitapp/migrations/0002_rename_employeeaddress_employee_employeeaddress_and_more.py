# Generated by Django 4.1.1 on 2022-10-03 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linitapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Employeeaddress',
            new_name='employeeaddress',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employeeemail',
            new_name='employeeemail',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employeename',
            new_name='employeename',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Employeenumber',
            new_name='employeenumber',
        ),
    ]
