# from celery import shared_task
# from django.utils import timezone
# from .models import UserTariffSubscription, Ad
#
# @shared_task
# def check_tariff_expiry():
#     now = timezone.now()
#     # Деактивировать истекшие подписки
#     expired_subscriptions = UserTariffSubscription.objects.filter(end_date__lt=now, is_active=True)
#     for subscription in expired_subscriptions:
#         subscription.is_active = False
#         subscription.save()
#
#         # Если это бизнес-аккаунт, удалить UP со всех объявлений пользователя
#         if subscription.tariff.type == 'business_account':
#             Ad.objects.filter(user=subscription.user).update(is_up=False)
#
# @shared_task
# def check_up_expiry():
#     now = timezone.now()
#     # Удалить UP с истекших объявлений
#     expired_ups = Ad.objects.filter(is_up=True, up_expiration__lt=now)
#     expired_ups.update(is_up=False)
