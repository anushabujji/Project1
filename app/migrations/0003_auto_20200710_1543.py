# Generated by Django 2.0.3 on 2020-07-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200710_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]