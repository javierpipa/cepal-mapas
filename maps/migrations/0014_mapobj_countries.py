# Generated by Django 2.0.9 on 2018-11-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0013_mapobj_image_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapobj',
            name='countries',
            field=models.ManyToManyField(blank=True, to='maps.WorldBorder'),
        ),
    ]
