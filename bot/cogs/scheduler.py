import nextcord
from nextcord.ext import commands, tasks
import random
import os
import json
import aiohttp

class Scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63
        self.topics = self.load_topics()
        self.target_channel_id = 1268242910579654719
        self.fox_image_url = 'https://randomfox.ca/floof/'
        self.message_count = 0
        self.message_threshold = 5 
        self.fox_image_probability = 10

        self.send_topic.start()
        self.track_activity.start()

    def load_topics(self):
        json_path = os.path.join(os.path.dirname(__file__), '..', 'json', 'topics.json')
        with open(json_path, 'r') as file:
            data = json.load(file)
        return data["topics"]

    @tasks.loop(minutes=30)
    async def send_topic(self):
        channel = self.bot.get_channel(self.target_channel_id)
        if channel:
            random_topic = random.choice(self.topics)
            embed = nextcord.Embed(
                title="Topic",
                description=random_topic,
                color=self.color
            )
            try:
                await channel.send(embed=embed)
            except nextcord.Forbidden:
                pass

    @tasks.loop(seconds=60)
    async def track_activity(self):
        
        channel = self.bot.get_channel(self.target_channel_id)
        if self.message_count >= self.message_threshold:
            if random.randint(1, self.fox_image_probability) == 1:
                await self.maybe_send_fox_image(channel)
            self.message_count = 0  

    async def maybe_send_fox_image(self, channel):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.fox_image_url) as response:
                if response.status == 200:
                    data = await response.json()
                    fox_image = data['image']
                    fox_embed = nextcord.Embed(
                        title="Random Fox Image",
                        color=self.color
                    )
                    fox_embed.set_image(url=fox_image)
                    try:
                        await channel.send(embed=fox_embed)
                    except nextcord.Forbidden:
                        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == self.target_channel_id:
            self.message_count += 1

    @send_topic.before_loop
    async def before_send_topic(self):
        await self.bot.wait_until_ready()

    @track_activity.before_loop
    async def before_track_activity(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Scheduler(bot))
