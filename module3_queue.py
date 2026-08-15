# Module 3: Queue and Waiting Time Estimator

# Join the queue and update the queue number for the next customer
def join_queue(queue, table_size, next_queue_number):
    queue[table_size].append(next_queue_number) 

    print(f"Queue Number {next_queue_number} added to {table_size}-seater queue")
    return next_queue_number + 1 # this increments the next queue number for the next customer

# Calls next customer
# How this function works:
# This function gets called ONLY when someone of the same table size decides to leave the hawker 
# centre (from module 1 unoccupy_table)
# Due to the fact that this is a queue, the customers no longer have the choice to pick their
# desired zone, they shall just take the next available table that is of their table size.
# This function requires the zones dictionary and zone + table_size of the unoccupied table
# because it needs to change the dictionary when the next person comes in.

def call_next_customer(zones, zone, priority_queue, queue, table_size):

    if len(priority_queue[table_size]) == 0 and len(queue[table_size]) == 0: 
    # this would happen when the table_size was previously full and someone unoccupy the table,
    # causing this function to run.
    # but if there is no queue for that table size then we just do nothing.
        return
    elif len(priority_queue[table_size]) != 0:
        customer_number = priority_queue[table_size][0] # assigns the current customer to be called
        print(f"\nNow serving Priority Queue Number {customer_number}: Zone: {zone}, Table Size: {table_size}")
        priority_queue[table_size].pop(0)
        zones[zone][table_size] -= 1 
    else: 
        customer_number = queue[table_size][0] # assigns the current customer to be called
        print(f"\nNow serving Queue Number {customer_number}: Zone: {zone}, Table Size: {table_size}")
        queue[table_size].pop(0) 
        zones[zone][table_size] -= 1 

# this function is the first part to calculate the estimated waiting time
# it calculates the total number of tables per table size (regardless of zones)
# this function is used in pc_main.py
def count_table_type(max_tables):

    # Stores total number of each table type
    table_totals = {2: 0, 4: 0, 6: 0, 8: 0}

    # Go through every zone
    for zone in max_tables:
        # Go through every table type in the zone
        for table_size in max_tables[zone]:
            # Add the number of tables to the total
            table_totals[table_size] += max_tables[zone][table_size]
    return table_totals

# How this waiting time function works:
# Estimate how long it takes for a customer to eat.
# The customer queueing has to wait for (queuelength / total_tables_of_table_size) * avg_dining_duration
# Example:
# Let's say there is 10 tables for two, avg_dining_duration = 30 min
# If the queue is 10, then the 10th person would wait around (10 / 10) * 30 = 30 minutes
# We use queue_length as the customer's position since this function 
# runs right after they join the queue
def waiting_time(tables_per_table_type, priority_queue, queue, table_size):
    avg_dining_duration = 30 # how long a customer takes to eat in minutes
    queue_length = len(queue[table_size]) + len(priority_queue[table_size])
    total_tables_of_table_size = tables_per_table_type[table_size]
    estimated_waiting_time = (queue_length / total_tables_of_table_size) * avg_dining_duration
    estimated_waiting_time = round(estimated_waiting_time)
    print(f"Estimated waiting time: {estimated_waiting_time} minutes")

# This function allows a customer to leave the queue if they change their mind
def leave_queue(queue, priority_queue, table_size, queue_number):
    if queue_number in queue[table_size]:
        queue[table_size].remove(queue_number)
        print(f"Queue Number {queue_number} has left the {table_size}-seater queue")
    elif queue_number in priority_queue[table_size]:
        priority_queue[table_size].remove(queue_number)
        print(f"Priority Queue Number {queue_number} has left the {table_size}-seater priority queue")
    else:
        print(f"Queue Number {queue_number} not found in the queue.")