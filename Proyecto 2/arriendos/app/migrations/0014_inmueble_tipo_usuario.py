# Generated by Django 4.2 on 2024-06-10 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_inmueble_usuario_inmueble_id_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='tipo_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inmuebles', to='app.tipo_usuario'),
            preserve_default=False,
        ),
    ]