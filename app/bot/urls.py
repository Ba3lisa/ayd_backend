from django.urls import include, path
from app.bot.views import BotWebhook

urlpatterns = [
    path('', BotWebhook.as_view(), name='bot_webhook'),
]

