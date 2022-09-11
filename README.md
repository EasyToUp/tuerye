# tuerye
* study python note

## 20220911

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