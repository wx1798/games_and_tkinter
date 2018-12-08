from tkinter import *
from tkinter import messagebox
import urllib.request
import requests
def weather():
    city = entry.get()
    if city == "":
        messagebox.showinfo('提示', '请输入要查询的城市')
    else:
        city = urllib.request.quote(city)
        host = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
        appcode = '8c42c716b4484ee3a01e2d3fdcf1c7bf'
        querys = 'city='+city
        url = host + '?' + querys
        header = {'Authorization': 'APPCODE ' + appcode}
        info = requests.get(url, headers=header).json()['result']
        # 删除上一行
        lis.delete(0, END)
        lis.insert(0, '星期:%s' % info['week'])
        lis.insert(1, '天气:%s' % info['weather'])
        lis.insert(2, '温度:%s' % info['temp'])
        lis.insert(3, '风向:%s' % info['winddirect'])
# 创建窗口
root = Tk()
# 标题
root.title('天气查询')
# 窗口位置
root.geometry('500x400+500+300')
# 标签控件
lable = Label(root, text='请输入查询城市:')
# 定位 布局 pack place
lable.grid(row=0, column=0)
# 输入控件
entry = Entry(root, font=('微软雅黑', 23))
entry.grid(row=0, column=1)
# 列表框控件
lis = Listbox(root, font=('微软雅黑', 15), width=40, height=10)
# 跨列合并
lis.grid(row=1, columnspan=2)
# command点击触发方法
button = Button(root, text='查询', width=10, command=weather)
# sticky对齐方式WENS
button.grid(row=2, column=0, sticky=W)
button1 = Button(root, text='退出', width=10, command=root.quit)
button1.grid(row=2, column=1, sticky=E)
# 显示
root.mainloop()