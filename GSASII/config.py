# -*- coding: utf-8 -*-
'''
*config.py: Configuration options*
----------------------------------
This file created in SelectConfigSetting on 20 02 2023 15:48
'''

import os.path
import GSASIIpath

Main_Pos = (1467, 238)
'''Main window location - will be updated & saved when user moves
it. If position is outside screen then it will be repositioned to default
'''

Main_Size = (700, 450)
'''Main window size (width, height) - initially uses wx.DefaultSize but will updated
 and saved as the user changes the window
'''

Plot_Pos = (443, 119)
'''Plot window location - will be updated & saved when user moves it
these widows. If position is outside screen then it will be repositioned to default
'''

Plot_Size = (700, 600)
'''Plot window size (width, height) - initially uses wx.DefaultSize but will updated
 and saved as the user changes the window
'''

previous_GPX_files = [
	  "/Users/66j/Documents/ORNL/code/tmp/Silicon_6banks.gpx",
   ]
'''A list of previously used .gpx files
'''

