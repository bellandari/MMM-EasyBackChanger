# MMM-EasyBackChanger

This is a Python bot that will change the video being displayed by MMM-EasyBack : https://github.com/mykle1/MMM-EasyBack
It works in conjuction with MMM-AutoRefresh : https://github.com/jasonyork/MMM-auto-refresh

I did a complete write up inside the Python file itself explaining what everything does and what it accesses. 
The short of it is: It accesses the MMM-EasyBack video folder, picks a file and then edits the MagicMirror config.js file with the new information. 
When MMM-AutoRefresh does its refresh, the new video will be playing. 

This file can be modified to do photos as well, user will need to change the extension the bot looks for as well as the directory it looks for it in. 

In order to work properly, this program needs to run in the background of the Raspberry Pi. I've been using it for about a week and have had zero problems and no noticible performance losses. 

If there are any issues, please let me know! 
