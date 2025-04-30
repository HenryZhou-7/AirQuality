### Summary of the Notebook

This notebook processes and analyzes global air pollution data, combining it with city and country information, and performs various data cleaning, visualization, and machine learning tasks. Below is a summary of the steps:

1. **Data Loading and Cleaning**:
    - Loaded global air pollution data and city information datasets.
    - Identified and handled missing values in the dataset, particularly for `country_name`, using fuzzy matching with city names.

2. **Data Export and Re-import**:
    - Cleaned data was exported to CSV files and re-imported for further processing.

3. **Data Visualization**:
    - Created scatter plots using Plotly to visualize AQI levels by city and country.
    - Analyzed the number of cities per country with unique AQI data.

4. **Database Integration**:
    - Connected to a PostgreSQL database to retrieve and combine pollution data with city coordinates using SQL queries.

5. **Country-Level Analysis**:
    - Calculated average AQI values for each country and merged them with geographical coordinates for visualization.

6. **Machine Learning**:
    - Applied K-Nearest Neighbors (KNN) regression to predict AQI values based on geographical coordinates.
    - Tuned the hyperparameter `K` using cross-validation to minimize RMSE.
    - Evaluated the model using RMSE and MAE metrics, with and without clipping AQI values.

7. **Exploratory Data Analysis**:
    - Visualized the distribution of AQI values using histograms.

8. **Final Results**:
    - Identified the best K value for KNN regression and evaluated the model's performance on the test set. We see that the model can confidently predict AQI values within approximately ±16 units (MAE). This prediction may not be good enough for health warnings and it is not intended for such use cases, but for more of a general feel for any particular area on land.

This notebook combines data cleaning, visualization, database integration, and machine learning to analyze and predict air quality levels globally. Using Dash and plotly, I have created a interative map that can predict AQI based of cursor clicks.
![air quality](https://github.com/user-attachments/assets/61134932-4d3c-4071-b01c-b3be65c5b82f)
