# Weather Prediction Using HMM

This project is a website that predicts the next day's weather based on historical data using a Hidden Markov Model (HMM). The dataset used contains weather reports from **"Vijayawada"**, including attributes such as:

- Date
- Precipitation
- Temp Max (°C)
- Temp Min (°C)
- Wind
- Weather Condition

## How to Obtain the Dataset

Weather data for Vijayawada was obtained using an API from [Weather API](https://www.weatherapi.com/). To get the data:

1. Sign up for a new account on the website to access historical data.
2. Use the provided API key: `eb49d67b54f44743b2f102519241710` (valid for 13 days).
3. Go to the API explorer, input the API key and the location (Vijayawada, in this case).
4. Click on **Show Response** to get the API call.

> **Note:** Only new users are allowed access to historical data. After 13 days, only present-day data will be accessible. 



![image](https://github.com/user-attachments/assets/c9df638d-b33f-4bff-b0d8-9cd336818e8f)

5. Once api key is obtained, go to **API Explorer** and give api key and location of the place which you need data.
![image](https://github.com/user-attachments/assets/15269276-437d-4dca-bdb4-3677a388470a)

6. Click on show responce, it will give you call api.
![image](https://github.com/user-attachments/assets/e4b42bba-c12a-4790-8a05-91c3928fa314)

7. Then give the call api of historical data in code "Code to get dataset.ipynb" as it is, just change the api key and place.



### Dataset Format
The dataset obtained is saved in `historical_weather_Vijayawada_data.xlsx`, which contains data up to October 16, 2024. To fetch your dataset, copy the API call into the provided Jupyter Notebook **Code to get dataset.ipynb**, changing only the API key and location.

## Model
An HMM model is used to predict future weather based on past data. The code for the model can be found in the notebook **Weather Prediction using hmm.ipynb**.

- **Accuracy:** The model achieves an accuracy of 76%, which is reasonable given the real-time and frequently changing nature of weather.
- **Model Format:** The trained model is saved in `.pkl` format.

## Website Deployment
The model is deployed as a website using Streamlit. The code for the website is in the file **app.py**.


### Preview of website:
![image](https://github.com/user-attachments/assets/6b09b67e-df4e-479c-89a5-6717426e9f8a)

To run the website locally, execute the following commands:

```bash
myenv\Scripts\Activate
streamlit run app.py
```

![image](https://github.com/user-attachments/assets/6b28aae4-7f13-4a0f-95a4-3cc0697758c7)

# Result comparison:
On October 17, 2024, the weather report was fetched using the same API. The report can be found in 17-10-2024's data for verification.ipynb, and the results up to 7:30 PM are saved in ***17th_Oct_weather_data.xlsx***.

# Excel Data Result:
![image](https://github.com/user-attachments/assets/783cc437-f3e4-4c03-81e9-9c1c8ee12a74)

# My Website Prediction:
![image](https://github.com/user-attachments/assets/6d936cf9-c00f-4af3-b336-b2373163fa06)


### Note: The predicted temperature should be taken from the ***temp_min_celcius*** column.


