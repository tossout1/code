import pandas as pd

# Load the CSV file
df = pd.read_csv('Form_AI.csv')

# Get the value in row 2 (index 1), column 'name'

# Function that returns the same cell value
def ai_give_response(input):
    cell_value = df.at[f"{input}", 'output']
    return cell_value