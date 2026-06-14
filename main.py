import module1_tables
import module2_crowds
## MY EYES HURT READING THIS CODE HELP
## CURRENT PROGRESS: 
## MODULE 1 AND 2 ARE MOSTLY COMPLETE.
## NEED TO FIX THE USER INTERFACE A BIT MESSY
secretkey = "secretkey"
zones = {
    "A": {2: 5, 4: 8, 6: 3, 8: 2},
    "B": {2: 4, 4: 6, 6: 2, 8: 1},
    "C": {2: 6, 4: 5, 6: 4, 8: 2}
}

max_tables = {
    "A": {2: 5, 4: 8, 6: 3, 8: 2},
    "B": {2: 4, 4: 6, 6: 2, 8: 1},
    "C": {2: 6, 4: 5, 6: 4, 8: 2}
}

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
        module1_tables.occupy_table(zones, preferred_zone, table_size)
    elif enter_or_exit == "2":
        zone = input("Enter the zone you were at (A, B, C): ")
        table_size = int(input("Enter your table size (2, 4, 6, 8): "))
        module1_tables.unoccupy_table(zones, max_tables, zone, table_size)
    elif enter_or_exit == secretkey: # this is for employees when they close the application.
        print("Store closed.")
        break
    else:
        print("Invalid Option!")              