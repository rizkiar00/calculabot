#!/usr/bin/env python
# coding: utf-8

# In[1]:


from telegram.ext import Updater
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from telegram.ext import CommandHandler, MessageHandler, Filters
import seaborn as sns; sns.set()
import numpy as np
import numexpr as ne
from matplotlib.colors import ListedColormap

updater = Updater(token='900944674:AAHwA4UGb4WE5ybDh18FUrw8PVx0GPLSzns', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



# def echo(update, context):
#     context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

# echo_handler = MessageHandler(Filters.text, echo)
# dispatcher.add_handler(echo_handler)

def calculate(update, context):
    try:
        funtion = ' '.join(context.args)
        output = ne.evaluate(funtion)
    except:
        output = str('Input Invalid')
    context.bot.send_message(chat_id=update.message.chat_id, text=str(output))

calculate_handler = CommandHandler('calculate', calculate)
dispatcher.add_handler(calculate_handler)

def graph2d(update, context):
    try:
        x = np.linspace(-10, 10, 100)
        function = ' '.join(context.args)
        y = ne.evaluate(function)
        ax = sns.lineplot(x=x, y=y, sort=False, lw=1)
        ax.figure.savefig("output.png")
        plt.clf()
        context.bot.send_message(chat_id=update.message.chat_id, text='Sending Image...')
        context.bot.send_photo(chat_id=update.message.chat_id, photo=open('output.png', 'rb'))
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text='Input Invalid. Please Use "x" as a Variable')

graph2d_handler = CommandHandler('graph2d', graph2d)
dispatcher.add_handler(graph2d_handler)

def graph3d(update, context):
    try:
        X = np.linspace(-10, 10, 100)
        Y = np.linspace(-10, 10, 100)
        x, y = np.meshgrid(X, Y)
        function = ' '.join(context.args)
        z = ne.evaluate(function)
        cmap = ListedColormap(sns.color_palette("RdBu_r", 100))
        plt.contourf(x, y, z, 100, cmap=cmap)
        plt.colorbar();
        plt.axis(aspect='image');
        plt.savefig('output.png')
        plt.clf()
        context.bot.send_message(chat_id=update.message.chat_id, text='Sending Image...')
        context.bot.send_photo(chat_id=update.message.chat_id, photo=open('output.png', 'rb'))
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text='Input Invalid. Please Use "x" and "y" as a Variable')

graph3d_handler = CommandHandler('graph3d', graph3d)
dispatcher.add_handler(graph3d_handler)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Hello, I am Calculabot. A bot who can calculate and draw a function :)")
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="For more info please use /help command")

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="The command is:")
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="1. /calculate ex: /calculate 5**(2/3*2)*log(10)")
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="2. /graph2d ex: /graph2d x ** 3+2")
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="3. /graph2d ex: /graph3d sin(x)+cos(y)")

help_handler = CommandHandler('help',help)
dispatcher.add_handler(help_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Sorry, I didn't understand that command. Use /help for command list")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.start_polling()


# In[2]:


#import numpy as np
# import numexpr as ne
# a = (1 + 1) * 2
# ne.evaluate(str(a))


# In[3]:




# In[ ]:




# In[ ]:




