import requests
import re

print("code started")
response = requests.get('https://inrdeals.com/dealer/lakme-cosmetic/tamil-nadu/lakme-showroom-in-chennai')

while True:

    saloon_shop=re.findall('<a\s*href\=\"([^>]*?)\s*\"\s*>\s*<h2\s*style\=\"[^>]*?\"\s*class\=\"[^>]*?\s*>\s*([^>]*?)<\/h2>\s*<\/a>',response.text)

    for a in saloon_shop:
     print(a[0])
     
     response1=requests.get(str(a[0]))
     shop_add=re.search('<div\s*class\=\"[^>]*?\>\s*<i\s*class\=\"[^>]*?\s*>\s*<\/i>\s*<\/div>\s*<div\s*class\=\"[^>]*?\s*>\s*([^>]*?)\s*<\/div>\s*',response1.text).group(1)
     shop_con=re.search('<i\s*class\=\"fa\s*fa\-phone\s*fa\-lg\"\s*>\s*<\/i>\s*<\/div>\s*([\w\W]*?)\s*<\/div>',response1.text).group(1)
     shop_con=re.sub('<[^>]*?>','',shop_con)
     shop_con=shop_con.replace('\n','')
     
     saloon_details=open('saloon.txt','a',encoding='utf-8')
     saloon_details.write(a[0]+'\t'+str(shop_add)+'\t'+str(shop_con)+'\n')
       
    
    if re.search('<a\s*class\=\"page\-link\"\s*href\=\"([^>]*?)\"\s*rel\=\"next\"',response.text):
        nextpagelink = re.search('<a\s*class\=\"page\-link\"\s*href\=\"([^>]*?)\"\s*rel\=\"next\"',response.text).group(1)
        print(nextpagelink)
        nextpagesource = requests.get(str(nextpagelink))
        response = nextpagesource
           
    else:
        break
        
saloon_details.close()
    
    
    
    
    
