from dotenv import load_dotenv
import os
import discord
from discord import app_commands, channel, Interaction
import gspread
from google.oauth2.service_account import Credentials

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file("cedar-unison-475409-u6-e34e54e7b216.json", scopes=SCOPES)
gc = gspread.authorize(creds)

GUILD_ID = 1428320493903155213

# main body
class Client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)  # needed for slash commands

    async def on_ready(self): # on startup
        print(f'Logged in as {self.user}')

        try:
            guild = discord.Object(id=GUILD_ID)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')




# intents section

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.presences = True
intents.emojis = True
intents.webhooks = True

client = Client(intents=intents)

# Slash command section

@client.tree.command(name ="traininglog", description = "prints out the training log", guild = discord.Object(id = GUILD_ID))
@app_commands.describe(host = "Who hosted the event", passed_attendees = "which attendees passed", failed_attendees = "which attendees failed", phase = "phase")
async def traininglog(interaction: discord.Interaction, host: str, passed_attendees: str, failed_attendees: str, phase: str):
    author = interaction.user
    embed = discord.Embed(title=f'log created by {author.display_name}', description="training log results",color = discord.Color.blurple()) #declaring the embed

    if author.avatar:
        embed.set_thumbnail(url=author.avatar.url)

    embed.add_field(name="Host", value=host, inline=False) #adding lines/fields
    embed.add_field(name="Passed Attendees", value=passed_attendees or "None", inline=False)
    embed.add_field(name="Failed Attendees", value=failed_attendees or "None", inline=False)
    embed.add_field(name="Phase", value=phase, inline=False)

    await interaction.response.send_message(embed=embed)

    sheet = gc.open("WV, Police Academy Database").worksheet("Training logs ")
    try:
        # Find next empty row in column E (Host column)
        col_values = sheet.col_values(5)  # column E
        next_row = len(col_values) + 1

        sheet.update(f"E{next_row}", [[host]])
        sheet.update(f"G{next_row}:I{next_row}", [[passed_attendees] * 3])
        sheet.update(f"J{next_row}:L{next_row}", [[failed_attendees] * 3])
        sheet.update(f"M{next_row}", [[phase]])



    except Exception as e:
        print("failed to append the row", e)





client.run(TOKEN)
