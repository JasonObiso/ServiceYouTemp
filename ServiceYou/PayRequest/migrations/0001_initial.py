# Generated by Django 4.2.6 on 2023-10-12 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='PayRequest.user')),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(blank=True, max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
            bases=('PayRequest.user',),
        ),
    ]
