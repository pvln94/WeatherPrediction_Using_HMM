# WeatherPrediction_Using_HMM

I made a website that predicts the nextday's weather based on prevous days history weather data.
Dataset contains weather report of Vijayawada. It includes attributes such as date, precipitation, temp_max_celcius, temp_min_celcius, wind, weather_condition.

How to obtain Dataset:
Weather data of Vijayawada is obtained using an API from [website](https://www.weatherapi.com/).
API Key is "eb49d67b54f44743b2f102519241710". Note this is a temporary api key valid only for 13 days. Later that we are not accessible to historical data, only present days data is available.
Only new account users are accessible to historical data, so i suggest you to signup to website using new account.
![image](https://github.com/user-attachments/assets/c9df638d-b33f-4bff-b0d8-9cd336818e8f)

Once api key is obtained, go to api explorer and give api key and location of the place which you need data.
![image](https://github.com/user-attachments/assets/15269276-437d-4dca-bdb4-3677a388470a)

click on show responce, it will give you call api.
![image](https://github.com/user-attachments/assets/e4b42bba-c12a-4790-8a05-91c3928fa314)

then give the call api of historical data in code "Code to get dataset.ipynb" as it is, just change the api key and place.



The dataset which i obtained is "historical_weather_Vijayawada_data.xlsx", which contains data upto 16th october 2024.

Model used:
I used hmm model which is used to predict the future result based on previous data.

code part is in "Weather Prediction using hmm.ipynb".

As the data is related to weather(which changes frequently), large and real time, its accuracy to predict is 76%

I saved the model in pkl file format.

Then i used "streamlit" to run model as a website.
code for website is "app.py".

Preview of website:
![image](https://github.com/user-attachments/assets/6b09b67e-df4e-479c-89a5-6717426e9f8a)

Note: I attached a zip folder, u can use it and execute following commands to get website.


Code to run website is as in follows

myenv\Scripts\Activate
streamlit run app.py 

![image](https://github.com/user-attachments/assets/6b28aae4-7f13-4a0f-95a4-3cc0697758c7)

Result comparison:
As today is 17th october 2024, i obtained the weather report of this day using api, which is represented in "17-10-2024's data for verification.ipynb".
Its respective output upto 7:30 pm is in "17th_Oct_weather_data.xlsx".
excel result:
![image](https://github.com/user-attachments/assets/783cc437-f3e4-4c03-81e9-9c1c8ee12a74)

My website Result:
![image](https://github.com/user-attachments/assets/6d936cf9-c00f-4af3-b336-b2373163fa06)


Note: take temperature as temperature of "temp_min_celcius"


