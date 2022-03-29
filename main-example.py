# Filename: main-example.py
# Created By: Greg Shalay (June 29th 2021)
# Description: A simple Discord bot that reports the current status of a minecraft server.
#
# DISCLAIMER: This script stores IP addresses, port numbers, and your discord bot token as string literals. This is ok
#             if you intend to use this code for a small personal minecraft server and trust those that will connect to
#             it as I have. This code is BY NO MEANS SUITABLE FOR USE IN A PROFESSIONAL ENVIRONMENT. Storing sensitive
#             information this way is not best practice. This is simply a file to show a possible solution for
#             implementing a Discord Bot.

import discord
import platform
import socket
import os

cornCount = 0

# IP and port of the server to connect to.
host = ''  # TODO: Your host IP goes here.
vanilla_host = ''  # TODO (Optional): add another host IP here if you want the script to listen to two separate IP's.
pixel_port = ''  # TODO: The port for your server that you want to listen to.
vanilla_port = ''  # TODO (Optional): add another host IP here if you want the script to listen to two separate ports.

# The token of the registered Discord Bot (blacked out for security)
TOK = ''  # TODO: Register for a Discord bot on Discord's website and put your token here.


# Method that builds pings a socket at a given server address.
def pingServer(serverAddr, port):
    # Create a socket connectrion and set its default timeout in seconds.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((serverAddr, int(port)))

    print(result)

    return result  # Executes the ping and returns its status.


client = discord.Client()


# Simple event handler that reports the ready status of the bot + its username- to the python shell.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Event handler that fires every time a message is sent in the server. If the message is a bot command,
# the proper routine will execute.
@client.event
async def on_message(message):
    # Reports the status of the server at the given host and port combination.
    if message.content == '!status':
        res = pingServer(host, pixel_port)
        # TODO: Create your own custom messages to send to your server.
        if res == 0:
            await message.channel.send("```CSS\n Greg\'s Pixelmon server is up!\n```")
        else:
            await message.channel.send("```HTTP\n Greg\'s Pixelmon server is down.\n```")

        van_res = pingServer(vanilla_host, vanilla_port)

        # TODO: Create your own custom messages to send to your server.
        if van_res == 0:
            await message.channel.send("```CSS\n Greg\'s Vanilla server (1.18.1) is up!\n```")
        else:
            await message.channel.send("```HTTP\n Greg\'s Vanilla server (1.18.1) is down.\n```")
        return

    elif message.content == '!ip':
        await message.channel.send("```HTTP\n Current Pixelmon Server IP: " + host + ":" + pixel_port + "\n```")
        await message.channel.send(
            "```HTTP\n Current Vanilla Server IP: " + vanilla_host + ":" + vanilla_port + "\n```")
    elif message.content == '!corn':
        global cornCount
        cornCount = cornCount + 1
        await message.channel.send("```\nCorn Count: " + str(cornCount) + "\n```")


# Finally, run the 'bot' application using our unique bot token.
client.run(TOK)
