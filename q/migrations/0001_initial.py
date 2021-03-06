# Generated by Django 4.0.2 on 2022-02-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('desc', models.CharField(max_length=4141)),
            ],
        ),
        migrations.CreateModel(
            name='Login_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Register_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('mname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('rephone', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('reemail', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('repassword', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
