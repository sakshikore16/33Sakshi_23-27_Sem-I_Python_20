# 16. Build a hotel reservation system with classes 
# for rooms, guests, and reservations.
# Implement methods for checking room availability, 
# booking rooms, and generating invoices.

class Room:
    def __init__(self, number, capacity, rate):
        self.number, self.capacity, self.rate, self.reserved = number, capacity, rate, False

    def check_availability(self):
        return not self.reserved

    def book_room(self):
        if not self.reserved:
            self.reserved = True
            return True
        return False


class Guest:
    def __init__(self, name, email, phone):
        self.name, self.email, self.phone = name, email, phone


class Reservation:
    def __init__(self, guest, room, nights):
        self.guest, self.room, self.nights = guest, room, nights

    def generate_invoice(self):
        total_cost = self.room.rate * self.nights
        return f"\nInvoice for {self.guest.name}:\nRoom Number: {self.room.number}\n" \
               f"Number of Nights: {self.nights}\nTotal Cost: ${total_cost}"


rooms = [Room("101", 2, 100), Room("102", 4, 150), Room("103", 1, 80)]

guest = Guest(input("Enter your name: "), input("Enter your email: "), input("Enter your phone number: "))

while True:
    print("\nHotel Reservation System")
    print("1. Check Room Availability")
    print("2. Book a Room")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        room_number = input("Enter room number to check availability: ")
        room_found = next((room for room in rooms if room.number == room_number), None)
        print(f"Room {room_number} is {'available' if room_found and room_found.check_availability() else 'unavailable'}.")

    elif choice == "2":
        room_number = input("Enter room number to book: ")
        room_found = next((room for room in rooms if room.number == room_number), None)
        if room_found and room_found.book_room():
            nights = int(input("Enter the number of nights: "))
            reservation = Reservation(guest, room_found, nights)
            print(f"Room {room_number} booked successfully!\n{reservation.generate_invoice()}")
        else:
            print(f"Room {room_number} is unavailable. Please choose another room.")

    elif choice == "3":
        print("Exiting Hotel Reservation System. Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
