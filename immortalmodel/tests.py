from django.test import TestCase
from immortalmodel.models import ImmortalModel


class ImmortalTestCase(TestCase):
    """
    add immortalmodel to INSTALLED_APPS to run the following tests !!!
    """

    class Blashyrkh(ImmortalModel):
        pass

    def test_immortality(self):
        b = self.Blashyrkh()
        b.delete()
        self.assertRaises(self.Blashyrkh.DoesNotExist, self.Blashyrkh.objects.get, pk=b.pk)
        self.Blashyrkh.baseobjects.get(pk=b.pk)

    def test_resuscitate(self):
        b = self.Blashyrkh()
        b.delete()
        self.assertRaises(self.Blashyrkh.DoesNotExist, self.Blashyrkh.objects.get, pk=b.pk)
        b.deleted = False
        b.save()
        self.Blashyrkh.objects.get(pk=b.pk)

    def test_manually_deleted(self):
        b = self.Blashyrkh()
        b.deleted = True
        b.save()
        self.assertRaises(self.Blashyrkh.DoesNotExist, self.Blashyrkh.objects.get, pk=b.pk)
