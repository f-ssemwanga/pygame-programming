import pygame
import sqlite3 as sq

font_name = pygame.font.match_font("arial")


def draw_text(surf, text, size, x, y, clr):
    """Create a font object"""
    try:
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, clr)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
    except pygame.error as e:
        print(f"Pygame Error: {e}")


def dbConnector():
    """Connect to the database and return a connection object"""
    try:
        conn = sq.connect("")
        cur = conn.cursor()
        return conn, cur
    except sq.Error as e:
        print(f"Database connection error: {e}")


dbConnector()
