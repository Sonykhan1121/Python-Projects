from instabot import Bot
import os
import shutil
# The code snippet is checking if a folder named "config" exists in the current directory. If the
# folder exists, it is being removed (deleted) using `shutil.rmtree(config_folder)`. This is a way to
# ensure that any existing configuration data in the "config" folder is deleted before proceeding with
# the rest of the code.
config_folder = "config"
if os.path.exists(config_folder):
    shutil.rmtree(config_folder)

bot = Bot()
bot.login(username='sonykhan1121',password='SidratulMontaha01871787348')
bot.follow('zuck')
