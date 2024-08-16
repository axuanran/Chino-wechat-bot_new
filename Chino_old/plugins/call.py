
import yaml
from Chino_old.action_plugins import config
from Chino_old.another_action_base import get_roomNick_in_chatroom
from Chino_old.api_action import get_wxid_details

class call(): #称呼
    @staticmethod
    def data_name_write(name_write,name_write_call):
        conf=config.read("call")
        conf[name_write]=name_write_call
        config.write_yaml("call",conf)

    @staticmethod
    async def _a_ (msg_l:dict,an) -> str:
        wxid=msg_l["wxid"]
        wxid_group=msg_l["wxid_group"]

        if an.find('_a_') != -1 :
            wx_name=config.read("call")
            if wxid_group:
                wxid=wxid_group

                #    print(wx_name[wxid])
                if wxid in wx_name:
                    anr=an.replace('_a_',wx_name[wxid])

                #        print("有",anr)
                else:
                    #update_group_member_details(port,wxid,wxid_group)
                    wxid_de=await get_wxid_details(wxid_group)
                    nickName=wxid_de.data.nickName
                    #print(nickname)
                    anr=an.replace('_a_',nickName)
                #        print('无')
                return anr

        return an
    @staticmethod
    def name_write(msg_l):
        wxid=msg_l["wxid"]
        qu=msg_l["qu"]
        qu_data=qu.splitlines()
        #get_chatroom_details_all(wxid)
        if qu_data[1][:5] == "wxid_":
           wxid=qu_data[1]
        else:
            wxid=get_roomNick_in_chatroom(wxid,qu_data[1])
        if wxid is None:
            return "error"
        call.data_name_write(wxid,qu_data[2])

    @staticmethod
    def read_name_all(msg_l):
        data=config.read("call")
        data_json=yaml.dump(data, sort_keys=False, default_flow_style=False,allow_unicode=True)
        return data_json


# if __name__ =="__main__":
#     plugins_sql.inf("call",0.01,"zwx08","称呼")
#     qu_key.admin.write("call","&call",1,'{plugin}.call.name_write',1,"称呼写入")
#     qu_key.write("read_name_all","&c_all",0,"{plugin}.call.read_name_all",1,"所有称呼读取")
#     an_replace.write("call","_a_",1,"{plugin}.call._a_",1,"称呼替换")
#     config.first("call","""#wxid_: 称呼
# wxid_2eokvnwm9a5a22: 主人""")