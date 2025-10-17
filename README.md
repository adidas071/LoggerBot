equirements

Python 3.10+

PyCharm (or any Python IDE)

Windows OS

Setup

1️⃣ Download and extract

Download the ZIP of the repository.

Extract it to a folder on your PC.

Open the folder in PyCharm.

2️⃣ Create a virtual environment

python -m venv venv

venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure .env

Create a .env file in the project folder:

DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN


No spaces around =

5️⃣ Configure Google Sheets

Create a Google Cloud Service Account.

Download the JSON credentials file.

Enable Google Sheets API and Google Drive API.

Share your Google Sheet with the service account email (Editor).

Place JSON in the project folder.

Example in main.py:

creds = Credentials.from_service_account_file("service_account.json", scopes=SCOPES)

6️⃣ Set your server ID

Open main.py

Replace GUILD_ID with your server ID:

GUILD_ID = 123456789012345678

7️⃣ Run the bot

Slash Command Usage

/traininglog – Logs a training session.

Parameters:

host – Who hosted

passed_attendees – Passed attendees

failed_attendees – Failed attendees

phase – Training phase

The bot sends an embed in Discord and logs data to Google Sheets.

Security

Do not share .env or JSON credentials.

Keep your bot token safe.

Regenerate token if leaked.

File Structure
main.py
keep_alive.py
requirements.txt
.env                 # Discord token
service_account.json # Google credentials
