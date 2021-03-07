from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from django_logger.models import RemoteRequestLog


class RemoteRequestLogModelTests(TestCase):

    def test_create_and_retrieve_remote_request_log(self):
        logrecord = RemoteRequestLog.objects.create(
            request="Mobile"
        )

        retrieve_logrecord = RemoteRequestLog.objects.get(request="Mobile")

        self.assertEqual(logrecord, retrieve_logrecord)

    def test_create_and_retrieve_two_remote_request_log(self):
        RemoteRequestLog.objects.create(
            request="Mobile"
        )

        RemoteRequestLog.objects.create(
            request="Desktop"
        )

        retrieve_logrecords = RemoteRequestLog.objects.all()

        self.assertEqual(2, retrieve_logrecords.count())

    def test_delete_remote_request_log(self):
        RemoteRequestLog.objects.create(
            request="Mobile"
        )

        retrieve_logrecord = RemoteRequestLog.objects.get(request="Mobile").delete()

        self.assertTrue(retrieve_logrecord)

    def test_delete_notexist_remote_request_log(self):
        RemoteRequestLog.objects.create(
            request="Mobile"
        )
        with self.assertRaisesMessage(ObjectDoesNotExist, "RemoteRequestLog matching query does not exist."):
            RemoteRequestLog.objects.get(request="Desktop").delete()
