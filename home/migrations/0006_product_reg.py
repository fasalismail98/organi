# Generated by Django 3.1.6 on 2021-02-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_product_addedby'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('image', models.ImageField(upload_to='product_img/')),
            ],
        ),
    ]
