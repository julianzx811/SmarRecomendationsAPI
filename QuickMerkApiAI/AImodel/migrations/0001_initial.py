# Generated by Django 4.2.5 on 2023-09-27 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('EmpresaId', models.AutoField(primary_key=True, serialize=False)),
                ('Empresa_Nombre', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_categoria',
            fields=[
                ('CategoriaID', models.AutoField(primary_key=True, serialize=False)),
                ('Categoria', models.CharField(max_length=255)),
                ('icono', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('TiendaId', models.AutoField(primary_key=True, serialize=False)),
                ('Tienda_Nombre', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('latitudeDelta', models.FloatField()),
                ('longitudeDelta', models.FloatField()),
                ('empresaId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AImodel.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_info',
            fields=[
                ('ProductInfoId', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.CharField(max_length=255)),
                ('Disponibilidad', models.CharField(max_length=255)),
                ('Imagen', models.CharField(max_length=255)),
                ('Descripcion', models.CharField(max_length=4000)),
                ('link', models.CharField(max_length=4000, null=True)),
                ('categoria', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='AImodel.producto_categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=255)),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AImodel.producto_info')),
                ('tiendaId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='AImodel.tienda')),
            ],
        ),
    ]
