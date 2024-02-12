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


def writeNewToDatabase(playerName, score):
    """Writes to the database"""
    conn, cur = dbConnector()  # connect to the database
    id = generatePriKey()
    query = """INSERT INTO tblScores VALUES(?,?,?,?,?)"""
    cur.execute(query, (id, playerName, 0, 0, score))
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


def writeNewRecord(playerName, score):
    """Writes a value to a specific record"""
    conn, cur = dbConnector()
    query = """SELECT count(*)FROM tblScores WHERE userName =?"""
    cur.execute(query, (playerName,))
    results = cur.fetchall()
    print(results)
    if results[0][0] == 1:
        appendExisting(playerName, score)
    else:
        writeNewToDatabase(playerName, score)
    # query record to be written to
    # prepare data to be written
    # open connection, write data, close connection


def generatePriKey():
    """reads records and generates a unique key"""
    conn, cur = dbConnector()
    query = """SELECT ID FROM tblScores """
    cur.execute(
        query,
    )
    results = cur.fetchall()
    print(results)
    newKey = results[-1][0] + 1
    conn.close()
    return newKey


def appendExisting(playerName, score):
    """appends and existing record with a new score, swaps out oldest score"""
    conn, cur = dbConnector()
    query = """SELECT score1, score3, score3 FROM tblScores WHERE userName=?"""
    cur.execute(query, (playerName,))
    results = cur.fetchall()
    print(results)

    updateQuery = (
        """UPDATE tblScores SET score1=?, score2=?, score3 =? WHERE userName =?"""
    )
    s1, s2, s3 = results[0][1], results[0][2], score
    cur.execute(updateQuery, (s1, s2, s3, playerName))
    conn.commit()
    conn.close()


# test dbConnection works
# print(dbConnector())
# writeToDatabase()
# readDatabaseRecords()
# writeNewRecord("Gio",3)
# print(generatePriKey())
# appendExisting("Thomas")
appendExisting("Gio", 9)
