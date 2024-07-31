import pandas as pd
file_path = "D:\Slot-D\ML Practical\day1.6.csv"
data = pd.read_csv(file_path)
print("First five rows of the dataset:")
print(data.head())
X = data.iloc[:, :-1].values 
y = data.iloc[:, -1].values  
hypothesis = ['0'] * X.shape[1]
for i in range(len(y)):
    if y[i] == 'Yes':  
        for j in range(X.shape[1]):
            if hypothesis[j] == '0':
                hypothesis[j] = X[i][j]
            elif hypothesis[j] != X[i][j]:
                hypothesis[j] = '?'
print("Most specific hypothesis:")
print(hypothesis)
