# Tests modules. Run code here to test and debug
import module1_tables
import module2_crowds
import module3_queue
# Functions from modules and required args
# Module 1:
#   display_tables -> requires zones dictionary
#   occupy_table -> zones dictionary, preferred zone and preferred table size
#   unoccupy_table -> zones dictionary, max_tables dictionary, zone, table_size, queue dictionary, priority queue dictionary
# Module 2:
#   occupancy_percentage -> max_tables dictionary, zones dictionary
#   crowd_indicator -> max_tables dictionary, zones dictionary
# Module 3:
#   join_queue -> queue dictionary, preferred table size and queue_numbers[table_size]  
#                 where queue_numbers[table_size] corresponds to next_queue_number
#   call_next_customer -> zones dictionary, zone of previous customer, priority_queue dictionary, queue dictionary, table_size
#   count_table_type -> max_tables dictionary
#   waiting_time -> tables_per_table_type dictionary, which is the return value of count_table_type,
#                   priority_queue dictionary, queue dictionary, table_size
# Module 5:
#   join_priority_queue -> priority_queue dictionary, preferred table size and queue_numbers[table_size]
#                          where queue_numbers[table_size] corresponds to next_queue_number


# How this works:
# Step 1: To test a function, look above for what variables are necessary 
#         (Copy paste the variables you need from main to here)
# Step 2: Run the function in the format <name_of_module>.<function>(args_necessary)
# Step 3: Once you are done testing, select your entire code and press ctrl / to comment everything
#         (This prevents code from overlapping)




########## START OF TESTS ##########
# MODULE 3: ZONES BUT EVERYTHING OCCUPIED:
# zones = {
#     "A": {2: 0, 4: 0, 6: 0, 8: 0},
#     "B": {2: 0, 4: 0, 6: 0, 8: 0},
#     "C": {2: 0, 4: 0, 6: 0, 8: 0}
# }

# # m3. join queue
# queue = {
#     2: [],
#     4: [],
#     6: [],
#     8: []
# }
# queue_numbers = {2: 201, 4: 401, 6: 601, 8: 801}

# idkwhatitreturns = module3_queue.join_queue(queue, 2, queue_numbers[2]) 
# print(f"The function join_queue returns {idkwhatitreturns}")