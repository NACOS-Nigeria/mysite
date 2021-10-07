# Generated by Django 3.2.6 on 2021-09-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Person', models.CharField(max_length=45, verbose_name='Имя')),
                ('Number', models.IntegerField()),
                ('text', models.TextField(verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'ОТЗЫВ! ',
                'verbose_name_plural': 'ОТЗЫВЫ!',
            },
        ),
    ]
