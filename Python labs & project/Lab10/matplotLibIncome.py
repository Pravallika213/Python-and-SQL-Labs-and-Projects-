import matplotlib.pyplot as plt

# Input data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create pie chart
plt.figure(figsize=(8, 8))  # Adjust the figure size if necessary
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)

# Add title
plt.title('Distribution of Monthly Income by Source')

# Show plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
