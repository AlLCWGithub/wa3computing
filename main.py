import module1_tables
import module2_crowds
import module3_queue
## MY EYES HURT READING THIS CODE HELP
## CURRENT PROGRESS: 
## MODULE 1 AND 2 ARE MOSTLY COMPLETE.
## NEED TO FIX THE USER INTERFACE A BIT MESSY

# Variables
secretkey = "secretkey"

## FOR TESTING OF MODULE 3, EVERY ZONE IS FULLY OCCUPIED SO THE USER HAS TO QUEUE.
zones = {
    "A": {2: 0, 4: 0, 6: 0, 8: 0},
    "B": {2: 0, 4: 0, 6: 0, 8: 0},
    "C": {2: 0, 4: 0, 6: 0, 8: 0}
}
# actual zones dictionary
# zones = {
#    "A": {2: 5, 4: 8, 6: 3, 8: 2},
#    "B": {2: 4, 4: 6, 6: 2, 8: 1},
#    "C": {2: 6, 4: 5, 6: 4, 8: 2}
#}

max_tables = {
    "A": {2: 5, 4: 8, 6: 3, 8: 2},
    "B": {2: 4, 4: 6, 6: 2, 8: 1},
    "C": {2: 6, 4: 5, 6: 4, 8: 2}
}

# For module 3, queue
queue = {
    2: [],
    4: [],
    6: [],
    8: []
}
queue_numbers = {2: 201, 4: 401, 6: 601, 8: 801}

# this tells me the number of tables per table type, so can estimate how long to wait
# example of this dictionary could be: {2: 10, 4: 15 ...} i.e. there is 10 tables of 2, 15 tables of 4...
tables_per_table_type = module3_queue.count_table_type(max_tables)

while True:
    # welcome message
    print("\nWelcome to Smart Hawker Centre!")
    while (enter_or_exit := input("Please pick an option: \n\
(1) Enter \n\
(2) Exit \n")) not in ("1", "2", secretkey):
        print("Invalid Input") # Using the walrus operator, I can assign enter_or_exit to input, before checking if it is in a tuple of ("1", "2")
    ## FOR NOW, WE ASSUME THE TABLES WILL NEVER GO EMPTY 
    ## WILL BE FIXED IN MODULE 3.
    if enter_or_exit == "1":
        # Display the crowd indicator and ask them for their preferred zone
        module1_tables.display_tables(zones)
        module2_crowds.crowd_indicator(max_tables, zones)
        preferred_zone = input("Enter your preferred zone (A, B, C): ")
        table_size = int(input("Enter your table size (2, 4, 6, 8): "))
        if zones[preferred_zone][table_size] != 0:
            module1_tables.occupy_table(zones, preferred_zone, table_size)
        else:
            # otherwise it means that the table size they want is already occupied.
            print(f"There is no vacant {table_size}-person tables in zone {preferred_zone}.\n")
            print(f"Current Queue For Your Table Size: {len(queue[table_size])}\n")
            # ask if they wanna queue or no
            wannaqueue = input("Do you want to queue? (Y/N)")
            if wannaqueue == "Y":
                print(f"Your queue number: {queue_numbers[table_size]}")
                queue_numbers[table_size] = module3_queue.join_queue(queue, table_size, queue_numbers[table_size])
                module3_queue.waiting_time(tables_per_table_type, queue, table_size)
            else:
                print("Ok you are not in the queue. Sorry for the inconvenience as you'll have to eat somewhere else. :(")
                
    elif enter_or_exit == "2":
        zone = input("Enter the zone you were at (A, B, C): ")
        table_size = int(input("Enter your table size (2, 4, 6, 8): "))
        module1_tables.unoccupy_table(zones, max_tables, zone, table_size, queue)
    elif enter_or_exit == secretkey: # this is for employees when they close the application.
        print("Store closed.")
        break
    else:
        print("Invalid Option!")              