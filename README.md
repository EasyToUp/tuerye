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

## 2022年09月13

* notice 
  * 序列是啥？

```py
# 第二版，第一版没保存下来，可惜  
i = 1
while True:
  answer = input('章鱼哥在吗？回答在/不在')
  if answer == '在':
    if i <= 3:
      print('章鱼哥来了，等他走了再玩')
      i += 1
      continue
    else:
      print('派大星，明天见！')
  elif answer == '不在':
    if i <= 3:
      print('玩第' + str(i) + '次叫车游戏')
      i += 1
      continue
    else:
      print('派大星，明天见！')

# 第三版，第二版忘记加break了
i = 1
while True:
  answer = input('章鱼哥在吗？回答在/不在')
  if answer == '在':
    if i <= 3:
      print('章鱼哥来了，等他走了再玩')
      i += 1
      continue
    else:
      print('派大星，明天见！')
      break
  elif answer == '不在':
    if i <= 3:
      print('玩第' + str(i) + '次叫车游戏')
      i += 1
      continue
    else:
      print('派大星，明天见！')
      break

```


![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/hmbb20220915003442.png)



```py
# 这两行代码用于生成一个 4 位数的随机密码，请不要更改！
from random import randint
password = randint(1000, 9999)

# 用循环找出 password 中存储的值
#用 for循环 
'''
for i in range(1000,10000,1):
  if i == password:
    print  ('猜对啦，密码是' + str(i) )
    break
  else:
    i += 1
    continue
'''


#用 while 循环
'''i = 1000
while i != password:
  i += 1
print ('猜对啦，密码是' + str(i) )  
'''

m = [x for x in range(1000,10000) if x == password]
print ('猜对啦，密码是' + str(m[0]) )  
```

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/random20220915003621.png)


```py
for i in range(1,101,1):
  if i % 5 == 0 and i % 3 == 0:
    print ('FizzBuzz')
    i += 1
    continue
  elif i % 5 == 0 :
    print ('Buzz')
    i += 1
    continue
  elif i % 3 == 0 :
    print ('Fizz')
    i += 1
    continue
  else:
    print (str(i))
    i += 1
    continue

```

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/fizzbuzz_20220915003751.png)

```py
brush_num = 0
water_num = 0
bottle_num = 0

for i in range(1,500,1):
  for j in range(1,500,1):
    left_money = 500 - 85 * i - 55 * j
    if left_money % 40 == 0 and left_money > 0:
      brush_num = i
      water_num = j
      bottle_num = int(left_money / 40)
      print('电动牙刷-' + str(brush_num) + '，漱口水-' + str(water_num) + '，水杯-' + str(bottle_num))
      continue
  break
# try 2
result = 0
n = 1
m = 1

while n < 21:
  m = m * n
  result += m
  #print(m)
  #print(result)
  n += 1
print(result)

'''
while n < 21:
  for i in range(n,n+1,1):
    #print(i)
    m = m * i
    result += m
    #print(m)
    #print(result)
  n += 1
print(result)
'''

```

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/electricbrush_20220915003926.png)


## 2022年09月14
* notice 
  * 字符串题目都不难，课也短,繁琐比较

```py
# 有下面这行代码，random() 方法才会奇效，注意不要删掉它~
import random

roles = ['哆啦A梦', '迪迦奥特曼', '路飞', '苏大强', '容嬷嬷', '甄嬛', '谢耳朵']
spots = ['埃菲尔铁塔上', '地铁上', '大街上', '飞机上', '三里屯', '家里', '浴室里', '王者峡谷']
events = ['背课文', '高唱《死了都要爱》', '蹦极', '补暑假作业', '跳远', '开黑', '800米跑', '看《生活大爆炸》']

# 请仿照下面这行代码，生成列表 spots 和 events 的随机索引值
i_role = random.randint(0, len(roles) - 1)
i_spots = random.randint(0, len(spots) - 1)
i_events = random.randint(0, len(events) - 1)
#print(roles[i_role])
#print(spots[i_spots])
#print(events[i_events])
# 下面是老师写好的句子模板，请你用字符串格式化的方法向其中填入内容。
# 当然，你也可以 DIY 输出句子的格式哦！
print('我看到了一件怪事：%s在%s%s。' % (roles[i_role],spots[i_spots],events[i_events]))
```

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/random-stq20220915004432.png)


```py
homework = '''提起刘备、项羽和张飞，人们总是会联想到桃园三结义的故事。
东汉末年，朝廷腐败，民不聊生。
刘备、项羽和张飞想共同干一番事业，拯救陷入水深火热之中的百姓。
三人在桃园结为异姓兄弟，风雨同舟，肝胆相照，开创了蜀汉基业。'''


#print(homework.index('项'))
a = homework.index('项')
b = homework[a+1:].index('项')
print(a)
print(b)

while i in homework:
  if i == '项':       
    a = homework.index('项')
    b = homework[a+1:].index('项')
   
    new_homework = homework[:a] + '关' + homework[a+1:]
    #print(new_homework)

'''
for i in homework:
  if i == '项':
    print(homework.index('项'))
    #global new_homework
    a = homework.index('项')
    new_homework = homework[:a] + '关' + homework[a+1:]
    print(new_homework)
'''    
'''
for i in new_homework:
  if i == '项':
    a = new_homework.index('项')
    new1_homework = new_homework[:48] + '关' + homework[49:]
    print(new1_homework)
    '''
```
![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/guanyu_20220915004711.png)

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/Q_20220915004801.png)

![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/A_20220915004811.png)

### 2022年09月17-18 


![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/a20220919002542.png)

```py

# 赛亚人
class Saiyan:
  hair = '黑发'
  # 每个赛亚人战斗力不同
  def __init__(self, ATK):
    self.ATK = ATK

# 请在下方定义“超级赛亚人”类
class SuperSaiyan(Saiyan): 
  pass
  def hensin(self):
  # 超级赛亚人能够变身
    self.hair = '金发'
    self.ATK = self.ATK * 50
    # 变身后发色变为金色
    # 战斗力变为原来的 50 倍


# 卡卡罗特是超级赛亚人，初始战斗力为 25
kakarot = SuperSaiyan(25)
# 他是赛亚人
if isinstance(kakarot, Saiyan):
  print('卡卡罗特是赛亚人，长着一头{}'.format(kakarot.hair))
else:
  print('卡卡罗特不是赛亚人')
print('他的战斗力是 {}'.format(kakarot.ATK))

# 并且能通过变身提升战斗力
print('卡卡罗特伴随着一阵金光，开始变身！')
kakarot.hensin()
print('变身后的战斗力是 {}'.format(kakarot.ATK))


```


![b](https://raw.githubusercontent.com/EasyToUp/tuerye/main/doc/image/b20220919002556.png)

```py

key = 'R'
  card = random.choice(cards[key])
  print('恭喜抽到{}卡，你拿到的英雄是{}'.format(key,card))
  return key
  
while True:
 if draw_card2() == 'SSR':
  break
#  if key == 'SSR':
#    return
  
# 缓慢打印

'''def print_slowly(text, delay=0.1):
  # 在一行内逐字打印 text
  for letter in text:
    print(letter, end='')
    sleep(delay) # 每打印一个字，暂停 delay 秒
  print('')
  '''

```

```py

from random import randint

# 选手类
class Player:
  # 每当创建新对象，都自动为他登记信息
  def __init__(self, name, HP, ATK):
    self.name = name  # 为选手登记姓名
    self.HP = HP      # 为选手登记生命值
    self.ATK = ATK    # 为选手登记攻击力
    print('已成功登记信息')
    self.show_info()
    
  
  # 展示信息
  def show_info(self):
    print('+ {}\tHP: {}\tATK: {}\n'.format(self.name, self.HP, self.ATK))
    



  # 发动攻击
  def hit(self,target):
    print('>> 【{}】向【{}】发动攻击，\n'.format(self.name,target.name)
#    target.defend(self.AATK)

  # 防御攻击
  def defend(self,damage):
    if randint(0, 100) <= 20:
      print('>> 【{}】完美躲避了攻击！\n'.format(self.name))
    else:
      self.HP = self.HP - damage
      print('>> 【{}】收到了{}点伤害！\n'.format(self.name,damage))

# 实例化 Player 类，生成一个新的实例对象，赋值给变量 kakarot
kakarot = Player('卡卡罗特',100,25)
# 实例化 Player 类，生成一个新的实例对象，赋值给变量 piccolo
piccolo = Player('比克大魔王',100,25)
# 展开决斗
print('-'*32 + '\n')
while True:
  # 每回合开始，由卡卡罗特先发动攻击
  hit(kakarot,piccolo)
  # 判断此时决斗是否分出胜负
  if piccolo.HP <= 0:
    print('\n{}获胜'。format(kakarot.name))
    break
  # 若未分出胜负，则攻防交换，由比克大魔王发动攻击
  hit(piccolo,kakarot)
  # 判断此时决斗是否分出胜负
  if kakarot.HP <= 0:
    print('\n{}获胜'。format(piccolo.name))
    break
  # 每回合结束，打印出两人当前信息
  piccolo.show_info()
  kakarot.show_info()
  print('-'*32 + '\n')


```