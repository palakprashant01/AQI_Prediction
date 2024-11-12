import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv
from plot_aqi import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016

def metadata(month, year):
    # Web scrape each file from each year
    html_file = open(f'Data/Html_Data/{year}/{month}.html', 'rb')
    plain_text = html_file.read()
    
    temp_data = []
    final_data = []
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for subtable in table:
            for row in subtable:
                text_row = row.get_text()
                temp_data.append(text_row)
    
    # Calculate the number of rows
    numRows = len(temp_data) // 15
    
    # Extract data for each row
    for info in range(round(numRows)):
        new_temp_data = []
        for i in range(15):
            new_temp_data.append(temp_data[0])
            temp_data.pop(0)
        final_data.append(new_temp_data)
    
    # Remove the last and first rows (unnecessary data)
    final_data.pop(len(final_data) - 1)
    final_data.pop(0)
    
    # Remove specific columns with missing values
    for k in range(len(final_data)):
        final_data[k].pop(6)
        final_data[k].pop(13)
        final_data[k].pop(12)
        final_data[k].pop(11)
        final_data[k].pop(10)
        final_data[k].pop(9)
        final_data[k].pop(0)
    
    return final_data

def combine(year, cs):
    # Combine data for all the years
    mylist = []
    for a in pd.read_csv(f'Preprocessed-Data/real_{year}.csv', chunksize=cs):
        dataframe = pd.DataFrame(data=a)
        mylist.extend(dataframe.values.tolist())
    return mylist

if __name__ == "__main__":
    # Create directory if it doesn't exist
    if not os.path.exists("Preprocessed-Data"):
        os.makedirs("Preprocessed-Data")
    
    for year in range(2013, 2017):
        real_data = []
        # Write header row to CSV file
        with open(f"Preprocessed-Data/real_{year}.csv", 'w', newline='') as csvfile:
            write = csv.writer(csvfile, dialect='excel')
            write.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'W', 'V', 'VM', 'PM 2.5'])
        
        # Process data for each month
        for month in range(1, 13):
            temp = metadata(month, year)
            real_data.extend(temp)
        
        # Dynamically call the average data function for the year
        pm = getattr(sys.modules[__name__], f'avg_data_{year}')()
        
        # Insert placeholder if necessary
        if len(pm) == 364:
            pm.insert(364, '-')
        
        # Insert PM 2.5 values into the data
        for i in range(len(real_data) - 1):
            real_data[i].insert(8, pm[i])
        
        # Write processed data to CSV file
        with open(f'Preprocessed-Data/real_{year}.csv', 'a', newline='') as csvfile:
            write = csv.writer(csvfile, dialect='excel')
            for row in real_data:
                if all(element not in ["", "-"] for element in row):
                    write.writerow(row)
    
    # Combine data from all years
    data_2013 = combine(2013, 600)
    data_2014 = combine(2014, 600)
    data_2015 = combine(2015, 600)
    data_2016 = combine(2016, 600)
    
    total = data_2013 + data_2014 + data_2015 + data_2016
    
    # Write combined data to a new CSV file
    with open('Preprocessed-Data/Real_Combine.csv', 'w', newline='') as csvfile:
        write = csv.writer(csvfile, dialect='excel')
        write.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'W', 'V', 'VM', 'PM 2.5'])
        write.writerows(total)
    
    # Read the combined CSV file into a pandas DataFrame
    df = pd.read_csv('Preprocessed-Data/Real_Combine.csv')
    print(df.head())

        










