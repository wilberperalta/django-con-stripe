# Generated by Django 3.0.3 on 2020-02-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_carrusel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrusel',
            name='nombreclass',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
