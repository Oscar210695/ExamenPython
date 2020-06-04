# Generated by Django 3.0.6 on 2020-06-04 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('subInventario', models.CharField(error_messages={'unique': 'Ya existe actualmente esta clave'}, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('pdv', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripción', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('clave', models.CharField(error_messages={'unique': 'Ya existe actualmente esta clave'}, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('total', models.IntegerField(default=0)),
                ('entregada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('folio', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ilusionesAPI.Almacen')),
                ('orden', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='ilusionesAPI.Orden')),
            ],
        ),
        migrations.CreateModel(
            name='ordenCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ilusionesAPI.Almacen')),
                ('estatus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ilusionesAPI.Estatus')),
                ('orden', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='ilusionesAPI.Orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ilusionesAPI.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('imei', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ilusionesAPI.Producto')),
            ],
        ),
    ]
