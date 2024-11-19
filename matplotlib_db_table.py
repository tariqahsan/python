import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Establishing connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mma123",
    database="mmadb"
)

# Query to fetch data
query = "SELECT x_value_column, y_value_column, z_value_column FROM mmadb.sample_data"

# Load data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Closing the connection
conn.close()

# Pivoting data to create a matrix suitable for heatmap
df_pivot = df.pivot(index='y_value_column', columns='x_value_column', values='z_value_column')
# Plotting heatmap
sns.heatmap(df_pivot, annot=True, cmap='coolwarm')
plt.title('Heatmap of Z values')
plt.show()

