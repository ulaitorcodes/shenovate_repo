# Generated by Django 3.0.5 on 2021-06-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('area_of_interest', models.CharField(max_length=50)),
                ('hdyhau', models.CharField(max_length=50)),
                ('why', models.CharField(max_length=50)),
            ],
        ),
    ]
