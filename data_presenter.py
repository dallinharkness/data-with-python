invoices = open('CupcakeInvoices.csv')


for data_per_line in invoices:
    print(data_per_line)

# for data_per_line in invoices:
#     values = data_per_line.split(',')
#     print(values[2])


# for data in invoices:
#     values = data.split(',')#this line takes out the commas to giev each element an index
#     total = int(values[3]) * float(values[4])
#     print(total)
# total = 0
# for data in invoices:
#     values = data.split(',')
#     total = total + (int(values[3]) * float(values[4]))

# print(total)

invoices.close()


import matplotlib.pyplot as plt

x = ['Chocolate', 'Strawberry', 'Vanilla']
y = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
plt.plot(x,y)




plt.show()
