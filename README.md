# Currexch

Currexch is a currency exchange rate analysis platform that allows users to visualize, analyze, and predict exchange rates. The platform provides insightful features for comparing multiple currencies, creating custom currency baskets, viewing current rates, and forecasting future rates.

## Features

### 1. Home Tab
- **Select Multiple Currencies**: Users can choose multiple currencies to analyze.
- **Custom Duration**: Specify a custom duration for which the exchange rate against USD will be visualized.
- **Visualizations**: Graphical representation of exchange rates for the selected duration.
- **Key Metrics**:
  - Minimum and maximum exchange rates during the selected period.
  - **Risk Factor**: An evaluation of currency volatility based on historical data.

### 2. Currency Basket Tab
- **Create Custom Currency Basket**: Users can select multiple currencies to form a basket.
- **Total Value Calculation**: The total value of the currency basket is displayed in the selected base currency.

### 3. Future Prediction Tab
- **Predict Future Values**: Select a currency and specify the duration (up to 10 years) to predict future exchange rates.
- **Confidence Interval**: The prediction includes a confidence interval to provide a range for the forecasted exchange rates.

### 4. Exchange Rate Tab
- **Current Exchange Rates**: View a list of real-time exchange rates for all currencies against USD.
- **Search Functionality**: Quickly search for and view the exchange rate of a specific currency.

## Installation

To run the Currexch platform locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/currexch.git
2. **Navigate to the Project Directory**:
   ```bash
   cd currexch
3. **nstall Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Use Streamlit to run the app**:
   ```bash
   streamlit run app.py


## Data Source

The platform fetches exchange rate data from a MongoDB database, ensuring real-time accuracy and up-to-date currency information.
