# Sales_Data_Project
Project in Data Analytics using fictional sales data with Excel, SQL and Python. (Version for Potential Recruiters). 

# Sales Data Analytics Project
### Data Exploration and Analysis with Excel, SQL, and Python

This project involves a comprehensive exploratory data analysis (EDA) of a fictional sales dataset. The primary goal was to process raw data, extract meaningful insights, and visualize key trends using a combination of industry-standard tools.

### Data Cleaning & Preprocessing
* **Excel:**
    * Performed initial data inspection and cleansing.
    * Standardized text formats (e.g., `UPPER()` for name casing in `CustomerID` column).
    * Identified and imputed missing `Quantity` values by deriving them from `TotalAmount` and `UnitPrice`.
    * Extracted address components (`City`, `State`, `Zip Code`) into separate columns.
    * Created a calculated column for monthly sales trends.
    * Identified and removed duplicate records to ensure data integrity.
    * Sorted customer records for organized analysis.

### Key Insights & Visualizations (Excel)
* **Product Category Revenue:** A column chart (Excel Sheet 3) clearly illustrates that 'Electronics' is the dominant product category, contributing approximately 85% of total revenue.
* **Monthly Sales Performance:** A line graph (Excel Sheet 8) visualizes month-over-month sales trends, depicting both the total sum of orders and the number of distinct customer orders per month.

### SQL Data Querying
* Employed SQL (via SQLite, managed within a Python environment) for efficient data extraction and aggregation.
* Executed queries involving `SELECT`, `FROM`, `WHERE`, `GROUP BY`, and `SUM`.

### Python for Data Processing & Analysis
* Developed a Python script (`sohrab.py`) utilizing the **Pandas** library for robust data manipulation, including:
    * Loading `sales_data_clean.csv` into a DataFrame.
    * Calculating aggregate statistics (e.g., total sales, number of unique customer orders).
    * Analyzing sales performance by `ProductCategory`.
* Integrated **SQLite3** within the Python script to create and interact with a local sales database, demonstrating database creation and basic data loading from CSV.
* Generated console outputs to summarize key findings, such as total sales, unique customer counts, and sales distribution by category.

### Tools Used
* **Excel:** Data Cleaning, Transformation, Reporting, Visualization
* **Python:** Pandas (Data Manipulation), SQLite3 (Database Interaction)
* **SQL:** Querying, Aggregation
* **GitHub:** Version Control, Project Hosting
* **VS Code:** Integrated Development Environment
* **SQLTools:** VS Code Extension for SQL querying

### How to View
Explore the project files in this repository:
* `sohrab.py`: Contains the Python code for data processing and SQLite database creation.
* `sales_data_clean.csv`: The cleaned dataset used for analysis.
* `Workingwithdataset.xlsx`: The Excel workbook demonstrating data cleaning and initial visualizations.
* `Sales Data.session.sql` (if uploaded): SQL queries used for data extraction and analysis.

