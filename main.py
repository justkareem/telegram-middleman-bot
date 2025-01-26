from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Dictionary to track users for reverse communication
user_to_admin = {}

# Replace with your Telegram user ID (admin ID)
admin_id = "<your user id>"
YOUR_BOT_TOKEN = "<your bot token>"


# Command: /start
# Sends a welcome message to users when they start the bot.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! I’ll relay your messages to the admin.")


# Handles messages from users and forwards them to the admin.
async def relay_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user  # Retrieve the user who sent the message
    user_id = user.id  # Extract the user ID
    message = update.message.text  # Extract the message text

    # Save user details to enable reverse communication
    user_to_admin[user_id] = user

    # Format the message to send to the admin
    admin_message = (
        f"Message from {user.first_name} (@{user.username}): {message}\n\n"
        f"Reply to this message to respond to User ID: {user_id}"
    )

    # Send the message to the admin
    await context.bot.send_message(chat_id=admin_id, text=admin_message)


# Handles replies from the admin and sends them back to the corresponding user.
async def relay_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:  # Ensure the admin is replying to a forwarded message
        reply_text = update.message.reply_to_message.text

        if "User ID:" in reply_text:
            try:
                # Extract the user ID from the admin's reply
                user_id = int(reply_text.split("User ID:")[1].strip())
                response = update.message.text  # Get the admin's response text

                # Send the response back to the user
                await context.bot.send_message(chat_id=user_id, text=response)
            except (IndexError, ValueError):
                await update.message.reply_text(
                    "Failed to extract User ID. Please ensure you reply to a valid message.")
        else:
            await update.message.reply_text("Please reply to a message that includes the User ID.")
    else:
        await update.message.reply_text("Reply to a forwarded message to respond.")


# Main function to initialize the bot and its handlers.
def main():
    # Initialize the bot with the token
    application = Application.builder().token(YOUR_BOT_TOKEN).build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Add message handler to process admin replies
    application.add_handler(
        MessageHandler(filters.TEXT & filters.REPLY & filters.User(user_id=admin_id), relay_to_user)
    )

    # Add message handler to process user messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, relay_to_admin))

    # Start polling for updates
    application.run_polling()


if __name__ == '__main__':
    main()
