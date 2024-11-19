import os
import json
import requests
import math_operations  # Importing the user-defined module

# Function to read the content of a text file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to make an API request and return JSON response
def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

# Function to save JSON data to a file
def save_json_to_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    # Example 1: Read content from a file
    file_content = read_file('example.txt')
    if file_content:
        print(f"File Content:\n{file_content}\n")
    
    # Example 2: Fetch data from an API
    api_url = 'https://jsonplaceholder.typicode.com/posts/1'
    api_data = get_api_data(api_url)
    if api_data:
        print(f"API Data:\n{json.dumps(api_data, indent=4)}\n")
    
        # Save API data to a JSON file
        save_json_to_file(api_data, 'api_data.json')
    
    # Example 3: Perform arithmetic operations using the custom module
    a, b = 10, 5
    print(f"Addition: {a} + {b} = {math_operations.add(a, b)}")
    print(f"Subtraction: {a} - {b} = {math_operations.subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {math_operations.multiply(a, b)}")
    print(f"Division: {a} / {b} = {math_operations.divide(a, b)}")
