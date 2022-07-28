import requests
import re
import time
import urllib3

# import json


urllib3.disable_warnings()
ServerData = []
ServerPath_dispose = []
ServerPath = []
ServerInformation = []
ServerName = []
ServerPort = []
ServerRemark = []
ServerInformation_PlayerCount = []
ServerInformation_MaxPlayer = []
ServerInformation_Version = []
NowTime = 0
ServerState = []

# 在这里配置数据！
OutTime = 5  # 超时时间
Verify = False  # 是否证书检查
Runtimes = 3  # 循环次数
TimeInterval = 10.0  # 间隔秒数


# 获取时间
def gettime():
    global NowTime
    time_tuple = time.localtime(time.time())
    NowTime = "{}年{}月{}日 {}:{}".format(time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4],
                                       time_tuple[5], time_tuple[6])


# 爬取网页
def getserverdata():
    global ServerPath
    global ServerPathCouCount
    global ServerData
    global ServerPath_dispose
    global CloseServer
    global ServerState
    global OutTime
    global Verify

    for x in range(ServerPathCouCount):
        ServerPath_dispose.append("https://" + str(ServerPath[x]) + ":" + str(ServerPort[x]) + "/status/server")
        # print(ServerPath_dispose[x])
        x = x + 1
    # print(ServerPath)

    for z in range(ServerPathCouCount):
        try:
            print("正在获取服务器状态" + str(z) + "/" + str(ServerPathCouCount))
            ServerData.append(
                requests.get(ServerPath_dispose[z], timeout=OutTime, verify=Verify).content.decode())  # 关闭证书检测 超时3s

        except:
            ServerState.append("0")
            ServerData.append("")
            z = z + 1
            continue

        z = z + 1
        ServerState.append("1")
    # print(ServerData)


# 获取服务器数据
def getserverinformation():
    global ServerPath
    global ServerPathCouCount
    global ServerData
    global ServerInformation_PlayerCount
    global ServerInformation_Version
    global ServerInformation_MaxPlayer

    for z in range(ServerPathCouCount):
        ServerInformation_PlayerCount.append(''.join(re.findall(r'playerCount":(.*),"maxPlayer":', ServerData[z])))
        ServerInformation_MaxPlayer.append(''.join(re.findall(r',"maxPlayer":(.*),"version":"', ServerData[z])))
        ServerInformation_Version.append(''.join(re.findall(r',"version":"(.*)"}}', ServerData[z])))
        if ServerInformation_MaxPlayer[z] == "-1":
            ServerInformation_MaxPlayer[z] = "∞"
        z = z + 1


def printserverinformation():
    global ServerPathCouCount
    global ServerState
    global ServerName
    global ServerPath
    global ServerPort
    global ServerInformation_Version
    global ServerInformation_PlayerCount
    global ServerInformation_MaxPlayer
    global ServerRemark

    gettime()

    print("当前时间为：" + str(NowTime))

    print("当前服务器状态：\n")
    print("开启的服务器")
    for a in range(ServerPathCouCount):

        if ServerState[a] == "1":
            print(a + 1, end='')
            print(",{}：{}(服务器在线)".format(str(ServerName[a]), str(ServerPath[a])))
            print("端口:" + ServerPort[a])
            print("游戏版本：" + ServerInformation_Version[a])
            print("在线玩家：" + str(ServerInformation_PlayerCount[a]) + "/" + str(ServerInformation_MaxPlayer[a]))
            print("备注：\n" + ServerRemark[a] + "\n\n")
        else:
            print(a + 1, end='')
            print(",{}：{}(服务器离线)".format(str(ServerName[a]), str(ServerPath[a])))
            print("游戏版本：x.x.x")
            print("备注：\n" + ServerRemark[a] + "\n\n")
        a = a + 1


# def writeserverlist():
#    global ServerPathCouCount
#    global ServerName
#    global ServerPath
#    jsontext = {'points': []}
#    jsondata = json.dumps(jsontext, indent=4, separators=(',', ': '))
#    for index,row in subdf.iterrows():
#        jsontext['Server'].append({'Name': ServerName[z], 'Path': ServerPath[z]})
#
#    f = open('ServerList.json', 'w')# 创建配置文件
#    f.write(jsondata)
#    f.close()


# 在这里写网址

# 服务器列表
ServerPath.append("xx.xxxxx.cn")  # 地址
ServerName.append("Kawaa的服务器")  # 名称
ServerPort.append("54321")  # 端口
ServerRemark.append("")

ServerPath.append("111.222.333.44")
ServerName.append("Kawaa的服务器")
ServerPort.append("15212")
ServerRemark.append("")

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓以此类推


ServerPathCouCount = len(ServerPath)


for c in range(Runtimes):
    getserverdata()
    getserverinformation()
    printserverinformation()
    time.sleep(TimeInterval)




input("输入任意键退出")

# print(ServerInformation_PlayerCount)
# print(ServerInformation_MaxPlayer)
# print(ServerInformation_Version)
