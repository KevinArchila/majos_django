# Generated by Django 5.0.3 on 2024-05-04 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nevera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambio_tempe',
            name='estado',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]