import scp
from discord.ext import commands
from discord.ext import tasks
import json
import time
import discord

class Msgcheck(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.check_message.start()

    def read_json(self):
        with open('Management.json',mode="r") as f:
            data = json.load(f)
        return data

    def write_json(self,data):
        with open('Managements.json',mode="w") as f:
            json.dump(data,f,indent=4)
        return


    async def create_channel(self,name:str):
        msg = self.bot.get_channel(815591142451839007)
        ctg = msg.category
        channel = await ctg.create_text_channel(name=name)
        id = channel.id
        js = self.read_json()
        js["messages"][f"{name}"] = id



    async def get_message(self,d:dict):
        js = self.read_json()
        for person,content in d.items():
            if person not in js["messages"].keys():
                await self.create_channel(person)
                js = self.read_json()
            channel = self.bot.get_channel(js["messages"][person])
            for c in content:
                await channel.send(content)

    @commands.Cog.listener(name='on_message')
    async def on_message(self,message):
        msg = self.bot.get_channel(815591142451839007)
        ctg = msg.category
        if message.channel.category == ctg:
            return
        teacher_name = message.channel.name
        teacher_name = teacher_name.replace('-',' ')
        m = await ctx.send('`送信中...`')
        scp.send_msg(teacher_name,message.content)
        await message.add_reaction('👍')
        m.delete()
        
        
    @tasks.loop(seconds=60)
    async def check_message(self):
        res = scp.has_messages()
        if res is None:
            return
        self.get_message(res)

def setup(bot):
    bot.add_cog(Msgcheck(bot))

