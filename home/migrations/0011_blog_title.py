# Generated by Django 3.1.6 on 2021-02-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
