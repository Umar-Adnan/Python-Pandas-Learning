import pandas as pd
import numpy as np

# 1. Create a sample dataset with missing values (NaN)
data = {
    'Date': pd.date_range(start='2026-01-01', periods=6, freq='D'),
    # Day 2 and Day 5 are missing
    'Temperature': [10.0, np.nan, 20.0, 25.0, np.nan, 30.0]
}

df = pd.DataFrame(data)

print("--- Original DataFrame with Missing Values ---")
print(df)
print("\n" + "="*50 + "\n")

# 2. Linear Interpolation (Default - Straight line midpoint)
df_linear = df.copy()
df_linear['Temperature'] = df_linear['Temperature'].interpolate(method='linear')

print("--- 1. Linear Interpolation ---")
print(df_linear)
print("\n" + "="*50 + "\n")

# 3. Time-Based Interpolation (Uses the Date index to compute time gaps)
df_time = df.copy()
df_time = df_time.set_index('Date')  # Time-based interpolation requires a DatetimeIndex
df_time['Temperature'] = df_time['Temperature'].interpolate(method='time')

print("--- 2. Time-Based Interpolation ---")
print(df_time)
print("\n" + "="*50 + "\n")

# 4. Polynomial Interpolation (Curved line smooth fit - order 2 = quadratic)
df_poly = df.copy()
df_poly['Temperature'] = df_poly['Temperature'].interpolate(method='polynomial', order=2)

print("--- 3. Polynomial Interpolation (Order 2) ---")
print(df_poly)