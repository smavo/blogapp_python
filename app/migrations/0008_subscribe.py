# Generated by Django 4.2.3 on 2023-07-29 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_post_created_date_post_modified_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'suscribe',
                'verbose_name_plural': 'suscribes',
            },
        ),
    ]
