# Generated by Django 3.1.5 on 2021-01-14 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210107_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zipcode',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
