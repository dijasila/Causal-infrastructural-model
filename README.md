# Causal-infrastructural-model

Here’s a general outline of a Python script that uses time series data to evaluate causal impact using the causalimpact library:

Steps:
Data Preparation: You need time series data for infrastructure changes (like parking removal) and the observed metrics (traffic flow, business activity, and property values).
Causal Impact Model: We use Bayesian Structural Time Series (BSTS) from causalimpact to estimate the impact of the intervention (e.g., parking removal).
Evaluation: The library provides an analysis of the counterfactual—what would have happened without the intervention.
Python Code
You would need time series data like this:

Date	ParkingSpaces	TrafficFlow	BusinessActivity	PropertyValue
2022-01-01	50	1000	500	700000
2022-02-01	50	950	480	705000
...	...	...	...	...
2023-01-01	30	850	450	690000
Install Dependencies
bash
Copy code
pip install causalimpact pandas matplotlib
Example Python Script
python
Copy code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from causalimpact import CausalImpact

# Example dataset creation (replace this with your real data)
data = {
    'date': pd.date_range(start='2022-01-01', periods=24, freq='M'),
    'parking_spaces': [50]*12 + [30]*12,  # Drop in parking spaces after 12 months
    'traffic_flow': np.random.normal(1000, 50, 12).tolist() + np.random.normal(850, 40, 12).tolist(),
    'business_activity': np.random.normal(500, 30, 12).tolist() + np.random.normal(450, 25, 12).tolist(),
    'property_value': np.random.normal(700000, 5000, 12).tolist() + np.random.normal(690000, 4000, 12).tolist()
}

df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Split the data into pre and post intervention (e.g., after parking spaces were removed)
pre_period = [0, 11]  # First 12 months are 'pre intervention'
post_period = [12, 23]  # Last 12 months are 'post intervention'

# Only include the variables of interest (e.g., parking spaces, traffic flow, etc.)
# In this example, we're assuming the intervention is the change in parking spaces
# and we're measuring the impact on traffic flow and business activity
df = df[['traffic_flow', 'business_activity']]

# Applying Causal Impact
ci = CausalImpact(df, pre_period, post_period)

# Print the summary report
print(ci.summary())
print(ci.summary('report'))

# Plot the results
ci.plot()
plt.show()
Code Explanation:
Data Setup: The data has two phases: before and after the intervention (e.g., reducing parking spaces).
CausalImpact Model: We use the CausalImpact library to create a counterfactual model predicting what would have happened without the intervention.
Evaluation: The library provides a detailed summary of the causal impact and visualizes the actual vs predicted outcome.
Results:
The output will show:

Point Estimates: Predicted changes in traffic flow, business activity, etc.
Confidence Intervals: It gives a range of possible values for the change.
Visualization: A graph that shows the actual vs predicted values, highlighting the causal effect.
Customization:
You can easily customize the analysis by including more metrics, such as property values, or by incorporating more sophisticated models depending on your data.

Let me know if you need help with a specific part!
