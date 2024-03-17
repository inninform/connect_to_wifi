import os

def getMenuWifi():
    command = "netsh wlan show networks interface=Wi-fi"
    os.system(command)


def getNP():
    WName = input("enter the name of wifi : ")
    WPassword = input("enter the password of wifi : ")
    return WName, WPassword


def createNewConnection(name, SSID, password):
        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>""" + name + """</name>
        <SSIDConfig>
            <SSID>
                <name>""" + SSID + """</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>""" + password + """</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
        command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
        with open(name + ".xml", 'w') as file:
            file.write(config)
            os.system(command)


def cnc():
    wifiname, wifipass = getNP()
    createNewConnection(wifiname, wifiname, wifipass)
    command = "netsh wlan connect name=\"" + wifiname + "\" ssid=\"" + wifiname + "\" interface=Wi-Fi"
    os.system(command)


def ent():
    inp = input(">>> ")
    if (inp == "help"):
        print("cws : connect with the networks saved")
        print("sap : show all profiles")
        print("sps : show the profiles saved")
    if (inp == "cws"):
        cnc()
    if (inp == "sap"):
        getMenuWifi()
    if (inp == "sps"):
        cmdWN = os.system(f'"netsh wlan show profiles"')
        print(cmdWN)
while True:
    try:
        ent()
    except:
        print("any thing is wrong")