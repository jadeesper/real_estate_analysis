## Real Estate Analysis

The aim of this is to fetch data from a real estate website and save it into a parquet file. Pyspark is then used to study the data. Finally, we create a user-friendly dashboard with Streamlit for easier data exploration.


#NOTE
These notebooks should be ran (particularly 'preprocessing_feature_engineering.ipnyb') on a computer with Java (because of use of pyspark)

# GETTING STARTED
1. Download and Install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html)
2. Create a new conda environement
```
conda create -n myvenv python=3.9
```
3. Activate the environemnt
```
conda activate myvenv
```
4. Install Depedencies
```
pip install -r requirements.txt

#RUNNING THE STREAMLIT APP

1. Type the following command into a command prompt to open the Streamlit app
```
streamlit run streamlit/A_propos_des_données.py
```
2. If not redirected, click Local or Network URL using (ctrl+ click)
