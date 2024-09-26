import streamlit as st
import threading
import schedule
import time
import requests
from pymongo import MongoClient

# Importing your modules
import dashboard
import currency_bucket
import future_prediction
import exchange_rate

st.set_page_config(layout="wide")

# MongoDB connection details
MONGO_URI = 'mongodb://localhost:27017/'  # Adjust as necessary
DB_NAME = 'CurrExchTest'
COLLECTION_NAME = 'CurrExch'


# Function to fetch and update data in MongoDB
def update_currency_data():
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    # Fetch the latest currency data from the API
    response = requests.get('https://v6.exchangerate-api.com/v6/c616daa3d69e101f81daa5f2/latest/USD')

    if response.status_code == 200:
        latest_data = response.json()

        # Prepare data for MongoDB
        if 'conversion_rates' in latest_data:
            # Create a new document to store currency exchange rates
            currency_data = {
                'Date': latest_data['time_last_update_utc'][:10],  # Extract date in "YYYY-MM-DD" format
            }

            # Populate the document with conversion rates against USD
            for currency, rate in latest_data['conversion_rates'].items():
                # Add each currency rate to the document
                currency_data[currency] = rate

            # Insert the new data into MongoDB
            collection.insert_one(currency_data)  # Insert a single document containing all rates
            st.success("Database updated with the latest currency data.")
        else:
            st.error("No conversion rates found in the API response.")
    else:
        st.error("Failed to fetch data from the API.")


# Schedule the update function to run every day at midnight
def schedule_updates():
    schedule.every().day.at("00:00").do(update_currency_data)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=schedule_updates, daemon=True)
scheduler_thread.start()


# Define a function to display content based on the selected tab
def display_page(tab):
    if tab == "Exchange Rates":
        exchange_rate.main()
    elif tab == "Currency Bucket":
        currency_bucket.main()
    elif tab == "Home":
        dashboard.main()
    elif tab == "Future Prediction":
        future_prediction.main()


# Set up the top navigation using tabs
tabs = st.tabs(["Home", "Currency Bucket", "Future Prediction", "Exchange Rates"])

# Display the selected tab
with tabs[0]:
    display_page("Home")
with tabs[1]:
    display_page("Currency Bucket")
with tabs[2]:
    display_page("Future Prediction")
with tabs[3]:
    display_page("Exchange Rates")
