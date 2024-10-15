# WeatherPrediction_Using_HMM

I made a website that predicts the nextday's weather in Vijayawada based on previous 2 days weather report.
This website predicts the Precipitation that weather it is Sun or Fog or Rain.

I used HMM(Hidden Markov Model) to do the prediction.

Dataset:
For the local Vijayawada's Weather dataset used api key which have data from 2024-01-01 to 2024-10-15.
website for getting api is https://www.weatherapi.com/my/
How to get api: https://www.youtube.com/watch?v=fbCUGUj_uIU&t=126s
api key(for vijayawada): http://api.weatherapi.com/v1/current.json?key=f209d64f0866472da09232726242609&q=Vijayawada&aqi=no
This is time limited api such that after some time api gets disabled. so i downloaded the data from api into excel and used for prediction.

"GetDatasetOfVijayawadaTillToday.ipynb" is the code which stores api data into excel.
