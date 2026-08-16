import module1_tables as module1_tables
import module2_crowds as module2_crowds
import module3_queue as module3_queue
import module4_priority as module4_priority
from serial_connection import SerialConnection
import time

connection = SerialConnection()

# Variables

secretkey = "secretkey" # this is a secret key that employees can use to close the application. It is not meant for customers to know.

## FOR TESTING OF MODULE 3, EVERY ZONE IS FULLY OCCUPIED SO THE USER HAS TO QUEUE.
# zones = {
#     "A": {2: 0, 4: 0, 6: 0, 8: 0},
#     "B": {2: 0, 4: 0, 6: 0, 8: 0},
#     "C": {2: 0, 4: 0, 6: 0, 8: 0}
# }

zones = {
   "A": {2: 5, 4: 8, 6: 3, 8: 2},
   "B": {2: 4, 4: 6, 6: 2, 8: 1},
   "C": {2: 6, 4: 5, 6: 4, 8: 2}
}

# Pengu's Hawker Centre Prototype Box
# zones = {
#    "A": {2: 0, 4: 0, 6: 2, 8: 0},
#    "B": {2: 4, 4: 1, 6: 0, 8: 0},
#    "C": {2: 2, 4: 0, 6: 0, 8: 1}
#}

max_tables = {
    "A": {2: 5, 4: 8, 6: 3, 8: 2},
    "B": {2: 4, 4: 6, 6: 2, 8: 1},
    "C": {2: 6, 4: 5, 6: 4, 8: 2}
}

# Module 3: Queue: Variables
# Dictionary to store the queue for each table size. Key: table size, Value: list of queue numbers
queue = {
    2: [],
    4: [],
    6: [],
    8: []
}
# queue numbers start from 201 for 2-person tables, 401 for 4-person tables, 601 for 6-person tables, and 801 for 8-person tables.
queue_numbers = {2: 201, 4: 401, 6: 601, 8: 801} 

# Module 3: Estimate waiting time
    # tables_per_table_type is a dictionary that stores the number of tables per table type. 
    # this tells me the number of tables per table type, so can estimate how long to wait
    # example of this dictionary could be: {2: 10, 4: 15 ...} i.e. there is 10 tables of 2, 15 tables of 4...
    # This was done so that if the hawker centre layout is changed, we do not hard code the number of tables per table type.
tables_per_table_type = module3_queue.count_table_type(max_tables)

# Module 4: Priority Queue: Variables
priority_queue = {
    2: [],
    4: [],
    6: [],
    8: []
}

# variables for input validation
validzones = ["A", "B", "C"]
validtablesizes = ["2", "4", "6", "8"]


# MAIN LOOP OF THE PROGRAM
# How does this main loop work:
# Step 1. The user is prompted to enter an option (1, 2, 3, 4)
# Step 2. If the user enters 1 or 2:
# a. Display vacancy information (Module 1 and 2)
# b. Ask for input for table size and zone 
# c. If the table is available, occupy the table. (Module 1)
# d. If the table is not available, ask if they want to queue.
# e. If they want to queue, add them to the queue and estimate waiting time. (Module 3)
# Step 3: If the user enters 3:
# a. Ask for input for table size and zone
# b. Unoccupy the table (Module 1) 
# c. Call the next customer in the queue if there is a queue (Module 1 and 3)
# Step 4: If the user enters 4:
# a. Ask for input for table size and queue number
# b. Remove them from the queue (Module 3)

while True:
    # welcome message
    print("\nWelcome to Pengu Hawker Centre!")
    while (enter_or_exit := input("Please pick an option: \n\
(1) Enter \n\
(2) Enter as Priority \n\
(3) Exit \n\
(4) Leave Queue \n")) not in ("1", "2", "3", "4", secretkey): 
        print("Invalid Input") 
# How the walrus operator (:=) works
# Assigns enter_or_exit to input, 
# while also checking if it is in a tuple of ("1", "2", "3", "4", secretkey). 
# It will keep printing Invalid Input until the user enters a valid input.

    # ENTER HAWKER CENTRE
    if enter_or_exit == "1" or enter_or_exit == "2":
        module1_tables.display_tables(zones)
        crowd_level = module2_crowds.crowd_indicator(max_tables, zones)
        connection.send("CROWD", crowd_level) # send the crowd level to microbit to display on LED

        while ((preferred_zone := input("Enter your preferred zone (A, B, C): ").strip().upper()) not in validzones):
            print("Invalid Zone!")
        while ((table_size := input("Enter your table size (2, 4, 6, 8): ").strip()) not in validtablesizes):
            print("Invalid Table Size")
        table_size = int(table_size)

        # If the table size is available, occupy the table
        if zones[preferred_zone][table_size] != 0: 
            module1_tables.occupy_table(zones, preferred_zone, table_size)

        # otherwise it means that the table size they want is already occupied.
        else:
            print(f"\nThere is no vacant {table_size}-person tables in zone {preferred_zone}.")
            print(f"Current Queue For Your Table Size: {len(queue[table_size])}\n")

            # ask if they wanna queue or no
            wannaqueue = input("Do you want to queue? (Y/N)")
            if wannaqueue == "Y":
                if enter_or_exit == "1": # if in normal queue:
                    print(f"Your queue number: {queue_numbers[table_size]}")
                    # queue_numbers[table_size] is the next queue number
                    # the module join_queue increments the queue number
                    queue_numbers[table_size] = module3_queue.join_queue(queue, table_size, queue_numbers[table_size]) 
                    # Print waiting time
                    module3_queue.waiting_time(tables_per_table_type, priority_queue, queue, table_size)

                else: # if in priority queue:
                    print(f"Your queue number: {queue_numbers[table_size]}")
                    # the function join_priority_queue increments the queue number
                    queue_numbers[table_size] = module4_priority.join_priority_queue(priority_queue, table_size, queue_numbers[table_size])
                    # Print waiting time
                    module4_priority.priority_waiting_time(tables_per_table_type, priority_queue, table_size)

            else: # if they dont wanna queue
                print("Ok you are not in the queue. Sorry for the inconvenience as you'll have to eat somewhere else. :(")

    # EXIT HAWKER CENTRE
    elif enter_or_exit == "3":
        while ((zone := input("Enter the zone you were at (A, B, C): ").strip().upper()) not in validzones):
            print("Invalid Zone!")
        while ((table_size := input("Enter your table size (2, 4, 6, 8): ").strip()) not in validtablesizes):
            print("Invalid Table Size!")
        table_size = int(table_size)
        module1_tables.unoccupy_table(zones, max_tables, zone, table_size, queue, priority_queue)

    # LEAVE QUEUE
    elif enter_or_exit == "4":
        while ((table_size := input("Enter your table size (2, 4, 6, 8): ").strip()) not in validtablesizes):
            print("Invalid Table Size!")
        table_size = int(table_size)
        queue_number = input("Enter your queue number: ") # Input validation is unnecessary as the function leave_queue already checks if the queue number is in the queue or not.
        queue_number = int(queue_number)
        module3_queue.leave_queue(queue, priority_queue, table_size, queue_number)

    elif enter_or_exit == secretkey: # this is for employees when they close the application.
        print("Store closed.")
        break

    time.sleep(5) # this is to give the user time to read the output before clearing the screen