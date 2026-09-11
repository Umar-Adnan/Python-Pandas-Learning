# 🐼 Python Pandas Mastery & Data Analysis Notes

A comprehensive, hands-on repository documenting my journey in learning and applying **Pandas** for modern data analysis, data cleaning, and manipulation using Python.

---

## 🛠️ Setup & Essential Dependencies

Before running the scripts in this repository, ensure you have Python installed along with the essential packages for handling spreadsheet and mathematical operations:

```bash
pip install pandas openpyxl scipy
```


## 🚀 Topics Covered

### 1. 🟢 Basics of Pandas & File I/O
* **DataFrame Core Operations:** Creating DataFrames, inspecting shape/structure using `df.info()` and `df.describe()`.
* **Exporting & Loading Datasets:** 
  * Reading and writing to **CSV**, **Excel (`.xlsx`)**, **JSON**, and **Text (`.tsv`)**.
  * Modern export best practices: Always use `index=False` during exports to prevent unwanted `Unnamed: 0` index columns.

---

### 2. 🧹 Data Cleaning & Missing Data Imputation
* **Handling Missing Values (`NaN`):**
  * Imputing numeric data using summary statistics (`fillna(mean())`, `fillna(median())`).
  * Imputing string/categorical data using `mode()[0]` or constant values (`'Unknown'`).
  * Forward and backward filling (`ffill()`, `bfill()`) for ordered datasets.
* **Interpolation Techniques:**
  * **Linear Interpolation:** Calculating straight-line midpoints between neighboring numeric values.
  * **Time-Based Interpolation:** Account for date-indexed spacing gaps.
  * **Polynomial Interpolation:** Smooth curve fitting (requires `scipy`).
* **Copy-on-Write Standard:** Avoiding `inplace=True` in favor of direct reassignments (`df['col'] = df['col'].fillna(...)`) to prevent `ChainedAssignmentError` in modern Pandas.

---

### 3. ✏️ Modifying & Transforming Data
* **Conditional Column Updating:** Changing specific column entries based on matching conditions using `.replace()`, `np.where()`, and `.loc[]`.
* **String Accessor Operations (`.str`):**
  * Whitespace stripping and case normalization (`.str.strip()`, `.str.title()`, `.str.lower()`).
  * Pattern searching and text filtering (`.str.contains()`, `.str.startswith()`).
  * Delimited text splitting into distinct DataFrame columns using `.str.split(expand=True)`.

---

### 4. 🔍 Selecting & Filtering Data
* **Conditional Masking:** Filtering rows based on single or multi-condition logic (`&`, `|`, `~`).
* **Index & Value Selection:** Accessing subsets using label-based indexing (`.loc[]`) and position-based indexing (`.iloc[]`).
* **Category Filtering:** Using `.isin()` to filter across multiple target values cleanly.

---

### 5. 📊 Aggregation & Grouping Operations
* **Built-in Metrics:** Extracting `mean`, `median`, `std`, `min`, `max`, `count` (ignores `NaN`), and `size` (includes `NaN`).
* **Grouped Analysis (`.groupby`):** Implementing the **Split-Apply-Combine** pattern to aggregate metric breakdowns across categories.
* **Custom Aggregations (`.agg`):** Computing multiple custom metrics across distinct columns simultaneously.

---

### 6. 🔗 Merging, Joining & Stacking
* **Value-Based Merges (`pd.merge`):** Combining relational datasets across **Inner**, **Left**, **Right**, and **Outer** join types.
* **Index-Based Joins (`df.join`):** Merging datasets on matching row indices.
* **Dataset Stacking (`pd.concat`):** Concatenating DataFrames vertically (row-wise) or horizontally (column-wise).

---

### 7. ⚡ Advanced Techniques & Workflow Efficiency
* Encoding strategies for categorical data handling.
* Memory management techniques for handling larger datasets efficiently.
* Git workflows for staging, tracking, and committing multiple analysis scripts (`git add .`, `git commit -m "..."`).


## 📈 Next Steps
* Transition into **Data Visualization** using `matplotlib` and `seaborn`.
* Explore **Exploratory Data Analysis (EDA)** on real-world datasets.
