import requests
import json
class GoodsDetails(object):
    def goods_detail(self,gid):
        '''
        :param gid:
        :return: gid{gid:'优惠1','优惠2'}
        '''
        url="https://mall.api.epet.com/v3/goods/detail/main.html?do=getDynamic&appname=epetmall&distinct_id=22990222799145077&duuid=947BF6F5BAF24F009D9AACD774BC8072" \
            "&hash=&iphone_model=iPhone7%2C2&my_wid=1&passkey=d8e45e56e4cfcb9e9a0f4709847ef6dd&postsubmit=r9b8s7m4&system=ios&version=446&debug=1"+'&gid='+gid

        gooddetail = requests.get(url)
        aa = json.loads(gooddetail.text)
        try:
            for i in aa['data']['modules'][2]['items']:
                print(i)
        except KeyError:
            print(aa['msg'])

GoodsDetails.goods_detail('aa','110623')