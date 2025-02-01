from django.test import TestCase
from .models import FAQ

class FAQTest(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_translation(self):
        faq = FAQ.objects.first()
        self.assertEqual(faq.get_translation("hi"), faq.question_hi)
