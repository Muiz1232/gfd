from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "24490919")
    API_HASH = environ.get("API_HASH", "d1b3b15126c47dd4cb491553ee1db910")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6576462283:AAHDzCx80v6dJX2FBrpb3-Js-EzhDnYcftM")
    STRING_SESSION = environ.get("STRING", "BQF1s6cAoxZitr4Z_3Dcn3QsBeP81fETNQGxlUPUHhssgVCgysgMwrv8JqNLXuvlp1wB2Qw3bjPxzBIcWlTgfuVvrc7hf5Ez0TEH7i4POyU0fSq14QTjzBlDBhALJu779JyQRuySPYM7CYhYk1EgCs90G3X2GUS2dO-cdkqzxwEPP7VJtYvxz7Eei4PYTH2Kd9P7_BGiagf0JG4GIrwYPUDz7_np_8UVwGkii9X54zzXuD9nvDAXIjkiuOTLxZl6LcuGKcbobdPIsOYA1db0O4SkN1FvoO9Bu6yadGkhwM8bKF8FYAOA68NMpPFcu9D00gxjv0-NP96WACwUzziDSQeLeHGcgAAAAAF0xr8GAA")
    SUDO_USERS = environ.get("SUDO_USERS", "5792432243")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
