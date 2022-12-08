import pandas as pd
import streamlit as st

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

# Create the title for the web app
st.title("My First Streamlit App")
sidebar = st.sidebar
sidebar.title("This is the sidebar.")
sidebar.write("You can add any elements to the sidebar.")

# Display the content of the dataset
st.header("Dataset Overview")
st.dataframe(titanic_data)

st.header("Data Description")

st.markdown("___")

# Select the gender and the display the dataset with this selection
selected_sex = st.selectbox("Select Sex", titanic_data['sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")

st.write(titanic_data.query(f"""sex==@selected_sex"""))

st.markdown("___")

# Select the embark town of the passanger and then display the dataset with this selection
selected_town = st.radio("Select Embark Town", titanic_data['embark_town'].unique())
st.write("Selected Embark Town:", selected_town)

st.write(titanic_data.query(f"""embark_town==@selected_town"""))

st.markdown("___")

# Select a range of the fare and then display the dataset with this selection
optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

# Display of the dataset whith the max fare selected
st.write(titanic_data.query(f"""fare>=@fare_max"""))