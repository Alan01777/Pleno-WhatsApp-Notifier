import logging
import os
from dotenv import load_dotenv
import requests
import time
import json
from requests.exceptions import RequestException
from datetime import datetime
from dataExtractor import DataExtractor
from env_vars import load_env_vars

class WhatsAppNotifier:
    def __init__(self, imposto, data_source):
        load_dotenv('../.env')
        self.TOKEN = os.getenv("META_TOKEN")
        if not self.TOKEN:
            logging.warning("META_TOKEN not found in environment variables.")
        self.url = 'https://graph.facebook.com/v20.0/315409608315070/messages'
        self.headers = {
            'Authorization': 'Bearer ' + self.TOKEN,
            'Content-Type': 'application/json'
        }
        self.imposto = imposto
        extractor = DataExtractor(imposto=imposto, data_source=data_source)
        self.contacts_dict = extractor.extractor()

    def send_messages(self, day):
        for name, contact in self.contacts_dict.items():
            data = {
                "messaging_product": "whatsapp",
                "to": contact,
                "type": "template",
                "template": {
                    "name": "aviso_imposto",
                    "language": {
                        "code": "pt_BR",
                        "policy": "deterministic"
                    },
                    "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": name
                                },
                                {
                                    "type": "text",
                                    "text": self.imposto
                                },
                                {
                                    "type": "text",
                                    "text": day
                                }
                            ]
                        }
                    ]
                }
            }
            try:
                response = requests.post(
                    self.url, headers=self.headers, data=json.dumps(data))
                response.raise_for_status()
            except RequestException as e:
                logging.error(f"Failed to send message to {name}. Error: {e}")
                print('Failed')
            else:
                now = datetime.now()
                logging.info(f"{now} --- Message sent to {name}")
                print('Success')
            time.sleep(3)