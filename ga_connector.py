from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from flask import Blueprint, request, jsonify
import requests
from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.channel import InputChannel
from rasa_core.channels.channel import CollectingOutputChannel

logger = logging.getLogger(__name__)



		
class GoogleConnector(InputChannel):
    """A custom http input channel.

    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""

    @classmethod
    def name(cls):
        return "google_home"

    #def __init__(self):
    #    self.out_channel = CustomOutput(url, access_token)

    def blueprint(self, on_new_message):
        from flask import Flask, request, Response
        import json	    
        google_webhook = Blueprint('google_webhook', __name__)

        @google_webhook.route("/", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @google_webhook.route("/webhook", methods=['POST'])
        def receive():
            payload = json.loads(request.data)		
            sender_id = payload['user']['userId']
            intent = payload['inputs'][0]['intent'] 			
            text = payload['inputs'][0]['rawInputs'][0]['query'] 		
            if intent == 'actions.intent.MAIN':	
                message = "<speak>Hello! <break time=\"1\"/> Welcome to the Rasa-powered Google Assistant skill. You can start by saying hi."			 
            else:
                out = CollectingOutputChannel()			
                on_new_message(UserMessage(text, out, sender_id))
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
          		
        return google_webhook

		
		
		
	