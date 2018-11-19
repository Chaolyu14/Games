# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:56:35 2018

@author: chaol
"""

class GameStats():
    
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
