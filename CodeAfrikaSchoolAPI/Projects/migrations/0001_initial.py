# Generated by Django 3.2.13 on 2022-04-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('language', models.PositiveSmallIntegerField(choices=[(1, 'python'), (2, 'java'), (3, 'javascript'), (4, 'rust'), (5, 'golang'), (6, 'c_plusplus'), (8, 'solidity')], default=1)),
            ],
        ),
    ]
