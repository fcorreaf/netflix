from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

ntf = pd.read_csv("../csv/NFLX.csv")
dj = pd.read_csv("../csv/DJI.csv")
ntf_q = pd.read_csv("../csv/NFLX_daily_by_quarter.csv")
#print(ntf.head(5))
#print(dj.head(5))
#print(ntf_q.head(5))
print(dj.info())
print(ntf.info())

# renombrar las columnas
ntf = ntf.rename(columns={'Adj Close': 'Price'})
dj = dj.rename(columns={'Adj Close': 'Price'})
ntf_q = ntf_q.rename(columns={'Adj Close': 'Price'})

sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(15, 10))
#sns.barplot(x="Date", y="Price", data=ntf)
#sns.boxplot(x="country", y="loan_amount", data=df)
#sns.violinplot(x="Quarter", y="Price", data=ntf_q, split=False)
sns.violinplot(ntf_q['Price'], color="red")
plt.xlabel("Price")
plt.title("Distribution of 2017 Netflix Stock Prices by Quarter")
plt.savefig("../graph/Distribution of 2017 Netflix Stock Prices by Quarter.png")
plt.show("../graph/Distribution of 2017 Netflix Stock Prices by Quarter.png")


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q 2017", "2Q 2017", "3Q 2017", "4Q 2017"]
earnings_actual = [.4, .15, .29, .41]
earnings_estimate = [.37, .15, .32, .41]

plt.scatter(x_positions, earnings_actual,  color="red", alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color="blue", alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")
plt.savefig("../graph/Earnings Per Share in Cents.png")
plt.show("../graph/Earnings Per Share in Cents.png")


revenue_by_quarter = [2.79, 2.98, 3.29, 3.7]
earnings_by_quarter = [.0656, .12959, .18552, .29012]
quarter_labels = ["2Q 2017", "3Q 2017", "4Q 2017", "1Q 2018"]

#def create_x(t, w, n, d):
#    return [t*x + w*n for x in range(d)]
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.9 # Width of each bar
bars1_x = [2 * x + 0.9*1 for x in range(4)]

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.9 # Width of each bar
bars2_x = [2 * y + 0.9 * 2 for y in range(4)]

plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)
middle_x = [(revenue_by_quarter + earnings_by_quarter) / 2 for revenue_by_quarter, earnings_by_quarter in zip(bars1_x, bars2_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(quarter_labels)
plt.legend(["Revenue", "Earnings"])
plt.title("Netflix Revenue and Earnings in Billions ($)")
plt.xlabel("Quarter 2017")
plt.ylabel("Average")
plt.savefig("../graph/Netflix Revenue versus Earnings 2017.png")
plt.show("../graph/Netflix Revenue versus Earnings 2017.png")


# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
#plt.plot(ntf.Date, ntf.Price, color='blue')
plt.plot(ntf['Date'], ntf['Price'], color="blue", marker= 's')
plt.xticks(rotation='vertical')
plt.title('Netflix Subplot')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.subplots_adjust(wspace=0.5)
ax1.set_xticks(range(len(ntf.Date)))
ax1.set_xticklabels(ntf.Date, rotation = 90)
plt.grid(True, color=[0.8, 0.8, 0.8])

# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
#plt.plot(dj.Date, dj.Price, color='red')
plt.plot(dj['Date'], dj['Price'], color="red", marker='s')
plt.xticks(rotation='vertical')
plt.title('DJ Subplot')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.subplots_adjust(wspace=0.5)
ax2.set_xticks(range(len(dj.Date)))
ax2.set_xticklabels(dj.Date, rotation = 90)
plt.grid(True, color=[0.8, 0.8, 0.8])
plt.savefig("../graph/Netflix_DJ_StockPrice_2017.png")
plt.show("../graph/Netflix_DJ_StockPrice_2017.png")


