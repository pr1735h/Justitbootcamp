from connect import *
import sqlite3 as sql
import datetime  # For capturing the current date and time
import logging

def log_error(error_message):
    """Logs the error message along with the current date and time."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Configure logging (you can adjust the filename and other settings)
    logging.basicConfig(filename="PyProject/UpdateErrors.log", level=logging.ERROR)
    
    # Log the error message
    logging.error("[%s] Error: %s", timestamp, error_message)

if __name__ == "__main__":
    # Example usage
    log_error("Something went wrong!")


def update_films():
    try:
        # Use FilmID, which is a primary key and a unique field, to update a record.
        filmID = input("Enter the FilmID to update a record: ")

        # The field selected for the update (title, yearReleased, rating, duration, or genre).
        fieldName = input("Enter the field (Title, YearReleased, Rating, Duration, or Genre) to update: ").title()

        # The value to be entered in the field.
        fieldValue = input(f"Enter the new value for {fieldName}: ")

        # Add quotes to field value
        fieldValue = f"'{fieldValue}'"

        # Check if the FilmID exists
        dbCursor.execute(f"SELECT filmID FROM tblFilms WHERE filmID = {filmID}")
        existing_film = dbCursor.fetchone()

        if existing_film:
            # FilmID exists, proceed with the update
            dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE FilmID = {filmID}")
            dbCon.commit()
            print(f"{filmID} updated in the tblFilms table")
        else:
            log_error(f"FilmID {filmID} does not exist.")
            print(f"Error: FilmID {filmID} does not exist.")
    except sql.OperationalError as e:
        log_error(f"Update failed: {e}")
        print(f"Update failed: {e}")
    except ValueError:
        log_error("Invalid input. Please enter a valid FilmID.")
        print("Error: Invalid input. Please enter a valid FilmID.")
    except Exception as e:
        log_error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    update_films()
