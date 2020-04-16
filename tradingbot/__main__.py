#!/usr/bin/env python3
"""
__main__.py for ISC POC Bot
This is the file which is executed 1st and starts the bot. this runs the main() function
defined in main.py file
> python -m tradingbot (with Python >= 3.6)
"""

from tradingbot import main

if __name__ == '__main__': #satisfied when module is run as the main module
    main.main()   #executes main function defined in main.py file
