import logging
import os
from whatsapp_notifier import WhatsAppNotifier

if __name__ == "__main__":
    if not os.path.exists('Logs'):
        os.makedirs('Logs')

    logging.basicConfig(filename='Logs/logs.log', level=logging.INFO)

    # You should be able to modify the lines below, using the source files you made
    tax_data_sources = {
        "DAS": {
            "source": "Data/DAS.xlsx",
            "day": "20"
        },
        "FGTS": {
            "source": "Data/FGTS.xlsx",
            "day": "05"
        },
        "PIS": {
            "source": "Data/PIS.xlsx",
            "day": "10"
        },
        "COFINS": {
            "source": "Data/COFINS.xlsx",
            "day": "15"
        },
        "PARCELAMENTO": {
            "source": "Data/PARCELAMENTO.xlsx",
            "day": "20"
        }
    }

    for tax, info in tax_data_sources.items():
        notifier = WhatsAppNotifier(tax, info["source"])
        notifier.send_messages(info["day"])
