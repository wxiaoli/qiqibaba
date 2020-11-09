# coding=utf-8
import matplotlib.pyplot as plt
def plot_scatter(arr,colors):
    plt.figure(figsize=(15.0, 8.0)) #宽，高
    print('arr.shape: ',arr.shape)
    x = arr[:,0]
    y = arr[:,1]
    plt.scatter(x, y, c=colors, marker='+')
    plt.xticks(())
    plt.yticks(())
    plt.show()
