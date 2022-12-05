#import the module telegram.ext
import telegram.ext
#This token is use to access the http api of telegram bot.This token is provided by BotFather.
Token="5640196922:AAG6C3ECDAbTljakw7HGdNUlB6yN1QGKZ-o"
#this object is use to perform with the bot.
updater=telegram.ext.Updater("5640196922:AAG6C3ECDAbTljakw7HGdNUlB6yN1QGKZ-o", use_context=True)
dispatcher=updater.dispatcher
#add some function.
#start command for starting the bot.#first message will be:hello welcome to etc etc...
def start(update, context):
    update.message.reply_text("Hello! Welcome to Techhub, type or click /help for select more options")
#this function we send the message with the command start the help content and for the playlist of the subject.    
def help(update, context):
    update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This perticular message
        /content -> About various playlist of Techhub
        /python -> The first video from python playlists
        /Sql -> The first video from SQL plyalists
        /Java -> The first video from Java playlists
        /contact -> contact information
        """
        )
#this will define all this command for output of the user. 
def content(update, context):
    update.message.reply_text("We have various playlists and articles available type or click on any subject to access the video")
    
def python(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=_xj5EXRwvW8&list=PLRA5R2KxGlkXMnty1_-644q7mxpOV-js6")
    
def Sql(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=n8OYmMsRNwM&list=PLRA5R2KxGlkUf-8t1VcJBCHilw3-Q8vZC")

def Java(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=WmeBbeUIGBs&list=PLRA5R2KxGlkV4MVAaKMHj2UtWho-Qaakp")

def contact(update, context):
    update.message.reply_text("You can contact on the registerd mail id provide here: https://lingarajtechhub.com/")
#this all function we will add with the dispatcher.and create a commandhandler to handel the function.    
dispatcher.add_handler(telegram.ext.CommandHandler("start",start))
dispatcher.add_handler(telegram.ext.CommandHandler("content",content))
dispatcher.add_handler(telegram.ext.CommandHandler("python",python))
dispatcher.add_handler(telegram.ext.CommandHandler("Sql",Sql))
dispatcher.add_handler(telegram.ext.CommandHandler("Java",Java))
dispatcher.add_handler(telegram.ext.CommandHandler("contact",contact))
dispatcher.add_handler(telegram.ext.CommandHandler("help",help))
#this command will check if the program will working or not.
updater.start_polling()
#this command will not exit the after the first command entry and it will wait for the user enter the other command
updater.idle()