
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('backtest_results_with_conditions.csv')

# App title
st.title('Return Graph by Symbol and Date')

# Dropdown to select symbol with date (column J)
symbol_with_date = st.selectbox('Select Symbol and Date', data['Symbol'].unique())

# Filter the data based on the selection
filtered_data = data[data['Symbol'] == symbol_with_date].iloc[0]

# Extract return columns for plotting
return_columns = ['1_month_return', '3_month_return', '6_month_return', '8_month_return', '9_month_return', 
                  '12_month_return', '15_month_return']
return_values = filtered_data[return_columns].values.flatten()

# Define the time periods
time_periods = [1, 3, 6, 8, 9, 12, 15]

# Plotting the return graph
fig, ax = plt.subplots()
ax.plot(time_periods, return_values, marker='o')
ax.set_title(f'Return Graph for {symbol_with_date}')
ax.set_xlabel('Months')
ax.set_ylabel('Return (%)')
ax.grid(True)

# Display the plot
st.pyplot(fig)
