# Generated by Django 3.2.3 on 2022-06-12 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20220611_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='languange_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.languangedetails'),
        ),
    ]