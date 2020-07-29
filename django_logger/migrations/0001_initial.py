# Generated by Django 3.0.8 on 2020-07-29 11:31

import _socket
from django.db import migrations, models
import django_logger.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True, default=django_logger.models.now)),
                ('user_pk', models.IntegerField(db_index=True, help_text='The primary key of the user making the request in which this record was logged.')),
                ('user_username', models.CharField(db_index=True, help_text='The username of the user making the request in which this record was logged.', max_length=255)),
                ('user_detail', models.TextField(null=True)),
                ('section', models.CharField(choices=[('console', 'Console'), ('login_screen', 'Console'), ('admin_screen', 'Admin')], db_index=True, help_text='The Backend/APP section in which this record was logged.', max_length=255)),
                ('action', models.CharField(choices=[('log_in', 'Log In'), ('log_out', 'Log Out'), ('change_password', 'Change Password'), ('user_update', 'User Update'), ('user_moderate', 'User Delete')], db_index=True, help_text='The Backend/APP action in which this record was logged.', max_length=255)),
                ('object_pk', models.IntegerField(db_index=True, help_text='The primary key of the object in which this record was logged.', null=True)),
                ('object_text', models.CharField(db_index=True, help_text='The name or definition of the object in which this record was logged.', max_length=255, null=True)),
                ('object_detail', models.TextField(null=True)),
                ('value_previous', models.TextField(help_text='The previous value when this record was logged.', null=True)),
                ('value_current', models.TextField(help_text='The current value when this record was logged.', null=True)),
            ],
            options={
                'ordering': ('-timestamp',),
                'permissions': (('view_logs', 'Can view log records'),),
            },
        ),
        migrations.CreateModel(
            name='LogRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(db_index=True, default=django_logger.models.now)),
                ('application', models.CharField(db_index=True, default='django_dev', help_text='The application logging this record.', max_length=256)),
                ('origin_server', models.CharField(db_index=True, default=_socket.gethostname, help_text='The server logging this record.', max_length=256)),
                ('client_ip', models.CharField(blank=True, db_index=True, help_text='The IP address of the client making the request.', max_length=128)),
                ('user_pk', models.IntegerField(blank=True, db_index=True, help_text='The primary key of the user making the request in which this record was logged.', null=True)),
                ('username', models.CharField(blank=True, db_index=True, help_text='The username of the user making the request in which this record was logged.', max_length=256)),
                ('uuid', models.CharField(blank=True, db_index=True, help_text='The UUID of the Django request in which this record was logged.', max_length=256)),
                ('logger', models.CharField(db_index=True, help_text='The name of the logger of the record.', max_length=1024)),
                ('level', models.CharField(db_index=True, help_text='The level of the log record (DEBUG, INFO...)', max_length=32)),
                ('message', models.TextField()),
                ('stack_trace', models.TextField(blank=True)),
                ('debug_page', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('-timestamp',),
                'permissions': (('view_logs', 'Can view log records'),),
            },
        ),
        migrations.CreateModel(
            name='RemoteRequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField()),
                ('response', models.TextField(null=True)),
                ('status_code', models.IntegerField(default=200)),
                ('timestamp', models.DateTimeField(db_index=True, default=django_logger.models.now)),
                ('uuid', models.CharField(blank=True, db_index=True, help_text='The UUID of the Django request in which this record was logged.', max_length=256)),
                ('user_agent', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ('-timestamp',),
                'permissions': (('views_logs', 'Can view log records'),),
            },
        ),
    ]
