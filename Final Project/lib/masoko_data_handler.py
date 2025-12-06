"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Data handler for Lake Masoko geochemical data
"""

import json

def readData(filename="data.json"):
    """Read Lake Masoko data from JSON file"""
    with open(filename, "r") as jsonFile:
        data = json.load(jsonFile)
    return data

def getDataByYear(data, year):
    """Find data record closest to given year"""
    if not data:
        return None
    
    closestRecord = min(data, key=lambda x: abs(x["Age (AD)"] - year))
    return closestRecord

def getYearRange(data):
    """Get range of years in dataset"""
    if not data:
        return (0, 0)
    
    years = [record["Age (AD)"] for record in data]
    return (min(years), max(years))

def getValueRange(data, key):
    """Get range of values for specific measurement"""
    if not data:
        return (0, 0)
    
    values = [record[key] for record in data 
              if record[key] != "-" and isinstance(record[key], (int, float))]
    
    if not values:
        return (0, 0)
    
    return (min(values), max(values))

def normalizeValue(value, minVal, maxVal):
    """Normalize value to range [0, 1]"""
    if maxVal == minVal:
        return 0.5
    return (value - minVal) / (maxVal - minVal)

def main():
    """Test function"""
    data = readData()
    print(f"Loaded {len(data)} records")
    
    minYear, maxYear = getYearRange(data)
    print(f"Year range: {minYear} - {maxYear} AD")

if __name__ == "__main__":
    main()
