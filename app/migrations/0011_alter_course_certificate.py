# Generated by Django 4.0.4 on 2022-07-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_course_certificate_course_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Certificate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
