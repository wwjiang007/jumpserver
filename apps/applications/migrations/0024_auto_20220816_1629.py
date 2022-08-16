# Generated by Django 3.2.14 on 2022-08-16 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0019_delete_applyapplicationticket'),
        ('authentication', '0012_auto_20220816_1629'),
        ('applications', '0023_auto_20220816_1021'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='account',
            name='app',
        ),
        migrations.RemoveField(
            model_name='account',
            name='systemuser',
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='application',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='historicalaccount',
            name='app',
        ),
        migrations.RemoveField(
            model_name='historicalaccount',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalaccount',
            name='systemuser',
        ),
        migrations.DeleteModel(
            name='ApplicationUser',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='HistoricalAccount',
        ),
    ]
