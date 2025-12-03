"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

masoko_data_handler.py
Module for reading and processing Lake Masoko geochemical data.
Provides functions to load, filter, and query climate data from 1511-2002 AD.
"""

import json


def read_data(filename="data.json"):
    """
    Read Lake Masoko geochemical data from JSON file.
    
    :param filename: Path to the JSON data file (default: "data.json")
    :return: List of dictionaries containing geochemical measurements
    """
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data


def get_data_by_year(data, year):
    """
    Find the data record closest to a given year.
    
    :param data: List of data dictionaries from read_data()
    :param year: Year to search for (AD)
    :return: Dictionary with data for the closest year, or None if not found
    """
    if not data:
        return None
    
    # Find the record with the closest year
    closest_record = min(data, key=lambda x: abs(x["Age (AD)"] - year))
    return closest_record


def get_year_range(data):
    """
    Get the range of years available in the dataset.
    
    :param data: List of data dictionaries from read_data()
    :return: Tuple of (min_year, max_year)
    """
    if not data:
        return (0, 0)
    
    years = [record["Age (AD)"] for record in data]
    return (min(years), max(years))


def get_value_range(data, key):
    """
    Get the range of values for a specific measurement.
    
    :param data: List of data dictionaries from read_data()
    :param key: The measurement key (e.g., "Fe/Ti", "Si/Ti", "MagSus (m3/kg)")
    :return: Tuple of (min_value, max_value), handles missing data marked as "-"
    """
    if not data:
        return (0, 0)
    
    # Filter out missing values (marked as "-")
    values = [record[key] for record in data 
              if record[key] != "-" and isinstance(record[key], (int, float))]
    
    if not values:
        return (0, 0)
    
    return (min(values), max(values))


def normalize_value(value, min_val, max_val):
    """
    Normalize a value to range [0, 1].
    
    :param value: The value to normalize
    :param min_val: Minimum value in range
    :param max_val: Maximum value in range
    :return: Normalized value between 0 and 1
    """
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)


def main():
    """Test function for the data handler module."""
    # Load the data
    data = read_data()
    print(f"Loaded {len(data)} records")
    
    # Get year range
    min_year, max_year = get_year_range(data)
    print(f"Year range: {min_year} - {max_year} AD")
    
    # Test year lookup
    test_year = 1750
    record = get_data_by_year(data, test_year)
    if record:
        print(f"\nData for year closest to {test_year}:")
        print(f"  Actual year: {record['Age (AD)']} AD")
        print(f"  Fe/Ti: {record['Fe/Ti']}")
        print(f"  Si/Ti: {record['Si/Ti']}")
        print(f"  MagSus: {record['MagSus (m3/kg)']}")
    
    # Test value ranges
    fe_min, fe_max = get_value_range(data, "Fe/Ti")
    print(f"\nFe/Ti range: {fe_min} - {fe_max}")
    
    si_min, si_max = get_value_range(data, "Si/Ti")
    print(f"Si/Ti range: {si_min} - {si_max}")
    
    mag_min, mag_max = get_value_range(data, "MagSus (m3/kg)")
    print(f"MagSus range: {mag_min} - {mag_max}")


if __name__ == "__main__":
    main()
