
import json

class jxkh_item:
    name = "default"
    Rank = [("S","A","B","C"),("S","A","B","B"),("B","A","B","C"),("B","C","B","B")]
    KQ = 10.0
    AW = 5.0

def jxkh_item_to_json(item):
    return{"name":item.name,"Rank":item.Rank,"KQ":item.KQ,"AW":item.AW}

def json_to_jxkh_item(d):
    item = jxkh_item()
    item.name = d["name"]
    item.Rank = d["Rank"]
    item.AW = d["AW"]
    item.KQ = d["KQ"]
    return item

def load_config():
    config = open("..\\resources\\jxkh\\config.json", "r")
    jsonobj = json.load(config)
    #print(jsonobj)
    return jsonobj

def load_content(contentname):
    content = open("..\\resources\\jxkh\\"+contentname, "r")
    #print(content)
    json_content = json.load(content)
    itemlist = list()
    for item in json_content["content"]:
        itemlist.append(json_to_jxkh_item(item))
    return itemlist,json_content["version"]

def save_content_template():
    templatefile = open("..\\resources\\jxkh\\content_template.jxkh","a")
    item_list = [jxkh_item(), jxkh_item(),jxkh_item(),jxkh_item()]
    json.dump(jxkh_item(),templatefile,default = jxkh_item_to_json)
    return

def handle_jxkh_item(config, item):
    KPIScore = 0.0
    for rank in item.Rank:
        KPIIndex = 0
        for KPI in rank:
            KPIScore += config["Rank"][KPI] * config["KPIWeight"][KPIIndex]
            KPIIndex += 1
    KPIScore /= len(item.Rank)
    final_score = item.KQ + item.AW + (100.0 - config["KQ"] - config["AW"])/100.0 * KPIScore
    return final_score

def handle_jxkh(config, itemlist):
    score_dic = {}
    for item in itemlist:
        score_dic[item.name] = handle_jxkh_item(config, item)
    sorted_totalscore = sorted(score_dic.items(), key = lambda d: d[1], reverse = True)
    return sorted_totalscore

def jxkh_main():
    print("jxkh_main")
    jsonconfig = load_config()
    itemlist, version = load_content(jsonconfig["contentfile"])
    #save_content_template()
    sorted_totalscore = handle_jxkh(jsonconfig[version], itemlist)
    print(sorted_totalscore)
    return
