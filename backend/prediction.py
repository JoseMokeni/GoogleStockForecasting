import pandas as pd
# import plt
import matplotlib.pyplot as plt
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from datetime import datetime


END_DATASET = '2023-10-20'


def getForecasts(model, date):
    import warnings
    warnings.filterwarnings('ignore')

    dateMinus20 = pd.to_datetime(date) - pd.DateOffset(days=20)
    datePlus5 = pd.to_datetime(date) + pd.DateOffset(days=5)
    
    step = (pd.to_datetime(datePlus5) - pd.to_datetime(END_DATASET)).days
    forecast = model.get_forecast(steps=step)

    # Access the forecasted values
    forecasted_values = forecast.predicted_mean
    # reset the indexes to start from 0
    
    forecasted_values = forecasted_values.reset_index(drop=True)
    
    # print(type(forecasted_values))
    # get the last value of the forecasted_values series
    i = forecasted_values[len(forecasted_values) - 1]
    # print("i =", i)
    # print(f"The forecasted value for {date} is {i}")
    
    # print("The forecasted value for {} is {}".format(date, forecasted_values[-1]))
    
    # set the index to dates from 2023-10-21 to datePlus5
    index = pd.date_range(pd.to_datetime('2023-10-21'), datePlus5)
    
    # create a new dataframe with the forecasted values and the index
    forecasted_values.index = index
    
    # now keep only the dates from dateMinus20 to datePlus5
    
    forecasted_values = forecasted_values[dateMinus20:datePlus5]
    
    print(type(forecasted_values))
    
    return forecasted_values

def uploadForecastToCloudinary(model, date):
    # this function will display the forectasted values
    # the forecast starting 20 days before the date and ending 2 days after the date
    
    forecasts = getForecasts(model, date)
    
    # plot the forecasts
    plt.figure(figsize=(16,8))
    # plot forecasts
    # forecasts is a series
    plt.plot(forecasts, color='green', label='Forecast')
    
    plt.ylabel('Close Price')
    plt.xlabel('Date')
    plt.legend()
    # convert the date string to a datetime object
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    # put a crossed line at the date    
    plt.axvline(x=date_obj, color='red', linestyle='--', label='Prediction Date')
    
    # display the value of the forecast at the date
    plt.text(date_obj, forecasts[date_obj], forecasts[date_obj])
    
    plt.savefig('forecast.png')
    
    # upload the image to cloudinary
    
    cloudinary.config(
        cloud_name = 'cloud_name',
        api_key = 'api_key',
        api_secret = 'api_secret'        
    )
    
    upload = cloudinary.uploader.upload('forecast.png') 
    os.remove('forecast.png')
    return upload['url']
    
    