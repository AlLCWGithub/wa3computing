# Testcases for the functions:
# Format: <module>.<function>.<testcase number>
# Testcases: normal, boundary, error
# HOW TO USE:
# TEST ONE TESTCASE AT A TIME. COMMENT THE TEST CASE AFTER DONE USING CTRL /

import module1_tables as module1_tables
import module2_crowds as module2_crowds
import module3_queue as module3_queue
import module4_priority as module4_priority

# Original variables from main (overwrite them to test functions):
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

queue = {
    2: [],
    4: [],
    6: [],
    8: []
}

queue_numbers = {2: 201, 4: 401, 6: 601, 8: 801} 

tables_per_table_type = module3_queue.count_table_type(max_tables)

priority_queue = {
    2: [],
    4: [],
    6: [],
    8: []
}

########## START OF TESTS ##########
# 1.1 display_tables
# 1.1.1 Normal test case: Display tables with normal values
# module1_tables.display_tables(zones) 
# 1.1.2 Boundary test case: Display tables with all zero values
# zones_zero = {
#    "A": {2: 0, 4: 0, 6: 0, 8: 0},
#    "B": {2: 0, 4: 0, 6: 0, 8: 0},
#    "C": {2: 0, 4: 0, 6: 0, 8: 0}
# }
# module1_tables.display_tables(zones_zero)
# 1.1.3 Error test case: Display tables with invalid vacancy values (negative numbers)
# zones_invalid = {
#    "A": {2: -5, 4: -8, 6: -3, 8: -2},
#    "B": {2: -4, 4: -6, 6: -2, 8: -1},
#    "C": {2: -6, 4: -5, 6: -4, 8: -2} 
# }
# module1_tables.display_tables(zones_invalid)  
# 1.1.4 Error test case: Display tables with invalid vacancy values (non-integer)
# zones_invalid_non_integer = {
#    "A": {2: "1337", 4: "1000", 6: "10000", 8: 2},
#    "B": {2: 4, 4: "123131", 6: "123456", 8: 1},
#    "C": {2: 6, 4: "LOL", 6: "HAHA", 8: 2}
# }
# module1_tables.display_tables(zones_invalid_non_integer)  

# 1.2 occupy_table
# 1.2.1 Normal test case: Occupy a table with valid zone and table size
# module1_tables.occupy_table(zones, "A", 4)
# 1.2.2 Boundary test case: Occupy a table with the last available table
# module1_tables.occupy_table(zones, "B", 8)
# 1.2.3 Error test case: Occupy a table with an invalid zone
# module1_tables.occupy_table(zones, "D", 4)
# 1.2.4 Error test case: Occupy a table with an invalid table size
# module1_tables.occupy_table(zones, "A", 10)

# 1.3 unoccupy_table
# 1.3.1 Normal test case: Unoccupy a table with valid zone and table size
# zones = {
#    "A": {2: 5, 4: 7, 6: 3, 8: 2},
#    "B": {2: 4, 4: 6, 6: 2, 8: 0},
#    "C": {2: 6, 4: 5, 6: 4, 8: 2}
# }
# module1_tables.unoccupy_table(zones, max_tables, "A", 4, queue, priority_queue)
# 1.3.2 Boundary test case: Unoccupy a table with the last occupied table
# module1_tables.unoccupy_table(zones, max_tables, "B", 8, queue, priority_queue)
# 1.3.3 Error test case: Unoccupy a table that was already fully vacant
# zones = {
#    "A": {2: 5, 4: 8, 6: 3, 8: 2},
#    "B": {2: 4, 4: 6, 6: 2, 8: 1},
#    "C": {2: 6, 4: 5, 6: 4, 8: 2}
# }
# module1_tables.unoccupy_table(zones, max_tables, "B", 4, queue, priority_queue)
# 1.3.4 Error test case: Unoccupy a table with an invalid table size/zone
# module1_tables.unoccupy_table(zones, max_tables, "A", 10, queue, priority_queue)  

# 2.1 crowd_indicator/occupancy_percentage
# 2.1.1 Normal test case: Calculate crowd indicator with normal values
# zones = {
#    "A": {2: 5, 4: 7, 6: 3, 8: 2},
#    "B": {2: 4, 4: 6, 6: 2, 8: 0},
#    "C": {2: 6, 4: 5, 6: 4, 8: 2}
# }
# module2_crowds.crowd_indicator(max_tables, zones)
# 2.1.2 Boundary test case: Calculate crowd indicator with zero occupancy.
# module2_crowds.crowd_indicator(max_tables, zones)
# 2.1.3 Error test case: swap arguments
# zones = {
#    "A": {2: 5, 4: 7, 6: 3, 8: 2},
#    "B": {2: 4, 4: 6, 6: 2, 8: 0},
#    "C": {2: 6, 4: 5, 6: 4, 8: 2}
# }
# module2_crowds.crowd_indicator(zones, max_tables)

# 2.2 crowd_indicator - check the returned value as well
# 2.2.1 Normal test case: returns LOW
# zones = {
#    "A": {2: 5, 4: 7, 6: 3, 8: 2},
#    "B": {2: 4, 4: 6, 6: 2, 8: 0},
#    "C": {2: 6, 4: 5, 6: 4, 8: 2}
# }
# print(f"returned value: {module2_crowds.crowd_indicator(max_tables, zones)}")
# 2.2.2 Normal test case: returns CROWDED
# zones = {
#    "A": {2: 5, 4: 1, 6: 1, 8: 1},
#    "B": {2: 1, 4: 1, 6: 2, 8: 0},
#    "C": {2: 1, 4: 1, 6: 4, 8: 2}
# }
# print(f"returned value: {module2_crowds.crowd_indicator(max_tables, zones)}")
# 2.2.3 Boundary test case: returns FULL
# zones = {
#    "A": {2: 0, 4: 0, 6: 0, 8: 0},
#    "B": {2: 0, 4: 0, 6: 0, 8: 0},
#    "C": {2: 0, 4: 0, 6: 0, 8: 0}
# }
# print(f"returned value: {module2_crowds.crowd_indicator(max_tables, zones)}")

# 3.1 join_queue
# 3.1.1 Normal test case: add a customer to queue[2] when queue is empty and should return the next customer's number
# print(f"returned: {module3_queue.join_queue(queue, 2, queue_numbers[2])}")
# 3.1.2 Error test case: add a customer to a non-existent queue: e.g. queue[10]
# print(f"returned: {module3_queue.join_queue(queue, 10, queue_numbers[10])}")

# 3.2 call_next_customer
# 3.2.1 Normal test case: both priority q and normal q have people -> priority served first
# queue = {
#     2: [201, 202, 203, 206],
#     4: [],
#     6: [],
#     8: []
# }

# priority_queue = {
#     2: [204, 205],
#     4: [],
#     6: [],
#     8: []
# }
# module3_queue.call_next_customer(zones, "A", priority_queue, queue, 2)
# 3.2.2 Boundary test case: no queue at all.
# queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }

# priority_queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }
# module3_queue.call_next_customer(zones, "A", priority_queue, queue, 2)
# it returned nothing so i could not screenshot any output
# 3.2.3 Error test case: zone or table size invalid
# module3_queue.call_next_customer(zones, "D", priority_queue, queue, 2) # returned nothing

# 3.3 waiting_time
# 3.3.1 normal test case: valid queue and priority queue
# queue = {
#     2: [201, 202, 203, 206],
#     4: [],
#     6: [],
#     8: []
# }

# priority_queue = {
#     2: [204, 205],
#     4: [],
#     6: [],
#     8: []
# }
# module3_queue.waiting_time(tables_per_table_type, priority_queue, queue, 2)
# expected output: 6 ppl in queue, total of 15 tables for 2, so 12 minutes
# 3.3.2 boundary test case: no queue
# queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }

# priority_queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }
# module3_queue.waiting_time(tables_per_table_type, priority_queue, queue, 2)
# 3.3.3 error test case: zero tables in the hawker center i.e. divide by zero
# queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }

# priority_queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }
# module3_queue.waiting_time({2: 0, 4: 0, 6: 0, 8: 0}, priority_queue, queue, 2)

# 3.4 Leave queue
# 3.4.1 normal: remove queue number from queue
# queue = {
#     2: [201, 202, 203, 206],
#     4: [],
#     6: [],
#     8: []
# }

# priority_queue = {
#     2: [204, 205],
#     4: [],
#     6: [],
#     8: []
# }
# module3_queue.leave_queue(queue, priority_queue, 2, 202)
# 3.4.2 error: leave queue that is empty/not found
# queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }

# priority_queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }
# module3_queue.leave_queue(queue, priority_queue, 2, 202)

