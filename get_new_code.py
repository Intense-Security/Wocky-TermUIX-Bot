import os, sys, time, requests

def GetCode(pic):
    old_test = (requests.get("https://wocky.pw/termuix/asni/").text).split("<a href")
    requests.get(f"https://wocky.pw/termuix/?key=lulzsec&action=img2txt&url={pic}")
    time.sleep(6)
    new_test = (requests.get("https://wocky.pw/termuix/asni/").text).split("<a href")
    i = 0
    current = 0 
    for line in new_test:
        # print(line)
        if line.startswith("=\"") and ".txt" in line:
            try:
                #print(f"TEST: {i} Old: " + old_test[i].split("\">")[0].replace("=\"", "") + " | New: " + line.split("\">")[0].replace("=\"", ""))
                old_code = old_test[i].split("\">")[0].replace("=\"", "") 
                new_code = line.split("\">")[0].replace("=\"", "")
                if old_code == new_code:
                    #print(f"{i} | matched! {old_code} = {new_code}")
                    current = i
            except:
                #print(f"{i} | Couldn't find the new code in the old list! (https://wocky.pw/termuix/asni/" + new_test[current+1].split("\">")[0].replace("=\"", "") + ")")
                return new_test[current+1].split("\">")[0].replace("=\"", "")
        i += 1
