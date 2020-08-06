from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from django_logger.models import LogRecord, RemoteRequestLog, ActionLog


class LogRecordAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'application', 'origin_server', 'client_ip', 'username', 'logger', 'level', 'message')
    list_filter = ('application', 'origin_server', 'username', 'logger', 'level')
    search_fields = ('application', 'origin_server', 'client_ip', 'username', 'logger', 'level', 'message')

    fieldsets = (
        (
            _('Server details'),
            {
                'fields': (
                    'timestamp',
                    'application',
                    'origin_server'
                )
            }
        ),
        (
            _('Request details'),
            {
                'fields': (
                    'client_ip',
                    'user_pk',
                    'username',
                )
            }
        ),
        (
            _('Logging details'),
            {
                'fields': (
                    'logger',
                    'level',
                    'message'
                )
            }
        ),
        (
            _('Exception details'),
            {
                'fields': (
                    'stack_trace',
                    'debug_page'
                )
            }
        )
    )

    readonly_fields = LogRecord._meta.get_all_field_names()


class RemoteRequestLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'status_code')
    list_filter = ('timestamp', 'status_code')
    search_fields = ('request', 'response', 'status_code')

    readonly_fields = RemoteRequestLog._meta.get_all_field_names()


class ActionLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user_username', 'action', 'object_text')
    list_filter = ('user_username', 'section', 'action')
    search_fields = ('user_username', 'section', 'action', 'object_text')


admin.site.register(LogRecord, LogRecordAdmin)
admin.site.register(RemoteRequestLog, RemoteRequestLogAdmin)
admin.site.register(ActionLog, ActionLogAdmin)
