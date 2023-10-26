'''
This is the main file that runs the application.
'''
import database
import user
import export
def main():
    # Create a database connection
    db = database.Database()
    # Create a User object
    user_obj = user.User(db)
    # User login
    if user_obj.login():
        # Fetch data for the user
        data = db.fetch_data(user_obj.user_id)
        # Export data to Excel
        export.to_excel(data)
if __name__ == "__main__":
    main()