"""
Test custom management commands

"""
from django.test import SimpleTestCase
from unittest.mock import patch
from psycopg2 import OperationalError as psycopg2Error
from django.db.utils import OperationalError
from django.core.management import call_command

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """ Test Commands """
    def test_wait_for_db_ready(self,patched_check):
        """ Test waiting for DB if it's already ready """
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])
