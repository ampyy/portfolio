# Generated by Django 4.0.2 on 2022-02-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0005_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='brief',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
