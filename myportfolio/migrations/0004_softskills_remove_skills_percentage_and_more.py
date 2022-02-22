# Generated by Django 4.0.2 on 2022-02-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0003_personal_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='skills',
            name='percentage',
        ),
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
