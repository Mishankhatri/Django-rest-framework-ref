# Generated by Django 4.0 on 2022-01-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
