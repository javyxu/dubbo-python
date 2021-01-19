# -*- coding: utf-8 -*-


from dubbo.client import DubboClient, ZkRegister, NacosRegister
import json
from dubbo.codec.encoder import Object

if __name__ == "__main__":
    dataQueryModel = Object("com.cloudwise.bdp.model.data.DataQueryModelConfig")
    dataQueryModel["pushdown"] = True
    dataQueryModel["limit"] = False
    dataQueryModel["params"] = {}
    dataQueryModel["sql"] = "SELECT view_1.id, view_1.repo FROM stream.test.test_ck AS view_1"
    
    dubbo_cli = DubboClient("DODB_GROUP/com.cloudwise.bdp.service.rpc.dubbo.IDataQueryModelService", 
                        version="1.0.0", 
                        dubbo_version="2.0.2",
                        host="10.0.2.167:18301")
    result = dubbo_cli.call('queryDataQueryModel', 
                            [110, dataQueryModel, True], 
                            timeout=3000)
    print(result)