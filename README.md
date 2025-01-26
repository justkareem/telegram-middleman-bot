# Telegram Relay Bot

Telegram Relay Bot is a Python-based bot built with the `python-telegram-bot` library. This bot acts as a bridge between users and an admin, relaying messages from users to the admin and allowing the admin to reply directly to the users.

## Features
- **User to Admin Communication**: Users can send messages to the bot, which are automatically forwarded to the admin.
- **Admin Replies**: Admin can reply to user messages by replying to forwarded messages, and the bot will relay the response back to the corresponding user.
- **User Tracking**: Keeps track of users who have sent messages, allowing seamless communication.

## How It Works
1. **User Initiates Conversation**: When a user sends a message to the bot, it forwards the message to the admin, including the user's details (e.g., name, username, and ID).
2. **Admin Responds**: The admin replies to the forwarded message, and the bot extracts the user ID from the original message to send the response back to the user.

## Prerequisites
- Python 3.9+
- A Telegram bot token (get one from [BotFather](https://t.me/botfather) on Telegram).

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/justkareem/telegram-middleman-bot.git
   cd telegram-middleman-bot
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install python-telegram-bot
   ```

4. **Set Your Bot Token**
   - Replace `<YOUR_BOT_TOKEN>` in the `main.py` file with your Telegram bot token.
   - - Replace `<your user id>` in the `main.py` file with your Telegram account user id.

5. **Run the Bot**
   ```bash
   python main.py
   ```

## Usage

1. **Start the Bot**: Users can send the `/start` command to the bot to receive a welcome message.
2. **Send Messages**: Any message sent by a user will be forwarded to the admin.
3. **Reply to Messages**: The admin can reply to forwarded messages to communicate directly with users.

## Code Overview

### Main Components

- **`/start` Command**: Greets users when they start the bot.
- **`relay_to_admin`**: Forwards user messages to the admin.
- **`relay_to_user`**: Sends admin replies back to the appropriate user.

### Key Variables
- `admin_id`: The Telegram user ID of the admin.
- `user_to_admin`: A dictionary to track users and their details for reverse communication.

## Example

1. User sends a message: `Hi, I need help!`
2. Admin receives:
   ```
   Message from John Doe (@johndoe): Hi, I need help!

   Reply to this message to respond to User ID: 123456789
   ```
3. Admin replies: `Sure, how can I assist?`
4. User receives: `Sure, how can I assist?`

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): The library used to power the bot.

