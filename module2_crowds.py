# Module 2: Crowd Level Indicators

# This function calculates the occupancy percentage of tables
def occupancy_percentage(max_tables, zones):
    total = 0

    for zone in max_tables:
        for table_size in max_tables[zone]:
            total += max_tables[zone][table_size]

    total_available = 0

    for zone in zones:
        for table_size in zones[zone]:
            total_available += zones[zone][table_size]

    # Calculate the percentage occupied
    occupied_tables = total - total_available
    percentage = (occupied_tables / total) * 100 # convert to percentage
    percentage = round(percentage) # round the percentage to nearest integer
    return percentage

# Display crowd information -> print the crowd info + LED display on microbit
def crowd_indicator(max_tables, zones):
    percentage = occupancy_percentage(max_tables, zones)
    print(f"Occupancy: {percentage}%")

    # LED displays
    if percentage <= 40:
        return "LOW"
    
    elif percentage <= 80:
        return "CROWDED"
    
    else:
        return "FULL"
