# Generated by Django 5.2 on 2025-06-03 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='transactions_type',
            new_name='transaction_type',
        ),
    ]
