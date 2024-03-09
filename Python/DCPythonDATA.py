import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    data = pd.read_csv('student_spending.csv')
    #print(data.head()) #this shows the first 5 rows of data
    plot_major_income(data)
    plot_income_to_aid(data) #you have to close the first window to see the second plot


def plot_major_income(dataIn):
    major_income_data = dataIn[['major', 'monthly_income']]
    #print(major_income_data.head())
    mean_major = major_income_data.groupby('major').mean() #mean of income grouped by major
    mean_major.plot(kind='bar', figsize=(10, 6))
    plt.title('Mean Monthly Income by Major')
    plt.xlabel('Major')
    plt.ylabel('Mean Monthly Income')
    plt.xticks(rotation=45)  # Rotate x-axis labels
    plt.tight_layout()  # labels were clipping
    plt.show()

def plot_income_to_aid(dataIn):
    income_aid_data = dataIn[['monthly_income', 'financial_aid']]
    plt.figure(figsize=(8, 6))
    plt.scatter(income_aid_data['monthly_income'], income_aid_data['financial_aid'])
    plt.title('Monthly Income vs. Financial Aid') 
    plt.xlabel('Monthly Income')
    plt.ylabel('Financial Aid')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
    exit
