# Generated by Django 4.2 on 2024-01-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0002_rename_invent_goods_alter_goods_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '货品', 'verbose_name_plural': '货品'},
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_text',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
