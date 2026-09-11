import pandas as pd

df_q1 = pd.DataFrame({
    'Emp_ID': [101, 102],
    'Sales': [15000, 20000]
})

df_q2 = pd.DataFrame({
    'Emp_ID': [103, 104],
    'Sales': [18000, 22000]
})

# 1. Vertical Stacking (Row-wise) - Stacking Q2 below Q1
# ignore_index=True resets the row numbers to 0, 1, 2, 3
vertical_stack = pd.concat([df_q1, df_q2], ignore_index=True)
print("=== Vertical Concatenation (Row-wise) ===")
print(vertical_stack)

# 2. Horizontal Stacking (Column-wise) - Placing DataFrames side-by-side
df_bonus = pd.DataFrame({
    'Bonus': [1500, 2000]
})

horizontal_stack = pd.concat([df_q1, df_bonus], axis=1)
print("\n=== Horizontal Concatenation (Column-wise) ===")
print(horizontal_stack)