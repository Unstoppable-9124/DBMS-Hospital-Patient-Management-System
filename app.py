from db import get_connection

# Add Patient
def add_patient():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Patient(name, age, gender) VALUES (%s, %s, %s)",
        (name, age, gender)
    )

    conn.commit()
    conn.close()

    print("✅ Patient Added Successfully")


# View Patients
def view_patients():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Patient")
    data = cursor.fetchall()

    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}")

    conn.close()


# Add Doctor
def add_doctor():
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Doctor(name, specialization) VALUES (%s, %s)",
        (name, specialization)
    )

    conn.commit()
    conn.close()

    print("✅ Doctor Added Successfully")


# View Doctors
def view_doctors():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Doctor")
    data = cursor.fetchall()

    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, Specialization: {row[2]}")

    conn.close()


# Book Appointment
def book_appointment():
    pid = int(input("Enter Patient ID: "))
    did = int(input("Enter Doctor ID: "))
    date = input("Enter Date (YYYY-MM-DD): ")
    time = input("Enter Time (HH:MM): ") + ":00"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Appointment(patient_id, doctor_id, date, time) VALUES (%s, %s, %s, %s)",
        (pid, did, date, time)
    )

    conn.commit()
    conn.close()

    print("✅ Appointment Booked")


# View Appointments (JOIN)
def view_appointments():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.name, d.name, a.date, a.time
        FROM Appointment a
        JOIN Patient p ON a.patient_id = p.patient_id
        JOIN Doctor d ON a.doctor_id = d.doctor_id
    """)

    data = cursor.fetchall()

    for row in data:
        print(f"Patient: {row[0]}, Doctor: {row[1]}, Date: {row[2]}, Time: {row[3]}")

    conn.close()


# Menu
def menu():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. Book Appointment")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            add_doctor()
        elif choice == '4':
            book_appointment()
        elif choice == '5':
            view_doctors()
        elif choice == '6':
            view_appointments()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice")


# Run Program
if __name__ == "__main__":
    menu()