def calc_loan(p,n,r=0.0052):
  hk = p * ((r * (1 + r)**n) / ((1 + r)** n -1))
  return hk

print (calc_loan(200,30*12))