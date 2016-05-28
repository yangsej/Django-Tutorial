import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() 는 pub_date가 미래인 질문에 대해서
Fasle를 반환해야 합니다."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertEqual(future_question.was_published_recently(), False)
