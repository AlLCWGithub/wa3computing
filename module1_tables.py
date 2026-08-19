# Module 1: Table Counter and Table Zones

from module3_queue import call_next_customer

# Display the number of tables and calculate the "best" zone
def display_tables(zones):

    best_zone_name = "" 
    best_zone_count = 0

    total = 0 

    # These nested for loops calculate the "best" zone
    for zone in zones:
        zone_total = 0 
        
        for table_size in zones[zone]:
           
            zone_total += zones[zone][table_size]
            
        print(f"Zone {zone}: {zone_total} tables available") # Print the number of vacant seats for each zone.
                                                             # e.g. Zone A: 10 tables available
                                                             #      Zone B: 20 tables available
       

        total += zone_total 

        # this replicates a max() function to find the max number of vacant seats
        if zone_total > best_zone_count: # if the current number of vacant seats > current best,
            best_zone_count = zone_total # set the best to the current number of vacant seats,
            best_zone_name = zone  # and set the best zone to the corresponding zone.

    print(f"Total available tables: {total} ")
    print(f"Recommended Zone: {best_zone_name}")

# Occupy a table
# The function requires the zones dictionary, the user's preferred zone and their table size.
def occupy_table(zones, zone, table_size): 
    # These if-statements prevents the user from trying to trick the system
    if zone not in zones:
        print("Invalid zone.\n")
        return 
    if table_size not in zones[zone]:
        print("Invalid table size.\n")
        return 

    # Check if table size has vacancy
    if zones[zone][table_size] > 0: 
        zones[zone][table_size] -= 1 
        print(f"Welcome into Smart Hawker Centre! \nZone: {zone} \nTable size: {table_size}") 
    else:
        print(f"No table for {table_size} available in zone {zone}.") 

# Unoccupy a table
# The function requires the zones dictionary, the fixed max tables dictionary, 
# the customer's table details (zone + table size), and queue dictionary (for module3)
def unoccupy_table(zones, max_tables, zone, table_size, queue, priority_queue):
    # These if-statements prevents the user from trying to trick the system
    if zone not in zones:
        print("Invalid zone.")
        return
    if table_size not in zones[zone]:
        print("Invalid table size.")
        return

    # Ensure count never exceeds original amount
    if zones[zone][table_size] < max_tables[zone][table_size]: 
        zones[zone][table_size] += 1 
        print("Thank you for visiting Smart Hawker Centre!")

        # MODULE 3: if the table was previously full but now is vacant, call the next number.
        if zones[zone][table_size] == 1: 
            call_next_customer(zones, zone, priority_queue, queue, table_size)
            print(f"Zone: {zone}, Table Size: {table_size}")
    else:
        print(f"All {table_size}-person tables in zone {zone} are already empty. Please try again!") # otherwise print error