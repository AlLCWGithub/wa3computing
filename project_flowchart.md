# Smart Hawker Centre – Module Flowchart Summary (Problem Decomposition)
This is the flowcharts for each function of the program.

## Module 1: Table Counter and Table Zones

### display_tables(zones)

```
START
  |
  v
Variables for best zone and total
  |
  v
For each zone:
   - add tables for each table size
   - print available tables in that zone
   - add zone total to overall total
   - compare zone total with current best zone
  |
  v
Display:
   - Total available tables
   - Recommended zone
END
```

### occupy_table(zones, zone, table_size)

```
START
  |
  v
Check zone exists?
  |-- No --> print invalid zone --> END
  |
  v
Check table size exists in selected zone?
  |-- No --> print invalid table size --> END
  |
  v
Is table count > 0?
  |-- Yes --> reduce count by 1 --> print welcome
  |-- No --> print no table available
END
```

### unoccupy_table(zones, max_tables, zone, table_size, queue, priority_queue)

```
START
  |
  v
Check zone exists?
  |-- No --> print invalid zone --> END
  |
  v
Check table size exists?
  |-- No --> print invalid table size --> END
  |
  v
Is current count below maximum allowed?
  |-- Yes --> increase available tables by 1 --> print thank-you
             --> if table was previously full, call next customer
  |-- No --> print all tables already empty
END
```

---

## Module 2: Crowd Level Indicators

### occupancy_percentage(max_tables, zones)

```
START
  |
  v
Count total possible tables from max_tables
  |
  v
Count current available tables from zones
  |
  v
occupied_tables = total tables - available tables
  |
  v
percentage = (occupied_tables / total tables) * 100
  |
  v
Round the percentage
  |
  v
Return percentage
END
```

### crowd_indicator(max_tables, zones)

```
START
  |
  v
Get percentage from occupancy_percentage
  |
  v
Print occupancy percentage
  |
  v
if percentage <= 40:
    return LOW
elif percentage <= 80:
    return CROWDED
else:
    return FULL
END
```

---

## Module 3: Queue and Waiting Time Estimator

### join_queue(queue, table_size, next_queue_number)

```
START
  |
  v
Add queue number to queue[table_size]
  |
  v
Print queue confirmation
  |
  v
Return next_queue_number + 1
END
```

### call_next_customer(zones, zone, priority_queue, queue, table_size)

```
START
  |
  v
Are priority and normal queues empty for this table size?
  |-- Yes --> do nothing --> END
  |
  v
Is priority queue not empty?
  |-- Yes --> serve first priority customer
             remove from priority_queue
             reduce available table count by 1
  |-- No --> serve first normal customer
             remove from queue
             reduce available table count by 1
END
```

### count_table_type(max_tables)

```
START
  |
  v
Create table_totals = {2:0, 4:0, 6:0, 8:0}
  |
  v
For each zone and table size:
    add max_tables count to the matching table size total
  |
  v
Return table_totals
END
```

### waiting_time(tables_per_table_type, priority_queue, queue, table_size)

```
START
  |
  v
Set average dining duration = 30 minutes
  |
  v
queue_length = normal queue length + priority queue length
  |
  v
estimated_waiting_time = (queue_length / total tables of that size) * 30
  |
  v
Round waiting time
  |
  v
Print estimated waiting time
END
```

### leave_queue(queue, priority_queue, table_size, queue_number)

```
START
  |
  v
Search normal queue for queue_number
  |-- Found --> remove from queue --> print message
  |
  v
If not found, search priority queue
  |-- Found --> remove from priority queue --> print message
  |-- Not found --> print queue number not found
END
```

---

## Module 4: Priority Queueing

### join_priority_queue(priority_queue, table_size, next_queue_number)

```
START
  |
  v
Add next queue number to priority_queue[table_size]
  |
  v
Print priority queue confirmation
  |
  v
Return next queue number + 1
END
```

### priority_waiting_time(tables_per_table_type, priority_queue, table_size)

```
START
  |
  v
Set average dining duration = 30 minutes
  |
  v
queue_length = length of priority_queue[table_size]
  |
  v
estimated_waiting_time = (queue_length / total tables of that size) * 30
  |
  v
Round value
  |
  v
Print estimated waiting time
END
```
