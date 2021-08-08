from wocky_termuix import WockyTermUIX
import os, sys, time, discord, threading, requests

from commands.help import *
from get_new_code import *

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        word_list = ['cheat', 'cheats', 'hack', 'hacks', 'internal', 'external', 'ddos', 'denial of service']
        links = ['http', 'https', 'https://', 'www.', '.com', '.pw', '.tech', '.net', '.io', '.xyz', '.cf', '.ga']

        # don't respond to ourselves
        if message.author == self.user:
            return

        ## Logger
        print(f"[NEW MESSAGE LOG]")
        print(f"[Name]: {message.author.name} | [ID]: {message.author.id}")
        print(f"[Server]: {message.guild.name} | [ID]: {message.guild.id}")
        lol = message.content.split(" ")[0]
        print(f"[CMD]: {lol} [MESSAGE]: {message.content}\r\n")

        messageContent = message.content
        if len(messageContent) > 0:
            if message.author.guild_permissions.administrator != True:
                for word in word_list:
                    if word in messageContent:
                        await message.delete()
                        await message.channel.send('Blacklisted word!\r\n')
                for link in links:
                    if link in messageContent:
                        await message.delete()
                        await message.channel.send('No Links Skid!')


            if messageContent == "help":
                await message.channel.send(f"```{help_cmd(messageContent)}```")

            
            elif "img2txt" in messageContent:
                url = GetCode(message.content.split(" ")[1])
                await message.channel.send(f"ASNI Text URL: {url}")
            
        messageattachments = message.attachments
        if len(messageattachments) > 0:
            for attachment in messageattachments:
                if attachment.filename.endswith(".dll"):
                    await message.delete()
                    await message.channel.send("No DLL's allowed!")
                elif attachment.filename.endswith('.exe'):
                    await message.delete()
                    await message.channel.send("No EXE's allowed!")
                else:
                    break

client = MyClient()
client.run("ODczNDc4MTQ3MTg0NjYwNTIw.YQ4_6g.XxM1MSp22gvtq80DznyZ-GlLKFY")
# while(True):
#     inputcmd = input("Sup dude: ")
#     print(inputcmd)