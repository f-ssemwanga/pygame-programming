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
        conn = sq.connect("dbases/pygameScores.db")
        cur = conn.cursor()
        return conn, cur
    except sq.Error as e:
        print(f"Database connection error: {e}")


def writeToDatabase():
    """Writes to the database"""
    conn, cur = dbConnector()  # connect to the database

    query = """INSERT INTO tblScores VALUES(2, "Gio", 2,0,0)"""
    cur.execute(query)
    conn.commit()
    conn.close()
    print("Success")


def readDatabaseRecords():
    """Reads records from a database"""
    conn, cur = dbConnector()
    query = """SELECT * FROM tblScores"""
    cur.execute(query)
    results = cur.fetchall()
    print(results)
    conn.close()


def writeToSpecific():
    """Writes a value to a specific record"""
    # query record to be written to
    # prepare data to be written
    # open connection, write data, close connection


# test dbConnection works
print(dbConnector())
# writeToDatabase()
readDatabaseRecords()
