# Generated by Django 2.1.2 on 2018-11-29 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kilogram', '0004_auto_20181130_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_b', models.IntegerField()),
                ('user_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grouping_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='groupa',
            old_name='group',
            new_name='group_a',
        ),
        migrations.RemoveField(
            model_name='groupa',
            name='user',
        ),
        migrations.AddField(
            model_name='groupa',
            name='user_a',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grouping_a', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
