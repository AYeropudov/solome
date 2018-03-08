# Generated by Django 2.0.2 on 2018-03-08 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20180302_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductToCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('catalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Catalog')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Product')),
            ],
        ),
    ]
