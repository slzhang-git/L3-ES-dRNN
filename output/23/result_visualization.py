import pandas as pd
import os
import matplotlib.pyplot as plt

country_index = 1

ground_truth_path = os.path.realpath(os.getcwd() + '/../../data/' + 'MHL_test.csv')
ground_truth_path_country = os.path.realpath(os.getcwd() + '/../../data/' + 'MHL_name.csv')
# print(ground_truth_path)
ground_tr = pd.read_csv(ground_truth_path, header=None)
ground_tr_value = ground_tr[country_index].values
# print(ground_tr[28].values)
# print(len(ground_tr_value))

ground_tr_name = pd.read_csv(ground_truth_path_country, header=None)
ground_tr_name_value = ground_tr_name[country_index].values

print(ground_tr_name_value)
print(type(ground_tr_name_value))

DATA_PATH = 'w1e5.csv'
testDates_df = pd.read_csv(DATA_PATH, header=None)
# testDates_df.columns
# testDates_df.iloc[:,0]
# testDates=pd.to_datetime(testDates_df.iloc[:,0])
# print(testDates_df.values[2])

# print(range(testDates_df.values))


load_series = list()
for record in testDates_df.values:
    if record[0] == str(country_index):
        index = 3
        while index < len(record):
            load_series.append(float(record[index]))
            index = index + 4
        # print(type(record))
        # print(len(record))
        # print(record[0:2])
        # print(record[3:3:-1])
        # print(record)
        # load_series=load_series.append(record[3:3:-1])
        # print('22222222')
# print(load_series)
# print(len(load_series))

plt.plot(ground_tr_value, linestyle='solid', linewidth=1)  
plt.plot(load_series, linestyle='dotted', linewidth=1)  
plot_title = 'ground truth vs. forecast for the country of ' + str(ground_tr_name_value)
plt.title(plot_title)  
plt.xlabel('hours in the whole year of 2018')  

plt.ylabel('load, mwh')  
plt.legend(['ground truth', 'forecast'], loc='upper left')  
#plt.axis([0, 2000, 3000, 9000])
plt.show()  
