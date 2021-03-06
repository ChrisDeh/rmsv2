# Generated by Django 2.0.1 on 2018-09-06 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0011_auto_20180510_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rms.Address')),
            ],
            options={
                'permissions': (('view_warehouse', 'Can view warehouse'),),
            },
        ),
        migrations.AddField(
            model_name='instance',
            name='warehouse',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='rms.Warehouse'),
        ),
    ]
