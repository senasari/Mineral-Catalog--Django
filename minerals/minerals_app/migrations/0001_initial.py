# Generated by Django 2.1.2 on 2018-10-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_filename', models.TextField()),
                ('image_caption', models.TextField()),
                ('category', models.TextField()),
                ('formula', models.TextField()),
                ('strunz_classification', models.TextField()),
                ('color', models.TextField()),
                ('crystal_system', models.TextField()),
                ('unit_cell', models.TextField()),
                ('crystal_symmetry', models.TextField()),
                ('cleavage', models.TextField()),
                ('mohs_scale_hardness', models.TextField()),
                ('luster', models.TextField()),
                ('streak', models.TextField()),
                ('diaphaneity', models.TextField()),
                ('optical_properties', models.TextField()),
                ('refractive_index', models.TextField()),
                ('crystal_habit', models.TextField()),
                ('specific_gravity', models.TextField()),
            ],
        ),
    ]
