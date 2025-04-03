# %%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\mosta\Downloads\quantium\QVI_transaction_data.csv")
df2 = pd.read_csv(r"C:\Users\mosta\Downloads\quantium\QVI_purchase_behaviour.csv")
df2

# %%
#DATA_cleaning
df.dropna(inplace=True)
df['DATE'] = pd.to_datetime(df['DATE']) 
df["PACK_SIZE"] = df["PROD_NAME"].str.extract(r'(\d{2,3})g').astype(float)
df["BRAND"] = df["PROD_NAME"].str.split().str[0]
# Merge transaction data with purchase behavior data on LYLTY_CARD_NBR
merged_data = df.merge(df2, on="LYLTY_CARD_NBR", how="left")
merged_data.head()


# %%
df.sort_values(by=['TOT_SALES'], ascending=False, inplace=True)
df.head(20)

# %%
# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df["TOT_SALES"].quantile(0.25)
Q3 = df["TOT_SALES"].quantile(0.75)
IQR = Q3 - Q1  # Interquartile Range

# Define the outlier thresholds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = df[(df["TOT_SALES"] < lower_bound) | (df["TOT_SALES"] > upper_bound)]
print("Outliers detected using IQR method:")
print(outliers)


# %%
df ['PROD_NAME'] = df['PROD_NAME'].str.strip().copy()
df['PROD_NAME'] = df['PROD_NAME'].str.replace('\'', '')
df['PROD_NAME'] = df['PROD_NAME'].str.replace('\"', '')

# %%

# Set style
sns.set_style("whitegrid")

# 1. Sales Trend Over Time
plt.figure(figsize=(12, 6))
merged_data.groupby("DATE")["TOT_SALES"].sum().plot()
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

# 2. Top 10 Brands by Total Sales
top_brands = merged_data.groupby("BRAND")["TOT_SALES"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_brands.index, y=top_brands.values, palette="viridis")
plt.title("Top 10 Brands by Total Sales")
plt.xlabel("Brand")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# 3. Pack Size Distribution
plt.figure(figsize=(12, 6))
sns.histplot(merged_data["PACK_SIZE"], bins=20, kde=True)
plt.title("Distribution of Pack Sizes")
plt.xlabel("Pack Size (grams)")
plt.ylabel("Count")
plt.show()


# %%
# Identify outliers in TOTAL SALES using IQR method
Q1 = merged_data["TOT_SALES"].quantile(0.25)
Q3 = merged_data["TOT_SALES"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
outliers = merged_data[(merged_data["TOT_SALES"] < lower_bound) | (merged_data["TOT_SALES"] > upper_bound)]

# Plot the distribution with outliers
plt.figure(figsize=(12, 6))
sns.boxplot(x=merged_data["TOT_SALES"])
plt.title("Boxplot of Total Sales (Identifying Outliers)")
plt.xlabel("Total Sales")
plt.show()

# Display summary of outliers
outliers.describe()


# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Identify outliers in TOTAL SALES using IQR method
Q1 = merged_data["TOT_SALES"].quantile(0.25)
Q3 = merged_data["TOT_SALES"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
outliers = merged_data[(merged_data["TOT_SALES"] < lower_bound) | (merged_data["TOT_SALES"] > upper_bound)]

# Plot the distribution with outliers
plt.figure(figsize=(12, 6))
sns.boxplot(x=merged_data["TOT_SALES"])
plt.title("Boxplot of Total Sales (Identifying Outliers)")
plt.xlabel("Total Sales")
plt.show()

# Display summary of outliers
print(outliers.describe())


# %%

plt.figure(figsize=(12, 6))

# Boxplot with log scale
sns.boxplot(x=np.log1p(merged_data["TOT_SALES"]))  # Using log transformation
plt.title("Boxplot of Total Sales (Log Scale for Clarity)")
plt.xlabel("Log(Total Sales + 1)")
plt.show()

# Histogram with KDE to see distribution
plt.figure(figsize=(12, 6))
sns.histplot(merged_data["TOT_SALES"], bins=50, kde=True, color="blue")
plt.axvline(lower_bound, color="red", linestyle="dashed", label="Lower Bound")
plt.axvline(upper_bound, color="red", linestyle="dashed", label="Upper Bound")
plt.title("Histogram of Total Sales with Outlier Thresholds")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Swarmplot (shows individual points clearly, may need sampling for large data)
plt.figure(figsize=(12, 6))
sns.stripplot(x=merged_data["TOT_SALES"], jitter=True, alpha=0.5)
plt.title("Scatterplot of Total Sales")
plt.xlabel("Total Sales")
plt.show()



