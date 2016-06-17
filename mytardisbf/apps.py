import logging
from django.apps import AppConfig
from tardis.tardis_portal.models import Schema

logger = logging.getLogger(__name__)


# change to your own schema name
ROBTEST_SCHEMA = "http://tardis.edu.au/schemas/robtest/1"


class RobTestConfig(AppConfig):
    name = 'robtest'
    verbose_name = "MyTardis RobTest"

    def ready(self):
        if not Schema.objects.filter(namespace__exact=ROBTEST_SCHEMA):
            from django.core.management import call_command
            call_command('loaddata', 'robtest')

