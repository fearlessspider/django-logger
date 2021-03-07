from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from django_logger.models import LogRecord


class LogRecordModelTests(TestCase):

    def test_create_and_retrieve_logrecord(self):
        logrecord = LogRecord.objects.create(
            application="Mobile"
        )

        retrieve_logrecord = LogRecord.objects.get(application="Mobile")

        self.assertEqual(logrecord, retrieve_logrecord)

    def test_create_and_retrieve_two_logrecord(self):
        LogRecord.objects.create(
            application="Mobile"
        )

        LogRecord.objects.create(
            application="Desktop"
        )

        retrieve_logrecords = LogRecord.objects.all()

        self.assertEqual(2, retrieve_logrecords.count())

    def test_delete_logrecord(self):
        LogRecord.objects.create(
            application="Mobile"
        )

        retrieve_logrecord = LogRecord.objects.get(application="Mobile").delete()

        self.assertTrue(retrieve_logrecord)

    def test_delete_notexist_logrecord(self):
        LogRecord.objects.create(
            application="Mobile"
        )
        with self.assertRaisesMessage(ObjectDoesNotExist, "LogRecord matching query does not exist."):
            LogRecord.objects.get(application="Desktop").delete()
