# This is a Python bot that will change MagicMirror's config.js file at a given interval. 
# I use this to change the video that is played by MMM-EasyBack: https://github.com/mykle1/MMM-EasyBack
# This is also used in conjunction with MMM-AutoRefresh: https://github.com/jasonyork/MMM-auto-refresh as MagicMirror won't update by itself. 
# This module runs in the background on the Pi and uses very little resources.
# I've been using it for about a week and have had no issues as of yet. 

# Needed modules

import re # Needed for pattern search
import random # Needed to randomize content selection
import time # Needed to time delay
import os # Needed to access folder directories

# Main function - everything inside is explained incase you want to modify it for yourself.

def main():
    
    # Opens the config.js file at the specified directory.
    # If yours is different, change this. 
    
    with open('/home/pi/MagicMirror/config/config.js', 'r+') as f:
        content = f.read()
        
        # This line accesses the MMM-EasyBack video directory and picks a random file.
        # Once again, if your video directory is different, change this.
        
        new = random.choice(os.listdir('/home/pi/MagicMirror/modules/MMM-EasyBack/videos'))
        
        # This is the pattern to search the config.js file for the specified file. 
        # If you're using this for photos, change the (mp4) to whatever the filetype you're using (jpg), (png).
        
        pattern = "[a-zA-Z0-9]+\.(mp4)"

        # This is the delay. The first number is seconds, the second is minutes. 
        # My MMM-AutoRefresh module refreshes every 30 minutes, this does as well. 
        # This means each video will play for 30 minutes before MagicMirror refreshes. 
        
        time.sleep(60*30)
        
        # Unless needed, I wouldn't mess with anything below this. 
        
        if re.search(pattern, content):
            print("Found current entry...")
            f.seek(0)
            f.truncate(0)

            # This searches the config.js file for the above pattern (line 24). 
            # Once found, it will erase the file (line 38 & 39), replace the specified content (pattern)
            # with the new (new) content and write it back to the same file, (line 46). It will print
            # both occurances to the terminal for easy reference and tracking. 
            
            f.write(re.sub(pattern, new, content))
            print(f"Change made to {new}")
            f.close()
            
            # Once the above is complete, it will call the main function and activate the timer. 
            
            main()

        # If for whatever reason it doesn't find any matching patterns, it will terminate. 
        
        else:
            print("Unable to find matching pattern. Terminating.")
main()
