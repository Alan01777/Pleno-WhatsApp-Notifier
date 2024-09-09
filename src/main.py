import logging
import os
from datetime import datetime
from whatsapp_notifier import WhatsAppNotifier

if __name__ == "__main__":
    if not os.path.exists('Logs'):
        os.makedirs('Logs')

    logging.basicConfig(filename='Logs/logs.log', level=logging.INFO)

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
        # Get the current day
        current_day = datetime.now().day

        # Gets the day the tax needs to be paid and substracts a number
        tax_day = int(info["day"]) - 2

        # Check if the tax day falls on a weekend
        tax_date = datetime.now().replace(day=tax_day)
        if tax_date.weekday() > 4:  # 5 and 6 corresponds to Saturday and Sunday
            tax_day -= tax_date.weekday() - 4  # adjust to the preceding Friday

        # If the current day is the same as the tax day, send the messages
        if current_day == tax_day:
            notifier = WhatsAppNotifier(tax, info["source"])
            notifier.send_messages(info["day"])
        else:
            print(f"{tax} will only be sent on day {tax_day}")