
# Weather Logger

This project is a simple **weather logging system** that records daily
weather information (temperature, humidity, wind speed, condition) into
a CSV file.



## 🚀 How to Use

1.  Open the `weather_log.csv` file in Excel, Google Sheets, or any CSV
    viewer.
2.  Analyze temperature, humidity, or weather trends over time.
3.  Extend this project by adding:
    -   Live weather API integration
    -   Graphs & data visualization
    -   Automated daily logging

## 🔮 Future Ideas

-   Build a **dashboard** to visualize trends.
-   Predict weather patterns using **machine learning**.
-   Share data with community groups or research projects.

------------------------------------------------------------------------

📊 Data Preparation and Shaping Project

Example raw_data.csv (before cleaning)
Temp	Hum	Condition
30	70	Sunny
32	75	Rainy
28	80	NaN
30	NaN	Sunny
30	70	Sunny

Example cleaned_data.csv (after shaping)
Temperature	Humidity	Condition	FeelsLike	Condition_encoded
30.0	70.0	Sunny	27.0	1
32.0	75.0	Rainy	29.5	0
28.0	80.0	Sunny	26.0	1
30.0	75.0	Sunny	27.5	1



