from connect import *

def insert_films():
    # Ask for user input (FilmID, Title, YearReleased, Rating, Duration, and Genre)
    # FilmID is an auto-increment field and does not require an input.
    title = input("Enter Title: ")
    yearReleased = input("Enter Year Released: ")
    rating = input("Enter Rating: ")
    duration = input("Enter Duration (in minutes): ")
    genre = input("Enter Genre: ")

    try:
        # Insert data into the films table
        dbCursor.execute("INSERT INTO tblFilms (Title, YearReleased, Rating, Duration, Genre) VALUES (?, ?, ?, ?, ?)",
                         (title, yearReleased, rating, duration, genre))
        dbCon.commit()  # Make the changes permanent
        print(f"{title} inserted in the tblFilms table")
    except sql.OperationalError as e:
        dbCon.rollback()
        print(f"Insert failed: {e}")

if __name__ == "__main__":
    insert_films()
