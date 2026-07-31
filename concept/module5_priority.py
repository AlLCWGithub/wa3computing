# Module 5: Priority Queueing
# Module 5 extends the queueing system by introducing a priority queue.
# Eligible users are placed into a separate queue.
# When a table becomes available, the system serves customers from the priority queue before the normal queue.


# Similar function to join_queue in module 3, but its a priority queue
# (i.e. when someone unoccupies table, the priority queue is checked before the normal queue)
def join_priority_queue(priority_queue, table_size, next_queue_number):
    priority_queue[table_size].append(next_queue_number) # append the queue number into the queue dictionary

    print(f"Queue Number {next_queue_number} added to {table_size}-seater priority queue")
    return next_queue_number + 1 # this increments the next queue number for the next customer

def priority_waiting_time(tables_per_table_type, priority_queue, table_size):
    avg_dining_duration = 30 # how long a customer takes to eat in minutes
    queue_length = len(priority_queue[table_size])
    total_tables_of_table_size = tables_per_table_type[table_size]
    estimated_waiting_time = (queue_length / total_tables_of_table_size) * avg_dining_duration
    estimated_waiting_time = round(estimated_waiting_time)
    print(f"Estimated waiting time: {estimated_waiting_time} minutes")
