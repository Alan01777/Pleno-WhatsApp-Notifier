import logging
import os
from datetime import datetime, timedelta
from whatsapp_notifier import WhatsAppNotifier

if __name__ == "__main__":
    if not os.path.exists('Logs'):
        os.makedirs('Logs')

    logging.basicConfig(filename='Logs/logs.log', level=logging.INFO)

    # List of month names in Portuguese
    month_names = ["de Janeiro", "de Fevereiro", " de Março", " de Abril", "de Maio", "de Junho", 
                   "de Julho", "de Agosto", "de Setembro", "de Outubro", "de Novembro", "de Dezembro"]

    # Get the previous month's name
    previous_month = month_names[(datetime.now().month - 2) % 12]

    tax_data_sources = {
        "DAS": {
            "source": "Data/DAS.xlsx",
            "day": "13",
            "month": previous_month
        },
        # "FGTS": {
        #     "source": "Data/FGTS.xlsx",
        #     "day": "05",
        #     "month": previous_month
        # },
        "PIS E COFINS": {
            "source": "Data/PIS e COFINS.xlsx",
            "day": "23",
            "month": previous_month
        },
        "PARCELAMENTO": {
            "source": "Data/PARCELAMENTO.xlsx",
            "day": "28",
            "month": previous_month
        }
    }

    for tax, info in tax_data_sources.items():
        # Get the current day
        current_day = datetime.now().day

        # Gets the day the tax needs to be paid and subtracts a number
        tax_day = max(1, int(info["day"]) - 2)
        # Check if the tax day falls on a weekend
        tax_date = datetime.now().replace(day=tax_day)
        if tax_date.weekday() > 4:  # 5 and 6 corresponds to Saturday and Sunday
            tax_day -= tax_date.weekday() - 4  # adjust to the preceding Friday

        # If the current day is the same as the tax day, send the messages
        if current_day == tax_day:
            notifier = WhatsAppNotifier(tax, info["source"])
            notifier.send_messages(info["day"], info["month"])
        else:
            print(f"{tax} will only be sent on day {tax_day}")