from plot_aqi import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016 #we will use data for 2017 and 2018 during testing time
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

def metadata(month, year): #web scrap each file from each year
    html_file = open('Data/Html_Data/{}/{}.html'.format(year, month), 'rb')
    plain_text = html_file.read() #read all data into plain_text

    temp_data = []
    final_data = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}): #iterating through all the tables in this class from the web scraped data
        for subtable in table:
            for row in subtable:
                text_row = row.get_text()
                temp_data.append(text_row)
    
    numRows = len(temp_data)/15 #get number of rows. each row has 15 features

    for info in range(round(numRows)): #iterate through each row
        #iterate through each feature
        new_temp_data = []
        for i in range(15):
            new_temp_data.append(temp_data[0])
            temp_data.pop(0) #remove data after appending
        final_data.append(new_temp_data)
    
    length =len(final_data)

    final_data.pop(length - 1) #remove the last record, we do not need it
    final_data.pop(0) #drop the features row

    for k in range(len(final_data)):
        #Dropping columns with missing values
        final_data[k].pop(6)
        final_data[k].pop(13)
        final_data[k].pop(12)
        final_data[k].pop(11)
        final_data[k].pop(10)
        final_data[k].pop(9)
        final_data[k].pop(0)

    return final_data

def combine(year, cs): #combine data for all the years
    for a in pd.read_csv('Preprocessed-Data/real_' + str(year) + '.csv', chunksize=cs):
        dataframe = pd.DataFrame(data=a)
        mylist = dataframe.values.tolist()
    return mylist


#main method
if __name__=="__main__":
    if not os.path.exists("Preprocessed-Data"):
        os.makedirs("Preprocessed-Data")
    for year in range(2013, 2017): #we will use 2017 and 2018 data during testing
        real_data = []
        with open("Preprocessed-Data/real_" + str(year) + '.csv', 'w') as csvfile:
            write = csv.writer(csvfile, dialect='excel') #show table resembling an excel file
            write.writerow(
                ['T', 'TM', 'Tm', 'SLP', 'H', 'W', 'V', 'VM', 'PM 2.5']
            )
        for month in range(1, 13):
            temp = metadata(month, year)
            real_data = real_data + temp

        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()  #dynamically calling avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016

        if len(pm) == 364:
            pm.insert(364, '-')

        for i in range(len(real_data)-1):
            real_data[i].insert(8, pm[i]) #append to the 8th column index with the pm 2.5 values
         
        with open('Preprocessed-Data/real_' + str(year) + '.csv', 'a') as csvfile: #append mode
            write = csv.writer(csvfile, dialect = 'excel')
            for row in real_data:
                flag = 0
                for element in row:
                    if element == "" or element == "-": #drop rows with blank values
                        flag = 1
                if flag != 1:
                    write.writerow(row) #only include rows without blank values
        
    
    data_2013 = combine(2013, 600)
    data_2014 = combine(2014, 600)
    data_2015 = combine(2015, 600)
    data_2016 = combine(2016, 600)

    total = data_2013+data_2014+data_2015+data_2016

    with open('Preprocessed-Data/Real_Combine.csv', 'w') as csvfile:
        write = csv.writer(csvfile, dialect='excel')
        write.writerow(
            ['T','TM','Tm','SLP','H', 'W', 'V', 'VM', 'PM 2.5']
        )
        write.writerow(total)

df = pd.read_csv('Preprocessed-Data/Real_Combine.csv')

        










