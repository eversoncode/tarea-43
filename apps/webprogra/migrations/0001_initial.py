# Generated by Django 2.0.6 on 2021-09-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('pk_employee', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('date_bo', models.DateField()),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.CharField(blank=True, max_length=8)),
                ('direcciono', models.TextField()),
            ],
        ),
    ]
