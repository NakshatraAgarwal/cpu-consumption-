import matplotlib .pyplot as plt
import psutil as p

app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count + 1
    if count <= 6:
        n = process.name()
        use = p.cpu_percent()
        app_name_dict.update({n:use})
        print("name:",n," CPU usage:", use)
        
        

keymax = max(app_name_dict, key=app_name_dict.get)
print(keymax)
keymin = min(app_name_dict, key = app_name_dict.get)
print(keymin)

name_list = [keymax,keymin]

cpusage = app_name_dict.values() 

maxm = max(cpusage)
print("Maximum",maxm)
minm = min(cpusage)
print("Minimum",minm)
maxmin = [maxm, minm]
print(name_list)
print(maxmin)

plt.figure(figsize = (40,28))
plt.xlabel("Names")
plt.ylabel("CPU Usage")
plt.bar(name_list,maxmin, width = 0.6, color = ("red","orange","yellow","green","blue","pink"))
plt.show()