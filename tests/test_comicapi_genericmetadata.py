import unittest
from metrontagger.comicapi.genericmetadata import GenericMetadata


class TestGenericMetadata(unittest.TestCase):
    def setUp(self):
        self.md = GenericMetadata()
        self.md.series = "Aquaman"
        self.md.issue = "0"
        self.md.title = "A Crash of Symbols"

        self.new_md = GenericMetadata()
        self.new_md.year = "1994"
        self.new_md.month = "10"
        self.new_md.day = "1"

    def test_metadata_overlay(self):
        self.md.overlay(self.new_md)

        self.assertEqual(self.md.series, "Aquaman")
        self.assertEqual(self.md.issue, "0")
        self.assertEqual(self.md.title, "A Crash of Symbols")
        self.assertEqual(self.md.year, "1994")
        self.assertEqual(self.md.month, "10")
        self.assertEqual(self.md.day, "1")

    def test_metadata_credits(self):
        result = [
            {"person": "Peter David", "primary": True, "role": "Writer"},
            {"person": "Martin Egeland", "role": "Penciller"},
            {"person": "Martin Egeland", "role": "Cover"},
        ]

        self.md.addCredit("Peter David", "Writer", primary=True)
        self.md.addCredit("Martin Egeland", "Penciller")
        self.md.addCredit("Martin Egeland", "Cover")

        self.assertEqual(self.md.credits, result)

    def test_metadata_credits_overlay(self):
        new_credit = [{"person": "Tom McCray", "role": "Colorist"}]
        result = [
            {"person": "Peter David", "role": "Writer"},
            {"person": "Tom McCray", "role": "Colorist"},
        ]

        self.md.addCredit("Peter David", "Writer")
        self.md.overlayCredits(new_credit)

        self.assertEqual(self.md.credits, result)
