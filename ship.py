# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:22:52 2018

@author: chaol
"""

import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """初始化飞船"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        #将每艘飞船放在屏幕底部中央
        self.image = pygame.image.load('images/ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # 移动 flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
             
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)