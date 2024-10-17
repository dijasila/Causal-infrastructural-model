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
plt.show(
