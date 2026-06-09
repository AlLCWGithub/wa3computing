import module1

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

# Sample testcases for module 1
module1.display_tables(zones)
print("\n")
module1.occupy_table(zones, "A", 4)
print("\n")
module1.display_tables(zones)
print("\n")
module1.unoccupy_table(zones, max_tables, "A", 4)