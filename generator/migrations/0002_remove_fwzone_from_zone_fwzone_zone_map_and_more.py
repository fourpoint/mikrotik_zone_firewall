# Generated by Django 4.2.3 on 2023-07-20 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fwzone',
            name='from_zone',
        ),
        migrations.AddField(
            model_name='fwzone',
            name='zone_map',
            field=models.ManyToManyField(through='generator.FWZoneMap', to='generator.fwzone'),
        ),
        migrations.AddField(
            model_name='fwzonemap',
            name='to_zone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dst_zone', to='generator.fwzone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fwzonemap',
            name='from_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_zone', to='generator.fwzone'),
        ),
    ]
