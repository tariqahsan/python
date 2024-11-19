import mysql.connector

# Database connection details (replace with your own)
host = "localhost"
user = "root"
password = "mma123"
database = "mma"

def connect_to_database():
  """Connects to the MySQL database."""
  try:
    connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
    return connection
  except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    return None

def create_record(name, email, phone):
  """Inserts a new record into the table."""
  connection = connect_to_database()
  if connection:
    cursor = connection.cursor()
    sql = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
    data = (name, email, phone)
    try:
      cursor.execute(sql, data)
      connection.commit()
      print("Record inserted successfully")
    except mysql.connector.Error as err:
      print("Error creating record:", err)
    finally:
      connection.close()
      cursor.close()

def read_records():
  """Fetches all records from the table."""
  connection = connect_to_database()
  if connection:
    cursor = connection.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Records:")
    for row in result:
      print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")
    connection.close()
    cursor.close()

def update_record(id, name, email, phone):
  """Updates an existing record in the table."""
  connection = connect_to_database()
  if connection:
    cursor = connection.cursor()
    sql = "UPDATE users SET name = %s, email = %s, phone = %s WHERE id = %s"
    data = (name, email, phone, id)
    try:
      cursor.execute(sql, data)
      connection.commit()
      print(f"Record with ID {id} updated successfully")
    except mysql.connector.Error as err:
      print("Error updating record:", err)
    finally:
      connection.close()
      cursor.close()

def delete_record(id):
  """Deletes a record from the table."""
  connection = connect_to_database()
  if connection:
    cursor = connection.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    data = (id,)
    try:
      cursor.execute(sql, data)
      connection.commit()
      print(f"Record with ID {id} deleted successfully")
    except mysql.connector.Error as err:
      print("Error deleting record:", err)
    finally:
      connection.close()
      cursor.close()

# Example usage
create_record("John Doe", "john.doe@example.com", "+1234567890")
read_records()
update_record(1, "Jane Doe", "jane.doe@example.com", "+9876543210")
read_records()
delete_record(2)
read_records()
