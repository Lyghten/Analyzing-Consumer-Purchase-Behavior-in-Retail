plt.figure(figsize=(10, 6))
sns.boxplot(x='Income_Level', y='Purchase_Amount', data=data)
plt.title('Purchase Amount by Income Level')
plt.xlabel('Income Level')
plt.ylabel('Purchase Amount')
plt.show()