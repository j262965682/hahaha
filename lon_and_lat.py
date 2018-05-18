
'''
利用高德地图api实现地址和经纬度的转换
'''
import requests
from  urllib.request import urlopen,quote

def geocode(address):
        #address = quote(address)
        output = 'json'
        parameters = {'address': address, 'key': 'ecfd34e614ece8f47967502f69002f7b','output':output}
        param_query = {'keywords':address, 'key': 'ecfd34e614ece8f47967502f69002f7b'}
        try:

            #tips = 'http://restapi.amap.com/v3/assistant/inputtips'
            base = 'http://restapi.amap.com/v3/geocode/geo'
            response = requests.get(base, parameters)
            answer = response.json()
            print(answer['geocodes'][0]['location'])
        except Exception:
            query = 'http://restapi.amap.com/v3/place/text'  # ?key=申请的开发者key&children=1&offset=20&page=1&extensions=base'
            param_query = {'keywords': address, 'key': 'ecfd34e614ece8f47967502f69002f7b'}
            response_cearch = requests.get(query, param_query)
            response_query = response_cearch.json()
            print(response_query['pois'][0]['location'])



        #answer = response.json()
        #answer_tips = response_tips.json()
        #response_query = response_cearch.json()
        #print( answer['geocodes'][0]['location'])
       # print(answer)
        #print(answer_tips)
        #print(response_query)
geocode('杭州市')