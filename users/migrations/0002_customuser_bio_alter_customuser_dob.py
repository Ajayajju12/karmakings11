# Generated by Django 4.2.7 on 2023-11-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
