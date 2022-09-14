brush_num = 0
water_num = 0
bottle_num = 0

for i in range(0,500,1):
  for j in range(0,500,1):
    left_money = 500 - 85 * i - 55 * j
    if left_money % 40 == 0 and left_money > 0:
      brush_num = i
      water_num = j
      bottle_num = int(left_money / 40)
      print('电动牙刷-' + str(brush_num) + '，漱口水-' + str(water_num) + '，水杯-' + str(bottle_num))
      #continue
  #break