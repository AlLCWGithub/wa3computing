import module1_tables
import module2_crowds
import module3_queue
import module5_priority
## MY EYES HURT READING THIS CODE HELP
## CURRENT PROGRESS: 
## PROBLEM 1: THE DISPLAY TABLES DO NOT DISPLAY THE INDIVIDUAL TABLES VACANCY, ONLY THE 
## TOTAL NUMBER OF TABLES IN EACH ZONE IS DISPLAYED.
## IF THE USER PICKS THE WRONG ZONE WHERE THERE IS NO VACANCY FOR THEIR TABLE SIZE, THEY ARE FORCED
## TO QUEUE FOR NO REASON, EVEN IF ANOTHER ZONE HAS AVAILABILITY.
## HOW TO WORKAROUND THIS:
## OPTION 1: JUST PRINT EVERYTHING
## PRINT THE TOTAL NUMBER OF TABLES OF A ZONE, THEN PRINT THE VACANCY FOR EACH TABLE TYPE
## BUT THIS RESULTS IN LIKE 20 LINES OF OUTPUT.
## OPTION 2: LET THE USER PICK PREFFERED ZONE, THEN SHOW THEM THE VACANCY FOR EACH TABLE TYPE
##           FOR THAT ZONE ONLY.
## AND THERE THEY CAN INPUT THEIR TABLE SIZE OR GO BACK TO THE FRONT PAGE
## LESS OUTPUT BUT MEANS MORE TEDIOUS FOR THE USER

## PROBLEM 2: INPUT VALIDATION.
## ONLY THE FIRST INPUT HAS INPUT VALIDATION BUT THE NEXT PART OF PREFERRED ZONE AND TABLE SIZE
## DOESNT HAVE INPUT VALIDATION. AND FOR PROBLEM 1 IF WE CHOOSE OPTION 2 
## THATS EVEN MORE INPUT VALIDATON.
## I MEAN WE COULD KEEP DOING WALRUS OPERATOR BUT IT CAN MAKE THE CODE EVEN MORE CONFUSING...

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

# Module 5: Priority Queue
priority_queue = {
    2: [],
    4: [],
    6: [],
    8: []
}

while True:
    # welcome message
    print("\nWelcome to Smart Hawker Centre!")
    while (enter_or_exit := input("Please pick an option: \n\
(1) Enter \n\
(2) Enter Priority Queue \n\
(3) Exit \n\
(4) Leave Queue \n")) not in ("1", "2", "3", "4", secretkey): # IGNORE OPTION 4 ONLY USED IN MODULE 6
        print("Invalid Input") # Using the walrus operator, I can assign enter_or_exit to input, 
                               # before checking if it is in a tuple of ("1", "2")

    if enter_or_exit == "1" or enter_or_exit == "2":
        # Display the tables information and crowd indicator and ask them for their preferred zone
        module1_tables.display_tables(zones)
        module2_crowds.crowd_indicator(max_tables, zones)
        preferred_zone = input("Enter your preferred zone (A, B, C): ")
        table_size = int(input("Enter your table size (2, 4, 6, 8): "))

        if zones[preferred_zone][table_size] != 0: # if there is vacancy for that
            module1_tables.occupy_table(zones, preferred_zone, table_size)

        else:
            # otherwise it means that the table size they want is already occupied.
            print(f"\nThere is no vacant {table_size}-person tables in zone {preferred_zone}.")
            print(f"Current Queue For Your Table Size: {len(queue[table_size])}\n")

            # ask if they wanna queue or no
            wannaqueue = input("Do you want to queue? (Y/N)")
            if wannaqueue == "Y":
                if enter_or_exit == "1": # if in normal queue:
                    print(f"Your queue number: {queue_numbers[table_size]}")
                    # the argument queue_numbers[table_size] is essentially the next queue number
                    queue_numbers[table_size] = module3_queue.join_queue(queue, table_size, queue_numbers[table_size]) 
                    module3_queue.waiting_time(tables_per_table_type, priority_queue, queue, table_size)

                else: # if in priority queue:
                    print(f"Your queue number: {queue_numbers[table_size]}")
                    queue_numbers[table_size] = module5_priority.join_priority_queue(priority_queue, table_size, queue_numbers[table_size])
                    module5_priority.priority_waiting_time(tables_per_table_type, priority_queue, table_size)

            else: # if they dont wanna queue
                print("Ok you are not in the queue. Sorry for the inconvenience as you'll have to eat somewhere else. :(")


    elif enter_or_exit == "3":
        zone = input("Enter the zone you were at (A, B, C): ")
        table_size = int(input("Enter your table size (2, 4, 6, 8): "))
        module1_tables.unoccupy_table(zones, max_tables, zone, table_size, queue, priority_queue)


    elif enter_or_exit == secretkey: # this is for employees when they close the application.
        print("Store closed.")
        break