# Generated by Django 3.2.4 on 2021-06-10 07:03

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mto',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.customuser')),
                ('paypal_id', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'MTO',
                'verbose_name_plural': 'MTO',
            },
            bases=('user.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
