import requests
import pytest
import json
from epet_interface.common.jsonbykey import get_target_value
class GoodList():

    def dynamic_goods_list(self):
        '''
        :param gids
        :return: dict_gid{'gid':['标签1','标签2']}
        '''
        url="https://mall.api.epet.com/v3/goods/list/list.html?" \
            "do=dynamic&appname=epetmall&distinct_id=22990222799145077" \
            "&duuid=947BF6F5BAF24F009D9AACD774BC8072" \
            "&gids=184673%2C184679%2C110623%2C115476%2C149757%2C143487%2C184675%2C141995%2C205720%2C143459%2C143453%2C127621%2C125607%2C170114%2C117661%2C138009%2C100312%2C168186%2C146470%2C143473&hash=" \
            "&id_param=cateid_3555&iphone_model=iPhone7%2C2&page=1&passkey=9a8da164e500d34563903ba895df9a62&postsubmit=r9b8s7m4&system=ios&version=446"
        goodslist_re = requests.get(url)
        aa = json.loads(goodslist_re.text)
        dict_gid = {}
        # print(aa.keys())
        # print(goodslist_re.text)
        # print(get_target_value('label', aa, []))
        for i in aa['data']['lists']:
            gid = i['data']['gid']
            print(i['data']['gid'])
            bb = i['data']['activity']
            # print(bb)
            label = []
            for j in i['data']['activity']:
                print(j['label'])
                label.append(j['label'])
                dict_gid[gid]=label
        print(dict_gid)



aa = GoodList.dynamic_goods_list('self')