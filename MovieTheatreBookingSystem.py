total_capacity = 350
seats_sold = 0
total_bookings = 0
rejected_bookings = 0

print("------------Movie Theatre Booking System----------------")

while seats_sold < total_capacity:
    
    # Get number of tickets
    try:
        num_tickets = int(input("\nEnter number of tickets or 0 to exit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Exit condition
    if num_tickets == 0:
        break

    # Validate ticket range
    if num_tickets < 1 or num_tickets > 15:
        print("Invalid booking: You can only book 1-15 tickets.")
        continue

    # Check if enough seats are available
    if seats_sold + num_tickets > total_capacity:
        print(f"BOOKING REJECTED - Not enough seats. Remaining: {total_capacity - seats_sold}")
        rejected_bookings += 1
        continue

    # Age validation
    is_valid_age = True
    print(f"Enter ages for {num_tickets} person(s):")

    for i in range(num_tickets):
        age = int(input(f"Age of person {i+1}: "))
        if age < 12:
            is_valid_age = False

    # Process booking result
    if is_valid_age:
        seats_sold += num_tickets
        total_bookings += 1
        print(f"BOOKING CONFIRMED - {num_tickets} tickets")
    else:
        rejected_bookings += 1
        print("BOOKING REJECTED - Age restriction (12+ only)")

# Final Report
print("\n------------Final Report------------")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {seats_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {total_capacity - seats_sold}")