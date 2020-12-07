from matplotlib import pyplot as plt

x_arr =  [x for x in range(0,11)]
y1_arr = [x/2 for x in x_arr]
y2_arr = [x/3 for x in x_arr]
y3_arr = [x**2/10 for x in x_arr]

print(x_arr)
print(y1_arr)

plt.plot(x_arr, y1_arr, label='y=x/2')
plt.plot(x_arr, y2_arr, label='y=x/3')
plt.plot(x_arr, y3_arr, label='y=x^2/10')

plt.grid()
plt.legend()

plt.title('Multiple Graphs')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.show()
