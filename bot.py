import nextcord
from nextcord.ext import commands

client = commands.Bot(command_prefix="!")


#
# NORMALE BEFEHLE
#
@client.command()
async def test(ctx):
    pass
    # Dieser Befehl wird duch !test ausgelöst!


#
# EVENTS
#
@client.event
async def on_ready():
    pass
    # Dieses Event löst beim Starten des Bot's aus!


#
# SLASH BEFEHLE
#
@client.slash_command(description="Test")
async def test(interaction: nextcord.Interaction):
    pass
    # Dieser Befehl wird duch /test ausgelöst!


#
# APPS
#
@client.message_command()
async def test(interaction: nextcord.Interaction):
    pass
    # Rechtsklick auf eine Nachricht > Apps


@client.user_command()
async def test(interaction: nextcord.Interaction):
    pass
    # Rechtsklick auf einen Benutzer > Apps

client.run("[Dein Bot Token]")
