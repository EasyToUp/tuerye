# tuerye
* study python note

## 2022年09月11

![a0](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/20220912011414.png)  


![a](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/20220912011335.png)  
```py

code_ranks = [
  '贾惜春', '贾巧姐', '李纨',
  '秦可卿', '史湘云', '王熙凤',
  '薛宝钗', '林黛玉', '妙玉',
  '贾迎春', '贾宝玉', '探春'
]
chinese_ranks = [
  '林黛玉', '薛宝钗', '贾宝玉',
  '贾探春', '史湘云', '贾迎春',
  '贾惜春', '王熙凤', '贾巧姐',
  '李纨', '妙玉', '秦可卿'
]
math_ranks = [
  '王熙凤', '贾迎春', '妙玉',
  '林黛玉', '贾惜春', '贾巧姐',
  '贾探春', '史湘云', '秦可卿',
  '李纨', '薛宝钗', '贾宝玉'
]

# 定义函数，计算某个学生出现在倒数三名的总次数
def last_three(name):
  name_code_index = code_ranks.index(name) + 1
  name_chinese_index = chinese_ranks.index(name) + 1
  name_math_index = math_ranks.index(name) + 1
  global count 
  count = 0
  if name_code_index > 9:
    count = count + 1
  if name_chinese_index > 9:
    count = count + 1
  if name_math_index > 9:
    count = count + 1
    #print(count)
last_three('贾宝玉')
print('贾宝玉排在倒数三名的次数是', str(count))
last_three('秦可卿')
print('秦可卿排在倒数三名的次数是', str(count))

```

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/20220912011401.png)

```  python
# 题目难读懂，要写很多123这种浪费时间的事情
month = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
]
chinese_num = [
  '一',
  '二',
  '三',
  '四',
  '五',
  '六',
  '七',
  '八',
  '九',
  '十',
  '十一',
  '十二',
  
]

def translate(word):
  rank = month.index(word) + 1
  chinese_num_yue = chinese_num[rank]
  print(chinese_num_yue + '月')

translate('June')

```

## 2022年09月12
### notice

* 不要忘记调用函数！！！
* 先判断后判断写出来冗余程度有差异

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/b20220913122748.png)

```py
mount = 8848130
paper = 0.08
n=0
list = []
while paper < 8848130:
  paper = paper * 2
  n += 1
  list.append(n)
#
  #print(list)
a = list[-1]
#print(a)
print('需要对折' + str(a) + '次')

```


![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/c20220913122802.png)

```py
usernames = ['小贝', '闻闻', '黄帮主']
passwords = ['123', '520', '666']

def login(username, password):
  if username in usernames:
    n = usernames.index(username)
    print(n)
    m = passwords[n]
    print(m)
    if m == password:
      print(username + '登录成功')
    else:
      print('密码错误')
  else:
    print('账号不存在')
# 使用 input() 函数输入账号密码
username = input('请输入账号:')
password = input('请输入密码:')
# 将账号密码传入 login() 函数判断是否可以登录
login(username, password)
```


![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/a20220913122731.png)

```py

# 有了下面这行代码，get_num() 函数才有效
# 千万不要手滑删除啦！
from random import randint
lottery = []

# 不需要修改函数，按照提示调用即可
def get_num():
  i = 1
  while i <= 6:
    number = randint(0, 99) 
    print(number)
    i += 1
    lottery.append(number)
get_num()    
print(lottery)
#  return randint(0, 99)



# 请你补全代码
# 用循环获得 6 个随机数存到 lottery 里作为中奖号码


# 打印出最终的 lottery 列表
print('本期彩票中奖号码为：'+ str(lottery))
```