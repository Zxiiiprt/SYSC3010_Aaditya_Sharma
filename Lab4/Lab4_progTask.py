import http.client
import urllib.parse
import time

key = "7481QW0APO2BO2BU"  #API Key
Group = 'L1-F-7'
MemID = 'a'
cmail = 'aadityasharma@cmail.carleton.ca'

def write():
    params = urllib.parse.urlencode({'field1': Group, 'field2': MemID, 'field3':cmail, 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(Group, "\n", MemID, "\n", cmail)
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connection failed")

if __name__ == "__main__":
    write()

