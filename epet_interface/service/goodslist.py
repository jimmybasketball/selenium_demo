import requests
import pytest
import json
from epet_interface.common.jsonbykey import get_target_value
class GoodList():

    def dynamic_goods_list(self,gids):
        '''
        :param gids
        :return: dict_gid{'gid':['标签1','标签2']}
        '''
        url="https://mall.api.epet.com/v3/goods/list/list.html?do=dynamic&gids="
        for gid in gids:
            url = url+str(gid)+','
        print(url)
        goodslist_re = requests.get(url)
        aa = json.loads(goodslist_re.text)
        dict_gid = {}
        try:
            for i in aa['data']['lists']:
                gid = i['data']['gid']
                if 'activity' in i['data']:
                    bb = i['data']['activity']
                    label = []
                    for j in bb:
                        # print(j['label'])
                        label.append(j['label'])
                        dict_gid[gid]=label
        except KeyError:
            print("接口返回参数错误")
        print(dict_gid)



aa = GoodList.dynamic_goods_list('self',[184673,184679,110623,115476])