#作用：保证数据的正确性

def make_averager():
    li = []
    def averager(value):
        li.append(value)
        total = sum(li)
        return total/len(li)
    return averager

#保证数据的正确性，li成为局部变量，如果写在函数外，一旦出现大量代码，可能会误写新的li把列表数据改变
avg = make_averager()
print(avg(1000)) # 1000
print(avg(1100)) #1050
