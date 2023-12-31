# Generated by Django 4.2.3 on 2023-07-28 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'tags',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'posts', 'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='post', to='app.tag'),
        ),
    ]
