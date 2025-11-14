import numpy as np
import csv
data=[]
with open("sensor_data.csv","r") as file:
    for line in file:
        row=line.strip().split(",")
        data.append(row)
arr=np.array(data,dtype=float)
arr[arr==-999]=np.nan
arr[(arr<0)|(arr>100)]=np.nan
sensor_mean=np.nanmean(arr,axis=0)
hour_median=np.nanmedian(arr,axis=1)
inv_count=np.isnan(arr).sum(axis=0)
worst_sensor=np.argmax(inv_count)
min_val=np.nanmin(arr)
max_val=np.nanmax(arr)
arr_norm=(arr-min_val)/(max_val-min_val)
np.savetxt("sensor_data_normalized.csv",arr_norm,delimiter=",")
print("Worst sensor index: ",worst_sensor)