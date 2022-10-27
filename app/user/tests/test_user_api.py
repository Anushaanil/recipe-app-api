"""
Tests for the user API.
"""
import sys
sys.path.append("..")
from core.models import User # noqa

from django.test import TestCase # noqa
from django.urls import reverse # noqa

from rest_framework.test import APIClient # noqa
