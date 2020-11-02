from django.shortcuts import render,redirect
import requests
import json
import urllib3
from requests.auth import HTTPBasicAuth


# Create your views here.
def home(request):
    return render(request,'home.html')


def collaboration(request):
    return render(request,'collab.html')



def getroom(request):
    api_req=requests.get("https://webexapis.com/v1/rooms",headers={'Authorization': 'Bearer Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0M2OGFhMzQwYjgyMzU3MDQwN2MyOWE1Zjg4ZTE3ZGVhZDY0Nzc2MmU5OTYxOGU2ZTQxODUzODIxYWQ0OTZjZjE5'})
    try:
        api=json.loads(api_req.content)
        #print(api)
    except Exception as e:
        api="Error not loading!"
    return render(request,'getroom.html',{'api2':api})

def meeting(request):
    api_req=requests.get("https://webexapis.com/v1/rooms",headers={'Authorization': 'Bearer Mzk2YTM2YTgtMzY2MS00ZTM3LTgyYjAtZTc3Y2MzZmQ2ODVmZjc1NmU4YTQtMDRi_PF84_f7ec1daa-c9e8-4dbc-9e60-c30b51478116'})
    try:
        api=json.loads(api_req.content)
        #print(api)
    except Exception as e:
        api="Error not loading!"
    return render(request,'invitemeet.html',{'api2':api})


def postroom(request):
    data2=request.POST.get('name')
    print(data2)

    api_req=requests.post("https://webexapis.com/v1/rooms",data={'title':data2},headers={'Authorization': 'Bearer Mzk2YTM2YTgtMzY2MS00ZTM3LTgyYjAtZTc3Y2MzZmQ2ODVmZjc1NmU4YTQtMDRi_PF84_f7ec1daa-c9e8-4dbc-9e60-c30b51478116',
                  })
    try:
        api=json.loads(api_req.content)
    except Exception as e:
        api="Error not loading!"
    return render(request,'create2.html',{'api2':api})


def team_members(request):
    teamId='Y2lzY29zcGFyazovL3VzL1JPT00vN2I3NDE1ZjAtMDIxYi0xMWViLWExYjgtNjEwYmEzZjdkZmJj'
    api_req=requests.get(f"https://webexapis.com/v1/team/memberships{teamId}",headers={'Authorization': 'Bearer MmMwODIzMTUtNjQzZC00ZmE2LWFhNTAtMWQ3MzBkYTFhZDI2Y2RiOTcwMWQtNWRi_PF84_f7ec1daa-c9e8-4dbc-9e60-c30b51478116'})
    try:
        api=json.loads(api_req.content)
        #print(api)
    except Exception as e:
        api="Error not loading!"
    return render(request,'team_members.html',{'api2':api})

def deletegroup(request):
    data2=request.GET.get('rmId')
    #print(data2)
    api_req=requests.delete(f"https://webexapis.com/v1/rooms/{data2}",headers={'Authorization': 'Bearer Mzk2YTM2YTgtMzY2MS00ZTM3LTgyYjAtZTc3Y2MzZmQ2ODVmZjc1NmU4YTQtMDRi_PF84_f7ec1daa-c9e8-4dbc-9e60-c30b51478116',
                  })
    try:
        api=json.loads(api_req.content)
    except Exception as e:
        api="Error not loading!"
    return render(request,'del.html')

def leads(request):
    return render(request,'leads.html')


def getid(request,id):
    data2=request.GET.get(id=id)
    d=data2[1:]
    print(d)
    api_req=requests.delete(f"https://webexapis.com/v1/rooms/{data2}",headers={'Authorization': 'Bearer MmMwODIzMTUtNjQzZC00ZmE2LWFhNTAtMWQ3MzBkYTFhZDI2Y2RiOTcwMWQtNWRi_PF84_f7ec1daa-c9e8-4dbc-9e60-c30b51478116',
                  })
    try:
        api=json.loads(api_req.content)
    except Exception as e:
        api="Error not loading!"
    return render(request,'del2.html',{'data':data2})





#from prettytable import PrettyTable



#ENVIRONMENT_IN_USE = "sandbox"

# Set the 'Environment Variables' based on the lab environment in use
#if ENVIRONMENT_IN_USE == "sandbox":
dnac = {
        "host": "sandboxdnac.cisco.com",
        "port": 443,
        "username": "devnetuser",
        "password": "Cisco123!"
    }




#dnac_devices = PrettyTable(['Hostname','Platform Id','Software Type','Software Version','Up Time'])
#dnac_devices.padding_width = 1
 	
# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#headers = {
#              'content-type': "application/json",
#              'x-auth-token':  ""
#          }
def networking(request):
    return render(request,'networking.html')


host=dnac["host"]
username=dnac["username"]
password=dnac["password"]

def dnac_login(request):
    url = "https://{}/api/system/v1/auth/token".format(host)
    response1 = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                verify=False)
    global tk
    tk = response1.json()["Token"]
    try:
        apilogin=json.loads(response1.content)
    except Exception as e:
        apilogin="Error not loading!"
    return render(request,'dnaclogin.html',{'log':apilogin})


def network_device_list(request):
    url = "https://{}/api/v1/network-device".format(dnac['host'])
    #headers["x-auth-token"]=tk
    response2 = requests.get(url, headers={
              'content-type': "application/json",
              'x-auth-token': tk
          }, verify=False)
    #data = response.json()
    #for item in data['response']:
    #    dnac_devices.add_row([item["hostname"],item["platformId"],item["softwareType"],item["softwareVersion"],item["upTime"]])
    apiget=json.loads(response2.content)
    return render(request,'network_device_list.html',{'get':apiget})
    print(tk)

#login = dnac_login(dnac["host"], dnac["username"], dnac["password"])
#network_device_list(dnac, login)

#print(dnac_devices)


def Network_health(request):
    url = "https://{}/dna/intent/api/v1/application-policy-application-set".format(dnac['host'])
    #headers["x-auth-token"]=tk
    response2 = requests.get(url, headers={
              'content-type': "application/json",
              'x-auth-token': tk
          }, verify=False)
    #data = response.json()
    #for item in data['response']:
    #    dnac_devices.add_row([item["hostname"],item["platformId"],item["softwareType"],item["softwareVersion"],item["upTime"]])
    apiget=json.loads(response2.content)
    return render(request,'Network_health.html',{'get':apiget})
    print(apiget)