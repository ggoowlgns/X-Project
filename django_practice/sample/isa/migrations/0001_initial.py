# Generated by Django 2.0.5 on 2018-06-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null='pjh')),
                ('passwd', models.CharField(max_length=30, null='0000')),
                ('phone_num', models.IntegerField(default=1, null=0)),
            ],
        ),
    ]
