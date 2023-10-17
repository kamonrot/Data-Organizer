import matplotlib.pyplot as plt
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
data_points = [15, 20, 10, 25]

plt.bar(categories, data_points)

plt.xlabel('Categories')
plt.ylabel('Number of Data Points')
plt.title('Bar Chart of Data Points in Categories')

# Add text labels on top of each bar
for i, value in enumerate(data_points):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.show()