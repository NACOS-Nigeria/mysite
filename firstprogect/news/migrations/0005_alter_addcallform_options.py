# Generated by Django 3.2.6 on 2021-09-09 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_delete_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addcallform',
            options={'verbose_name': 'Заявка перезвонить', 'verbose_name_plural': 'Заявки перезвонить'},
        ),
    ]
