# Generated by Django 3.2.5 on 2021-07-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20210710_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
