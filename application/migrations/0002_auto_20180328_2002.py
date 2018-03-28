# Generated by Django 2.0.1 on 2018-03-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='date_founded',
            new_name='date_opened',
        ),
        migrations.AddField(
            model_name='space',
            name='date_closed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='space',
            name='membership',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='space',
            name='operational_status',
            field=models.CharField(choices=[('OP', 'In Operation'), ('PL', 'Planned'), ('CL', 'Closed'), ('UK', 'Unknown Operation Status')], default='UK', max_length=2),
        ),
        migrations.AddField(
            model_name='space',
            name='size_in_sq_meters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='space',
            name='users',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='space',
            name='wheelchair_accessibility',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='space',
            name='phone',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
