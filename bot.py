from pyrogram import Client, filters
import os

bot_token = "6613078098:AAHnfVWoohhJRHA4imSnK7egxjn26tIohvw"
app = Client("my_bot", api_id=22912393, api_hash="e06daed2383e67661ad12936593dfc4c", bot_token=bot_token)


# Define a filter to ensure only the bot owner can use the command
def is_owner(_, __, update):
    return update.from_user.id == 1734100686


# Define the command handler to convert the HTML file to TXT
@app.on_message(filters.command("convert_to_txt") & is_owner)
def convert_html_to_txt(_, update):
    # Check if there is a document attached to the message
    if not update.document:
        update.reply_text("Please attach a HTML file to the message!")
        return
    
    # Check if the attached document is a HTML file
    if not update.document.file_name.endswith(".html"):
        update.reply_text("Please attach a HTML file to the message!")
        return
    
    # Download the HTML file
    html_file = app.download_media(update.document)

    # Convert the HTML file to TXT using lynx
    txt_file = os.path.splitext(html_file)[0] + ".txt"
    os.system(f"lynx -dump {html_file} > {txt_file}")
    
    # Send the converted file to the user
    update.reply_document(document=txt_file)

app.run()
