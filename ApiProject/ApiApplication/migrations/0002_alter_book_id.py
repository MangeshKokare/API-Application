# Generated by Django 4.2.2 on 2024-05-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]