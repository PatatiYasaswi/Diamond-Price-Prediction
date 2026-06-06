Diamond Price Prediction Project

Project Overview

This project is about predicting the price of diamonds using machine learning. 
Different features of diamonds such as carat, cut, color, clarity, depth, and dimensions were used to train the model.

The project was done step-by-step starting from data analysis to model building and finally creating a small web application for prediction.


Dataset Information

The dataset contains details about diamonds, including:

- Carat → Weight of the diamond
- Cut → Quality of diamond cut
- Color → Diamond color grade
- Clarity → Diamond clarity quality
- Depth → Total depth percentage
- Table → Width percentage of top surface
- X, Y, Z → Diamond dimensions
- Price → Price of the diamond


Project Steps

1. Data Understanding
- Loaded and studied the dataset
- Checked rows, columns, and data types

2. Data Cleaning
- Checked missing values
- Removed duplicate records

3. Exploratory Data Analysis (EDA)
- Created graphs and visualizations
- Studied relationships between features
- Found important patterns in the dataset

4. Data Preprocessing
- Converted categorical values into numbers
- Split data into training and testing sets
- Applied feature scaling where required

5. Model Building
Three machine learning models were trained:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

6. Model Evaluation
The models were compared using:
- R2 Score
- MAE
- RMSE

7. Final Model
Random Forest Regressor gave the best performance and was selected as the final model.

8. Deployment
A Streamlit web application was created where users can enter diamond details and get predicted prices instantly.


Best Model Performance

Random Forest Regressor:

- R2 Score: 0.982
- MAE: 262
- RMSE: 519

This shows the model predicts diamond prices with very high accuracy.



Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit



Files Included

- diamonds.csv → Dataset
- Diamond_Price_Prediction.ipynb → Main notebook
- diamond_price_model.pkl → Saved trained model
- app.py → Streamlit application
- requirements.txt → Required libraries



How to Run the Project

1. Install required libraries:

pip install -r requirements.txt

2. Run Streamlit app:

streamlit run app.py

3. Open the browser link shown in terminal.



Conclusion

This project successfully predicts diamond prices using machine learning techniques. 
Among all models, Random Forest Regressor performed the best and achieved very high prediction accuracy.

The project helped in understanding:
- Data analysis
- Visualization
- Machine learning models
- Model evaluation
- Basic deployment using Streamlit