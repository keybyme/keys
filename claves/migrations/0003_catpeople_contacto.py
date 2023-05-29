# Generated by Django 4.2.1 on 2023-05-29 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('claves', '0002_alter_item_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catpeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catp', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'catpeople',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('catpeople', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='claves.catpeople')),
            ],
            options={
                'db_table': 'contacto',
            },
        ),
    ]
