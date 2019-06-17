import asyncio
import inspect
import json
import logging
import uuid

from rasa.core.channels.channel import UserMessage, OutputChannel
from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import CollectingOutputChannel
from asyncio import Queue, CancelledError
from sanic import Sanic, Blueprint, response
from sanic.request import Request

from typing import (
    Text,
    List,
    Dict,
    Any,
    Optional,
    Callable,
    Coroutine,
    Iterable,
    Awaitable,
)

import rasa.utils.endpoints
from rasa.constants import DOCS_BASE_URL
from rasa.core import utils

logger = logging.getLogger(__name__)



		
class GoogleConnector(InputChannel):
    """A custom http input channel.

    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""

    @classmethod
    def name(cls):
        return "google_home"

    def __init__(
        self,
        username: Optional[Text] = None,
    ) -> None:
        self.username = username


    @staticmethod
    async def on_message_wrapper(
        on_new_message: Callable[[UserMessage], Awaitable[None]],
        text: Text,
        queue: Queue,
        sender_id: Text,
    ) -> None:
        collector = QueueOutputChannel(queue)

        message = UserMessage(
            text, collector, sender_id, input_channel=RestInput.name()
        )
        await on_new_message(message)

        await queue.put("DONE")  # pytype: disable=bad-return-type

    async def _extract_sender(self, req) -> Optional[Text]:
        return req.json.get("sender", None)


       # noinspection PyMethodMayBeStatic
    def _extract_message(self, req):
        return req.json.get("message", None)

    def stream_response(
        self,
        on_new_message: Callable[[UserMessage], Awaitable[None]],
        text: Text,
        sender_id: Text,
    ) -> Callable[[Any], Awaitable[None]]:
        async def stream(resp: Any) -> None:
            q = Queue()
            task = asyncio.ensure_future(
                self.on_message_wrapper(on_new_message, text, q, sender_id)
            )
            while True:
                result = await q.get()  # pytype: disable=bad-return-type
                if result == "DONE":
                    break
                else:
                    await resp.write(json.dumps(result) + "\n")
            await task

        return stream  # pytype: disable=bad-return-type




    #def __init__(self):
    #    self.out_channel = CustomOutput(url, access_token)

    def blueprint(self, on_new_message: Callable[[UserMessage], Awaitable[None]]):
        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            inspect.getmodule(self).__name__,
        )

        # noinspection PyUnusedLocal
        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request):
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=['POST'])
        async def receive(request: Request):
            payload = request.json		
            sender_id = payload['user']['userId']
            intent = payload['inputs'][0]['intent'] 			
            text = payload['inputs'][0]['rawInputs'][0]['query'] 		
            if intent == 'actions.intent.MAIN':	
                message = "<speak>Hello! <break time=\"1\"/> Welcome to the Rasa-powered Google Assistant skill. You can start by saying hi."			 
            else:
                out = CollectingOutputChannel()			
                on_new_message(UserMessage(text, out, sender_id, input_channel=self.name()))
                responses = [m["text"] for m in out.messages]
                message = responses[0]	
            r = json.dumps(
                {
                  "conversationToken": "{\"state\":null,\"data\":{}}",
                  "expectUserResponse": 'true',
                  "expectedInputs": [
                    {
                      "inputPrompt": {
                       "initialPrompts": [
                        {
                          "ssml": message
                        }
                      ]
                     },
                    "possibleIntents": [
                    {
                      "intent": "actions.intent.TEXT"
                    }
                   ]
                  }
                 ]
                })
            return r				
          		
        return custom_webhook

		
		
		
	
