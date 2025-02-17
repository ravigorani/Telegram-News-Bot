# Telegram News Scraping Bot

This Telegram bot scrapes news from a specific website and sends the latest news articles to users. It uses asynchronous programming to efficiently retrieve and send the news, ensuring smooth performance and scalability.

---

## Features

- Scrapes the latest news from a specified website.
- Sends news to users in a conversational format with clickable links.
- Supports sending multiple news articles at once with a short delay.
- Customizable for different websites by modifying the `Scrapper()` function.

---

## Requirements

- Python 3.7+
- Telegram Bot API Token
- Libraries:
  - `python-telegram-bot` (v20+)
  - `aiohttp` (or any web scraping library you are using)

---

## Installation

1. Clone the repository or download the code.
   
   ```bash
   git clone https://github.com/your-username/telegram-news-bot.git
   cd telegram-news-bot
   
2. Install the required packages:
  
   ```bash
   pip install -r requirements.txt

3. Set Up Environment Variables
   <br>
   <br>
   Create a `.env` file in the root directory of the project and add the following content:
   ```bash
   GOOGLE_API_KEY= ypur-google-api-key-here

4. Add BotFather Token in `main.py` file:

   ```bash
   TOKEN = <your-token>
   
5. Run the Bot
   
   ```bash
   python main.py

6. Using the Bot
   <br>
   <br>
   
   Once the bot is running, open Telegram and search for your bot. Type the `/news` command, and the bot will reply with the latest news articles and their clickable links.
