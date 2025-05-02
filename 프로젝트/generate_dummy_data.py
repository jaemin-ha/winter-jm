import json
import random
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.core.serializers import serialize
from django.contrib.auth import get_user_model
from challenges.models import ChallengeHost, Challenge, UserChallenge
from pathlib import Path

class Command(BaseCommand):
    help = '외부 JSON 파일을 불러와 챌린지 더미 데이터를 생성합니다.'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # 기본 사용자 및 호스트 생성
        user, _ = User.objects.get_or_create(
            username='dummyuser',
            defaults={'email': 'dummy@example.com', 'password': 'test1234'}
        )

        host, _ = ChallengeHost.objects.get_or_create(
            user=user,
            defaults={'company_name': '더미컴퍼니', 'phone_number': '01012345678'}
        )

        # JSON 파일 불러오기
        json_path = Path('challenges/data/challenge_list.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            challenge_items = json.load(f)

        # Challenge 및 UserChallenge 생성
        for item in challenge_items:
            challenge = Challenge.objects.create(
                challenge_host=host,
                title=item['title'],
                content=item['content'],
                status='예정',
                start_date=timezone.now(),
                end_date=timezone.now() + timedelta(days=30)
            )

            total_exp = random.randint(10000, 80000)
            prev_exp = total_exp + random.randint(5000, 20000)
            progress = round((total_exp / prev_exp) * 100, 2)

            UserChallenge.objects.create(
                user=user,
                challenge=challenge,
                target_expense=Decimal('50000.00'),
                previous_expense=Decimal(str(prev_exp)),
                total_expense=Decimal(str(total_exp)),
                progress=Decimal(str(progress)),
                status='참여중'
            )

        self.stdout.write(self.style.SUCCESS("✅ 외부 JSON 기반 챌린지/참여 더미 데이터 생성 완료"))
