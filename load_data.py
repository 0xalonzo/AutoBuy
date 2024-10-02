import pandas as pd

# Load the datasets 
usa_data = pd.read_csv('OnlineSalesUSA.csv', dtype={'Price': 'float64'}, low_memory=False)
uk_data = pd.read_csv('OnlineSalesUK.csv', dtype={'UnitPrice': 'float64'}, low_memory=False)  # Adjust dtype if needed

# Print head to test
print("UK Dataset Head:", uk_data.head)
print("USA Dataset Head:", usa_data.head)

