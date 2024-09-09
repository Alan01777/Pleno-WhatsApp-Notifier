# Pleno WhatsApp Notifier

This project is designed to send reminder messages via WhatsApp using the WhatsApp Business Cloud API. It's particularly useful for sending reminders about tax due dates.

## Features

- Sends WhatsApp messages 2 days before each tax due date.
- Adjusts the message sending day to the preceding Friday if the tax due date falls on a weekend.
- Reads contact information from Excel files.

## Setup

1. Clone this repository.
2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Update the `tax_data_sources` dictionary in `main.py` with the correct Excel file paths and tax due dates.

4. Run `main.py`:

    ```bash
    python main.py
    ```

## Usage

The script will automatically send WhatsApp messages for each tax on the appropriate day. The messages are sent 2 days before the tax due date, or on the preceding Friday if the tax due date falls on a weekend.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)