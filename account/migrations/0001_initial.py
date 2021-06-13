# Generated by Django 3.2.4 on 2021-06-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MTOPaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='eg paid, pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.IntegerField(help_text='micro tasks Id')),
                ('mto', models.IntegerField(help_text='Assigned to MTO')),
                ('payment', models.IntegerField()),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('fees', models.FloatField()),
            ],
        ),
    ]