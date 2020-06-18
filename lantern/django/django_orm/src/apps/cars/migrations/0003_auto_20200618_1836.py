# Generated by Django 3.0.6 on 2020-06-18 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0003_auto_20200618_1836'),
        ('cars', '0002_populate_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dealers.Dealer'),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('car', models.ManyToManyField(to='cars.Car')),
            ],
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['name'], name='cars_proper_name_9c9042_idx'),
        ),
    ]