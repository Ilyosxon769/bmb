# Generated by Django 4.0.4 on 2022-06-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_importexcel_fexcel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importexcel',
            name='fexcel',
            field=models.FileField(upload_to='excel/%Y/%m/%d'),
        ),
    ]
