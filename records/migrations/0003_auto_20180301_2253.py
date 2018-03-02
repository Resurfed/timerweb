# Generated by Django 2.0 on 2018-03-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20171221_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkpoint',
            old_name='velocity',
            new_name='avg_xy_speed',
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='avg_z_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='enter_xy_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='enter_z_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='exit_xy_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='exit_z_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='avg_xy_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='avg_z_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='enter_xy_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='enter_z_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='exit_xy_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='exit_z_speed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='best_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='completions',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='time',
            name='date_demoted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='type',
            field=models.CharField(choices=[('M', 'Map'), ('B', 'Bonus')], max_length=1),
        ),
    ]