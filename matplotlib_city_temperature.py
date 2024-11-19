import mysql.connector
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

# Establishing connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mma123",
    database="mmadb"
)

# SQL query to get temperature data for the entire year for a specific city
query = """
    SELECT date, min_temperature, max_temperature 
    FROM city_temperature 
    WHERE city = 'New York' 
    AND YEAR(date) = 2023
    ORDER BY date
"""

# Load the data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Plotting the temperature data
plt.figure(figsize=(10,6))

# Plotting the minimum and maximum temperatures
plt.plot(df['date'], df['min_temperature'], label='Min Temperature', color='blue')
plt.plot(df['date'], df['max_temperature'], label='Max Temperature', color='red')

# Adding labels and title
plt.title('Daily Temperature in New York - 2023')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)

# Add a legend
plt.legend()

# Show grid for better readability
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
