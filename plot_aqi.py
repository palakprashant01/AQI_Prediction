import pandas as pd
import matplotlib.pyplot as plt

#Determing the average AQI of each day (across 24 hours) in 2013

def avg_data_2013():
    temp = 0
    average = []
    for rows in pd.read_csv("AQI/aqi2013.csv", chunksize = 24): #iterating through all the 24 hours of the day 1 iteration
        adding = 0  #to add hour data
        avg = 0.0 #to divide data by 12 for the 12 months
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows(): #Iterating through the 24 rows and appending 'PM2.5' values to the data list
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                adding = adding + i
            elif type(i) is str: #get valid data values and converting to string
                if i!='NoData' and i!= 'PwrFail' and i!='---' and i!='InVld':
                    temp_str = float(i)
                    adding = adding+temp_str
        
        avg = adding/24
        temp = temp + 1

        average.append(avg)

    return average
    

#Determing the average AQI of each day (across 24 hours) in 2014

def avg_data_2014():
    temp = 0
    average = []
    for rows in pd.read_csv("AQI/aqi2014.csv", chunksize = 24): #iterating through all the 24 hours of the day 1 iteration
        adding = 0  #to add hour data
        avg = 0.0 #to divide data by 12 for the 12 months
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows(): #Iterating through the 24 rows and appending 'PM2.5' values to the data list
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                adding = adding + i
            elif type(i) is str: #get valid data values and converting to string
                if i!='NoData' and i!= 'PwrFail' and i!='---' and i!='InVld':
                    temp_str = float(i)
                    adding = adding+temp_str
        
        avg = adding/24
        temp = temp + 1

        average.append(avg)

    return average
    
#Determing the average AQI of each day (across 24 hours) in 2015

def avg_data_2015():
    temp = 0
    average = []
    for rows in pd.read_csv("AQI/aqi2015.csv", chunksize = 24): #iterating through all the 24 hours of the day 1 iteration
        adding = 0  #to add hour data
        avg = 0.0 #to divide data by 12 for the 12 months
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows(): #Iterating through the 24 rows and appending 'PM2.5' values to the data list
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                adding = adding + i
            elif type(i) is str: #get valid data values and converting to string
                if i!='NoData' and i!= 'PwrFail' and i!='---' and i!='InVld':
                    temp_str = float(i)
                    adding = adding+temp_str
        
        avg = adding/24
        temp = temp + 1

        average.append(avg)

    return average
    
#Determing the average AQI of each day (across 24 hours) in 2016

def avg_data_2016():
    temp = 0
    average = []
    for rows in pd.read_csv("AQI/aqi2016.csv", chunksize = 24): #iterating through all the 24 hours of the day 1 iteration
        adding = 0  #to add hour data
        avg = 0.0 #to divide data by 12 for the 12 months
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows(): #Iterating through the 24 rows and appending 'PM2.5' values to the data list
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                adding = adding + i
            elif type(i) is str: #get valid data values and converting to string
                if i!='NoData' and i!= 'PwrFail' and i!='---' and i!='InVld':
                    temp_str = float(i)
                    adding = adding+temp_str
        
        avg = adding/24
        temp = temp + 1

        average.append(avg)

    return average
    
#Determing the average AQI of each day (across 24 hours) in 2017

def avg_data_2017():
    temp = 0
    average = []
    for rows in pd.read_csv("AQI/aqi2017.csv", chunksize = 24): #iterating through all the 24 hours of the day 1 iteration
        adding = 0  #to add hour data
        avg = 0.0 #to divide data by 12 for the 12 months
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows(): #Iterating through the 24 rows and appending 'PM2.5' values to the data list
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                adding = adding + i
            elif type(i) is str: #get valid data values and converting to string
                if i!='NoData' and i!= 'PwrFail' and i!='---' and i!='InVld':
                    temp_str = float(i)
                    adding = adding+temp_str
        
        avg = adding/24
        temp = temp + 1

        average.append(avg)

    return average

#Determing the average AQI of each day (across 24 hours) in 2018

def avg_data_2018():
    temp = 0
    average = []
    for rows in pd.read_csv("AQI/aqi2018.csv", chunksize = 24): #iterating through all the 24 hours of the day 1 iteration
        adding = 0  #to add hour data
        avg = 0.0 #to divide data by 12 for the 12 months
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows(): #Iterating through the 24 rows and appending 'PM2.5' values to the data list
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                adding = adding + i
            elif type(i) is str: #get valid data values and converting to string
                if i!='NoData' and i!= 'PwrFail' and i!='---' and i!='InVld':
                    temp_str = float(i)
                    adding = adding+temp_str
        
        avg = adding/24
        temp = temp + 1

        average.append(avg)

    return average

if __name__=="__main__":
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.plot(range(0,365),lst2015,label="2015 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
    
    
