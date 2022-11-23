from __future__ import annotations

import logging

from rest_framework.response import Response
from rest_framework.views import APIView
logger = logging.getLogger(__name__)


class BotWebhook(APIView):
    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        logger.info(f'Received data: {data}')

        return Response({'status': 'ok', 'message': 'Hi !'})
