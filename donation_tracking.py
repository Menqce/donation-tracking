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

# Add a new donation
def add_donation(amount_donated, donation_date, donation_source, gift_aid, notes, donor_id, event_id):
    cursor.execute('''
        INSERT INTO 'DONATIONS' (amount_donated, donation_date, donation_source, gift_aid, notes, donor_id, event_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (amount_donated, donation_date, donation_source, gift_aid, notes, donor_id, event_id))
    connection.commit()

# Add a new event
def add_event(event_name, room_info, booking_time, event_cost):
    cursor.execute('''
        INSERT INTO 'EVENTS' (event_name, room_info, booking_time, event_cost)
        VALUES (?, ?, ?, ?)
    ''', (event_name, room_info, booking_time, event_cost))
    connection.commit()

# Add a new volunteer
def add_volunteer(first_name, last_name, phone_number):
    cursor.execute('''
        INSERT INTO 'VOLUNTEERS' (first_name, last_name, phone_number)
        VALUES (?, ?, ?)
    ''', (first_name, last_name, phone_number))
    connection.commit()

# View donations by donor
def view_donations_by_donor(donor_id):
    cursor.execute('''
        SELECT * FROM 'DONTAIONS' WHERE donor_id = ?
    ''', (donor_id,))
    donations = cursor.fetchall()
    for donation in donations:
        print(donation)

# Update donation
def update_donation(donation_id, amount_donated, gift_aid, notes):
    cursor.execute('''
        UPDATE 'DONATIONS' 
        SET amount_donated = ?, gift_aid = ?, notes = ? 
        WHERE donation_id = ?
    ''', (amount_donated, gift_aid, notes, donation_id))
    connection.commit()

# Delete a donation (note: prevents deletion if there are dependencies)
def delete_donation(donation_id):
    cursor.execute('''
        DELETE FROM 'DONATIONS' WHERE donation_id = ?
    ''', (donation_id,))
    connection.commit()

# Test function
def test_program():
    # Create tables
    create_tables()

    # sample data for teesting 
    # Adding donors
    add_donor("John", "Doe", "TechCorp", "B12 3DL", "12A", "1234567890")
    add_donor("Jane", "Smith", "HealthPlus", "AB1 2CD", "34B", "0987654321")

    # Adding an event
    add_event("Charity Gala", "Room 1", "2025-05-10 18:00", 5000.00)

    # Adding donations
    add_donation(200.00, "2025-04-25", 1, True, "Generous contribution", 1, 1)
    add_donation(150.00, "2025-04-26", 2, False, "Regular donation", 2, None)

    # Viewing donations by donor ID 1
    print("Viewing Donations by Donor ID 1:")
    view_donations_by_donor(1)

    # Updating donation
    print("Updating donation...")
    update_donation(1, 250.00, False, "Updated contribution")
    view_donations_by_donor(1)

    # Deleting donation
    print("Deleting donation...")
    delete_donation(1)
    view_donations_by_donor(1)

# Run testings 
test_program()

# Close connection after commiting 
connection.close()
