import mysql.connector
import os
from dotenv import load_dotenv


""" Create a database connection """
def create_connection():

    load_dotenv()

    conn = mysql.connector.connect(
        user = 'root',
        password="ENTER YOUR PASSWORD HERE",  #replace this with password to your own connection
        host = '127.0.0.1',
        database = 'formula1_db'
    )
    return conn

"""
Select driver info based on nationality (can modify)

Param: connection, nationality
"""
def select_driver_nationality(conn, nation):

    cursor = conn.cursor()

    query = ("select forename, surname, dob as birthdate "
             "from drivers "
             "where nationality = '"+nation+"' "
             "order by surname;")
    
    cursor.execute(query)

    for row in cursor.fetchall():
        first, last, dob = row
        print(f"{first:<30}{last:<30}{dob.strftime('%Y-%m-%d')}")


    cursor.close()

"""Select driver info of winners and their fastest laps"""
def select_winners_lap(conn):

    cursor = conn.cursor()

    query = ("select forename, surname, name, year, fastestLapTime "
            "from drivers "
            "inner join results "
            "on drivers.driverId = results.driverId "
            "inner join races "
            "on results.raceId = races.raceId "
            "where position=1; "
            )
    
    cursor.execute(query)

    for row in cursor.fetchall():
        first, last, track, year, lap = row
        print(f"{first:<30}{last:<30}{track:<30}{year:<30}{lap}")


    cursor.close()

"""
Select constructors that finished in a specific place in the race(can modify)

Param: connection, position
"""
def select_constructors(conn, position):

    cursor = conn.cursor()

    query = ("select name "
             "from constructors "
             "where constructorId in ( "
                "select constructorId "
                "from constructorStandings "
                "where position = "+position+");"
            )
    
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row[0])


    cursor.close()

"""Select races and the fastest stops if they are less than 23 seconds"""
def select_fastest_stop(conn):

    cursor = conn.cursor()

    query = ("select name, year, pits.fastestStop from races "
             " inner join ( "
                "SELECT raceId, MIN(duration) as fastestStop "
                "FROM pitStops  "
                "WHERE duration < 23.0 "
                "group by raceId "
            ") pits "
            "on races.raceId = pits.raceId; ")
    
    cursor.execute(query)

    for row in cursor.fetchall():
        track, year, stop = row
        print(f"{track:<30}{year:<30}{stop}")


    cursor.close()

"""Insert a new driver (myself)"""
def insert_myself(conn):

    cursor = conn.cursor()

    query = ('insert ignore into drivers '
             'value (6767, "zubariev", 67, "ZUB", "Oleh", "Zubariev", "2006-05-19", "Ukrainian", "https://www.linkedin.com/in/oleh-zubariev/");')
    
    cursor.execute(query)

    if cursor.rowcount > 0:
        print(" Insert successful!")
    else:
        print(" Insert failed.")


    cursor.close()

"""
Delete a constructor based on the nationality (can modify)

Param: connection, nationality
"""
def delete_constructor(conn, nation):

    cursor = conn.cursor()

    query = ("delete ignore from constructors " 
             "where constructorId>0 and nationality = '"+nation+"';)")
    
    cursor.execute(query)

    if cursor.rowcount > 0:
        print(" Delete successful!")
    else:
        print(" Delete failed.")

    cursor.close()

"""
results has a foreign key constructorId with on delete set null constraint.
to test it we select certain rows from results based on the foreign key,
then delete that constructor from the parent table and check if those rows of the child table are set to null
Works
"""
def test_on_delete(conn):
    cursor = conn.cursor()

    initial_select = ("select * from results where constructorId = 6 and grid = 22;") 

    cursor.execute(initial_select)

    for row in cursor.fetchall():
        print(row)

    delete_query = ("delete ignore from constructors "
                    "where constructorId = 6;")
    
    cursor.execute(delete_query)

    if cursor.rowcount > 0:
        print(" Delete successful!")
    else:
        print(" Delete failed.")

    final_select = ("select * from results where constructorId = 6 and grid = 22;")

    cursor.execute(final_select)

    for row in cursor.fetchall():
        print(row)

    cursor.close()


"""
constructorStandings has a foreign key constructorId with on update cascade constraint.
to test it we select certain rows from constructorStandings based on the foreign key,
then update that constructor from the parent table and check if those rows of the child table are updated
Works
"""
def test_on_update(conn, initial, final):
    cursor = conn.cursor()

    initial_select = ("select * from constructorStandings where constructorId="+initial+";") 

    cursor.execute(initial_select)

    for row in cursor.fetchall():
        print(row)

    delete_query = ("update constructors "
                    "set constructorId= "+final+
                    " where constructorId="+initial+";")
    
    cursor.execute(delete_query)

    if cursor.rowcount > 0:
        print(" Update successful!")
    else:
        print(" Update failed.")

    final_select = ("select * from constructorStandings where constructorId="+final+";")

    cursor.execute(final_select)

    for row in cursor.fetchall():
        print(row)

    cursor.close()




if __name__ == '__main__':

    # Create database connection
    conn = create_connection()
    if conn is None:
        print("Connection failed")
        exit()
    
    print("Connection successful")
    while(True):   #added the while loop after recording the video
        choice = input(
            "\nWhich query would you like to run?\n"
            "1. Select driver info based on nationality (can modify)\n"
            "2. Select driver info of winners and their fastest laps\n"
            "3. Select constructors that finished in a specific place in the race(can modify)\n"
            "4. Select races and the fastest stops if they are less than 23 seconds\n"
            "5. Insert a new driver (myself)\n"
            "6. Delete a constructor based on the nationality (can modify)\n"
            "7. Test ON DELETE SET NULL\n"
            "8. Test ON UPDATE CASCADE (can modify)\n"
            "Enter q to exit\n"
            "Your choice is: "
        )

        if choice == "1":
            nation = input("Enter drivers' nationality (e.g., German, Spanish): ")
            select_driver_nationality(conn, nation)

        elif choice == "2":
            select_winners_lap(conn)

        elif choice == "3":
            position = input("Select position in constructor's: ")
            select_constructors(conn, position)

        elif choice == "4":
            select_fastest_stop(conn)

        elif choice == "5":
            insert_myself(conn)

        elif choice == "6":
            nation = input("Insert nationality (e.g., French): ")
            delete_constructor(conn, nation)

        elif choice == "7":
            test_on_delete(conn)

        elif choice == "8":
            initial = input("Insert initial constructorId: ")
            final = input("Insert final constructorId: ")
            test_on_update(conn, initial, final)

        elif choice == "q":
            break

        else:
            print("Invalid choice")

        

    conn.close()