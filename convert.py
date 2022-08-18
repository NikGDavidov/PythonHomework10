
# import requests
# # 5D475AEG5V5443L0
# apy_key = "5D475AEG5V5443L0"
# url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo"
# r = requests.get(url)
# data = r.json()
# print (data)
# # print(data ["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

from google_currency import convert  

# Converted without comma like 70000.00 
def conv (cur,cur2,amount):

  num = int(amount)
  a = convert(cur, cur2, num) 
  b = a.split()
#   print(b)
#   print( b[5])
  result = b[5][1:-2]
  return result

