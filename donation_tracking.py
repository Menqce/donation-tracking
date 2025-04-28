import sqlite3
connection = sqlite3.connect('donation_tracking.db')
cursor = connection.cursor()

# Create tables for DONORS, DONATIONS, EVENTS, VOULENTEERS, DONATION SOURCE
def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 'DONORS' (
            donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            business_name TEXT,
            postcode TEXT,
            house_number TEXT,
            phone_number TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 'DONATIONS' (
            donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount_donated REAL NOT NULL,
            donation_date TEXT NOT NULL,
            donation_source INTEGER NOT NULL,
            gift_aid BOOLEAN,
            notes TEXT,
            donor_id INTEGER,
            event_id INTEGER,
            FOREIGN KEY(donor_id) REFERENCES Donors(donor_id),
            FOREIGN KEY(event_id) REFERENCES Events(event_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 'EVENTS' (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            room_info TEXT,
            booking_time TEXT,
            event_cost REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 'VOLUNTEERS' (
            volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS 'DONATIONSOURCE' (
            source_id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_name TEXT NOT NULL,
            description TEXT
        )
    ''')

    connection.commit()

# Add a new donor
def add_donor(first_name, last_name, business_name, postcode, house_number, phone_number):
    cursor.execute('''
        INSERT INTO 'DONORS' (first_name, last_name, business_name, postcode, house_number, phone_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, business_name, postcode, house_number, phone_number))
    connection.commit()

# Adding donors
    add_donor("John", "Doe", "TechCorp", "B12 3DL", "12A", "1234567890")
    add_donor("Jane", "Smith", "HealthPlus", "AB1 2CD", "34B", "0987654321")


# Close connection after commiting 
connection.close()
