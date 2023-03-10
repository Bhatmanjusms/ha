#### This Code Was Devloped By @AM_ROBOTS ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://shorturllink.in/')
    START_TXT = environ.get("START_TXT", "ð·ð´ð»ð¾ {}")
    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ð¼ð ð·ð´ð»ð¿ ð²ð¾ð¼ð¼ð°ð½ð³ð."""
    ABOUT_TXT = """<b>â¯ ð¼ð ð½ð°ð¼ð´: {}</b>
<b>â® ð²ðð´ð°ðð¾ð: <a href=https://t.me/being_ram_esh>Ram_Esh</a></b>
<b>â® ð»ð¸ð±ðð°ðð: ð¿ððð¾ð¶ðð°ð¼</b>
<b>â® ð»ð°ð½ð¶ðð°ð¶ð´: ð¿ððð·ð¾ð½ ð¹</b>
<b>â® ð³ð°ðð° ð±ð°ðð´: ð¼ð¾ð½ð¶ð¾-ð³ð±</b>
<b>â® ð±ð¾ð ðð´ððð´ð: Ram_Esh</b>
<b>â® ð±ðð¸ð»ð³ ððð°ððð: ð1.0.43 [ ð±ð´ðð° ]</b>
<b>â® TELEGRAM ð²ð·ð°ð½ð½ð´ð»: <a href=https://t.me/+Lux41ZFL9-QxNmM1>á¯âJOINá¯á¶</a></b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- á¯âUâá¯á¶ is a not open source project. 
- Source - https://github.com/Rameshkumarsahutmr/RKSFILTER

<b>DEVS:</b>
- <a href=https://t.me/being_ram_esh>Ram_Esh</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and á¯âUâá¯á¶ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. á¯âRam_Eshá¯á¶ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- á¯âá¯á¶ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. á¯âRam_Eshá¯á¶ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/being_ram_esh)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of á¯âUâá¯á¶

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>
â ðð¾ðð°ð» ððð´ðð: <code>{}</code>
â ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>
â ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±
â ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#ððð°ðð«ð¨ð®ð©
    
<b>áâº ðð«ð¨ð®ð© âª¼ {}(<code>{}</code>)</b>
<b>áâº ðð¨ð­ðð¥ ððð¦ððð«ð¬ âª¼ <code>{}</code></b>
<b>áâº ððððð ðð² âª¼ {}</b>
"""
    LOG_TEXT_P = """#ððð°ðð¬ðð«  
    
<b>áâº ðð - <code>{}</code></b>
<b>áâº ððð¦ð - {}</b>
"""
