# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:57:44 2018

@author: chaol
"""
import pygame
from pygame.sprite import Group
from setting import Settings
import game_functions as gf
from game_stats import GameStats
from ship import Ship

def run_game():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, screen, ship, aliens, bullets)
        
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
    
    
run_game()