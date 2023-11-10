import pandas as pd
import matplotlib.pyplot as plt



# CSV File for Line Plot
file_path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\junaid-data-set.csv'
data = pd.read_csv(file_path)

# Data filter for specific countries and series
countries = ['Afghanistan', 'Pakistan', 'Maldives', 'Sri Lanka']
series = 'EG.ELC.ACCS.UR.ZS'
years = ['2003 [YR2003]', '2004 [YR2004]', '2005 [YR2005]', '2006 [YR2006]', '2007 [YR2007]', '2008 [YR2008]']

filtered_data = data[data['Country Name'].isin(countries) & (data['Series Code'] == series)]
filtered_data = filtered_data.set_index('Country Name')

# Transpose the data for plotting
filtered_data = filtered_data[years].transpose()


#line plot start
plt.figure(figsize=(12, 8))
for country in countries:
    plt.plot(filtered_data.index, filtered_data[country], label=country)

plt.xlabel('Year')
plt.ylabel('Approching to Electricity (%)')
plt.title('Approching to Electricity in Urban Areas Over Time (Line Graph)')
plt.grid(True)
plt.legend()
plt.show()
#line plot End





# CSV File for Scatter Plot
data = pd.read_csv('C:\\Users\\DELL\\OneDrive\\Desktop\\10-1310-data-interim-equality-impact-he-funding-figure-4.csv', skiprows=2)


# Extract the data for plotting
deciles = data['Decile']
men_income = data['Men']
women_income = data['Women']
# Create a figure and plot the scatter plot for income by decile
plt.figure(figsize=(10, 6))
# Scatter plot for men's income by decile
plt.scatter(deciles, men_income, label='Men', c='blue', marker='o', alpha=0.7)
# Scatter plot for women's income by decile
plt.scatter(deciles, women_income, label='Women', c='red', marker='x', alpha=0.7)
# Set plot labels and title for the scatter plot
plt.xlabel('Decile')
plt.ylabel('Income')
plt.title('Income by Decile for Men and Women (Scatter Plot)')
# Add a legend
plt.legend()

# Show the scatter plot
plt.tight_layout()
plt.show()
#Scattor Plot End



# CSV File for Bar Plot
df = pd.read_csv('C:\\Users\\DELL\\OneDrive\\Desktop\\Junaid Assignment\\20230816Rolling12MonthsofCashReceiptsBrokenDownbyMonth1.csv')

#column into numeric and commas remove
df['MeatIndustryCash'] = df['MeatIndustryCash'].str.replace(',', '').fillna(0).astype(int)
df['MiscAndMilkIndustryCash'] = df['MiscAndMilkIndustryCash'].str.replace(',', '').fillna(0).astype(int)
df['RadiologicalCash'] = df['RadiologicalCash'].str.replace(',', '').fillna(0).astype(int)
df['GovernmentCash'] = df['GovernmentCash'].str.replace(',', '').fillna(0).astype(int)

# Dates column as the index
#Bar Graph start
df.set_index('InvoiceMonth', inplace=True)
all_colors = ['green','red','orange','purple']
# Create the bar plot
ax = df.plot(kind='bar', stacked=True, figsize=(12, 8), color=all_colors)

# Customize the plot
ax.set_xlabel('Values')
ax.set_ylabel('Invoice Months')
ax.set_title('Rolling of 1 year of Cash Receipts BrokeDown')
ax.legend(title='Columns', loc='upper left')

ax.set_xlim(-0.5, len(df) - 0.5)
plt.show()
#Bar Graph end