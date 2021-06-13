# Generated by Django 3.2.4 on 2021-06-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MicroTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='JO Name', max_length=100)),
                ('target_date', models.DateField()),
                ('description', models.TextField(help_text='Job Description')),
                ('sample', models.FileField(default='samples/default.pdf', help_text='upload Job Sample', upload_to='samples/%Y/%m/')),
                ('instructions', models.FileField(default='samples/default.pdf', help_text='Upload Job Instructions', upload_to='samples/%Y/%m/')),
                ('quantity', models.IntegerField(help_text='Quantity of the Job')),
                ('people_required', models.IntegerField(help_text='Number of people required ')),
                ('skills', models.TextField()),
                ('cost', models.IntegerField(help_text='Job Cost in AED')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
