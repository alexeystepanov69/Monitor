# Generated by Django 2.2.3 on 2019-07-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0026_auto_20190705_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='main_channel',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Канал'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='xbee_mac',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='MAC модема'),
        ),
    ]
