# Module 1: Table Counter and Table Zones

# Calculate available tables (used to display number of tables)
def total_available_tables(zones):

    total = 0

    for zone in zones:

        for table_size in zones[zone]:

            # Add available tables to total
            total += zones[zone][table_size]

    return total

# Display the number of tables 
def display_tables(zones):

    print("Welcome to Smart Hawker Centre")

    best_zone_name = ""
    best_zone_count = 0

    for zone in zones:

        zone_total = 0

        for table_size in zones[zone]:

            # Sum all available tables in this zone
            zone_total += zones[zone][table_size]

        print(f"Zone {zone}: {zone_total} tables available")

        if zone_total > best_zone_count:
            best_zone_count = zone_total
            best_zone_name = zone

    total = total_available_tables(zones)
    print(f"Total available tables: {total} ")

    print(f"Recommended Zone: {best_zone_name}")

# Occupy a table
def occupy_table(zones, zone, table_size):

    if zone not in zones:

        print("Invalid zone.")
        return

    if table_size not in zones[zone]:

        print("Invalid table size.")
        return

    # First select the zone
    # Then select the table size inside that zone
    # Example:
    # zones["A"][4]
    # means available 4-seater tables in Zone A

    if zones[zone][table_size] > 0:

        zones[zone][table_size] -= 1

        print(f"Customer seated at {table_size}-seater in Zone {zone}")

    else:

        print(f"No {table_size}-seater available in zone {zone}")

# Unoccupy a table
def unoccupy_table(zones, max_tables, zone, table_size):

    if zone not in zones:

        print("Invalid zone.")
        return

    if table_size not in zones[zone]:

        print("Invalid table size.")
        return

    # Ensure count never exceeds original amount

    if zones[zone][table_size] < max_tables[zone][table_size]:

        zones[zone][table_size] += 1

        print(f"{table_size}-seater in zone {zone} is now vacant")

    else:

        print("Error: Count cannot exceed maximum.")