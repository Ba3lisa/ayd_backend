from __future__ import annotations

from django.urls import path

from app.bot.views import BotWebhook

urlpatterns = [
    path('', BotWebhook.as_view(), name='bot_webhook'),
]
