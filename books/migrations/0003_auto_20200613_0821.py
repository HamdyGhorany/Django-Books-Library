# Generated by Django 3.0.6 on 2020-06-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200612_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='sites',
            field=models.IntegerField(blank=True),
        ),
    ]
