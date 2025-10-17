Discord Training Bot

A Discord bot that logs training sessions to Google Sheets and provides confirmation embeds in Discord.

Features

Slash command /traininglog to record:

Host

Passed attendees

Failed attendees

Training phase

Sends an embedded confirmation in Discord.

Automatically logs the data to a Google Sheet.

Designed for easy setup and use.

File Structure
SampleBot/
│
├─ main.py           # Main bot code
├─ keep_alive.py     # Optional: for hosting (e.g., Pella/Replit)
├─ requirements.txt  # Python dependencies
├─ .env              # Discord bot token (not tracked in Git)
└─ service_account.json  # Google Sheets service account JSON (not tracked in Git)

Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name


Or download the ZIP and extract it.

2. Install Python & Dependencies

Make sure Python is installed.
Create a virtual environment and install dependencies:

python -m venv venv
# Activate virtual environment:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

3. Discord Bot Setup

Go to the Discord Developer Portal
.

Create a new application → add a bot → copy the bot token.

Create a .env file in the project root:

DISCORD_TOKEN=your_bot_token_here


In main.py, replace the GUILD_ID variable with your server’s ID.

4. Google Sheets Setup

Create a service account in Google Cloud Console
.

Enable Google Sheets API and Google Drive API.

Download the JSON key file and place it in the project folder.

Share your Google Sheet with the service account’s email (xxxx@xxxx.iam.gserviceaccount.com) with Editor permissions.

In main.py, replace the JSON filename in the code with your service account JSON file.

5. Run the Bot
python main.py


The bot should now come online and respond to the /traininglog command.

Usage Example

In Discord, type:

/traininglog host: Alice passed_attendees: Bob,Charlie failed_attendees: Dave phase: Phase 1


The bot will:

Send an embed with the training log in Discord

Add a new row in the Google Sheet with the data

Hosting Tips

For 24/7 uptime, you can host on cloud services like Pella
 or Replit
.

Keep your .env and service account JSON private; do not commit them to GitHub.

Security Notes

Never share your Discord bot token or Google service account JSON.

Use .gitignore to exclude .env and JSON files from Git.
