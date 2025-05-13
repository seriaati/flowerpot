import os
import discord


class FlowerpotBot(discord.Client):
    async def on_message(self, message: discord.Message):
        if message.author.id == 489647643342143491:
            await message.add_reaction("❓")


intents = discord.Intents.default()
intents.message_content = True

client = FlowerpotBot(intents=intents)
client.run(os.environ["DISCORD_TOKEN"])
