# Generated by Django 2.0.5 on 2018-06-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isa', '0004_auto_20180606_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='job',
            field=models.CharField(max_length=20, null='학생'),
        ),
    ]