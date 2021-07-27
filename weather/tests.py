from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import Report


# Create your tests here.
class TestReportModel(TestCase):

  def make_valid_report(self):
    valid_report_params = {
        "city": "Arlington",
        "state": "VA",
        "zipcode": "22201",
        "temperature": 70.07,
        "weather": Report.Weather.SUNNY,
      }
    
    return Report.objects.create(**valid_report_params)

  def test_report_date_now_when_blank(self):
    """
    Creating a new report with a blank report_date field should set the time to now
    """
    valid_report = self.make_valid_report()

    report_date = valid_report.report_date
    now = timezone.now()
    difference = (now-report_date).seconds

    self.assertEqual(difference, 0)

  def test_reject_long_city(self):
    """
    Reporting with a city title length > 50 rejects the input
    """
    
    valid_report = self.make_valid_report()

    valid_report.city = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    self.assertRaises(ValidationError, valid_report.full_clean)

  def test_reject_long_state(self):
    """
    Reporting with a city title length > 50 rejects the input
    """
    
    valid_report = self.make_valid_report()

    valid_report.state = "XYZ"
    self.assertRaises(ValidationError, valid_report.full_clean)

  def test_reject_long_zipcode(self):
    """
    Reporting with a city title length > 50 rejects the input
    """
    
    valid_report = self.make_valid_report()

    valid_report.zipcode = "000001"
    self.assertRaises(ValidationError, valid_report.full_clean)

  def test_reject_short_zipcode(self):
    """
    Reporting with a city title length > 50 rejects the input
    """
    
    valid_report = self.make_valid_report()

    valid_report.zipcode = "0000"
    self.assertRaises(ValidationError, valid_report.full_clean)
