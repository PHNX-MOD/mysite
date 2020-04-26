from django.test import TestCase

class PageTests(TestCase):

    def test_about_page(self):
        response = self.client.get("/about/")
        self.assertContains(response, "this is the about page")
