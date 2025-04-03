# Retail Transaction Data Analysis

## Overview
This project analyzes retail transaction data and customer purchase behavior to identify patterns, trends, and outliers. The analysis includes data cleaning, exploratory data analysis (EDA), and visualization of key metrics.

## Dataset
The analysis uses two main datasets:
1. `QVI_transaction_data.csv` - Contains transaction details including:
   - Transaction date and ID
   - Product information (name, quantity, size)
   - Sales amounts
   - Store and loyalty card numbers

2. `QVI_purchase_behaviour.csv` - Contains customer demographic information:
   - Loyalty card number
   - Life stage (e.g., "YOUNG SINGLES/COUPLES")
   - Premium customer status (e.g., "Premium", "Mainstream")

## Analysis Steps

### 1. Data Preparation
- Merged transaction and customer behavior data
- Cleaned product names and extracted:
  - Brand names
  - Package sizes (in grams)
- Handled missing values
- Converted date formats

### 2. Exploratory Data Analysis
Key analyses performed:
- Sales trends over time
- Top performing brands by sales
- Package size distribution
- Outlier detection in sales amounts
- Customer segmentation analysis

### 3. Key Visualizations
The notebook includes several visualizations:
- Time series of total sales
- Bar charts of top brands
- Histograms of package sizes
- Boxplots for outlier detection
- Scatterplots of sales distribution

## Key Findings
1. **Sales Patterns**: Identified seasonal trends in transaction data
2. **Top Brands**: Smiths, Doritos, and Kettle emerged as top brands
3. **Package Sizes**: Most products fall in the 150-200g range
4. **Outliers**: Detected and analyzed transactions with unusually high sales amounts
5. **Customer Segments**: Premium customers show different purchasing patterns

## Technical Details
- **Language**: Python
- **Libraries**:
  - pandas (data manipulation)
  - numpy (numerical operations)
  - matplotlib/seaborn (visualization)
- **Analysis Techniques**:
  - IQR method for outlier detection
  - Time series analysis
  - Customer segmentation

## How to Use
1. Clone this repository
2. Install required packages: `pip install pandas numpy matplotlib seaborn`
3. Run the Jupyter notebook: `jupyter notebook Data_Analysis.ipynb`
4. The notebook will guide you through the analysis steps

## Future Work
Potential extensions of this analysis:
- Customer lifetime value prediction
- Market basket analysis
- Price elasticity modeling
- Promotion effectiveness analysis

## License
This project is licensed under the MIT License - see the LICENSE file for details.
