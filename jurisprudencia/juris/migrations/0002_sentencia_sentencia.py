# Generated by Django 2.0.6 on 2018-06-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juris', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentencia',
            name='sentencia',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]