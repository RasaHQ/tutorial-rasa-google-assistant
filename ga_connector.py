import logging
import json
from sanic import Blueprint, response
from sanic.request import Request
from typing import Text, Optional, List, Dict, Any

from rasa.core.channels.channel import UserMessage, OutputChannel
from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import CollectingOutputChannel



logger = logging.getLogger(__name__)


		
class GoogleConnector(InputChannel):
    """A custom http input channel.

    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""

    @classmethod
    def name(cls):
        return "google_assistant"


    def blueprint(self, on_new_message):
	    
        google_webhook = Blueprint('google_webhook', __name__)

        @google_webhook.route("/", methods=['GET'])
        async def health(request):
            return response.json({"status": "ok"})

        @google_webhook.route("/webhook", methods=['POST'])
        async def receive(request):
            payload = request.json	
            intent = payload['inputs'][0]['intent'] 			
            text = payload['inputs'][0]['rawInputs'][0]['query'] 
	
            if intent == 'actions.intent.MAIN':	
                message = "Hello! Welcome to the Rasa-powered Google Assistant skill. You can start by saying hi."			 
            else:
                out = CollectingOutputChannel()			
                await on_new_message(UserMessage(text, out))
                responses = [m["text"] for m in out.messages]
                message = responses[0]
            r = {
                  "expectUserResponse": 'true',
                  "expectedInputs": [
                    {
                      "possibleIntents": [
                        {
                          "intent": "actions.intent.TEXT"
                        }
                    ],
                    "inputPrompt": {
                      "richInitialPrompt": {
                        "items": [
                          {
                            "simpleResponse": {
                              "textToSpeech": message,
                              "displayText": message
                              }
                            }
                          ]
                        }
                      }
                    }
                  ]
                }

            return response.json(r)				
          		
        return google_webhook

		
		
		
	
