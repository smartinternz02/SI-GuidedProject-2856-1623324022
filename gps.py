import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "3f5ddu",#place you're crednetials 
        "typeId": "iotdevice",
        "deviceId":"2001"
    },
    "auth": {
        "token": "Sindhu@27"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()


while True:
    otp=random.randint(1111,9999)
    print(otp);
    admin_otp=int(input())
    if(otp== admin_otp):
        print("vechile door Open")
        lat=round(random.uniform(15,20),2)
        lon=round(random.uniform(15,20),2)
        myData={'latitude':lat,'longitude':lon}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(5)
    else:
        var="alert"
        myData={'danger':var}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Published data Successfully: %s", myData)
        client.commandCallback = myCommandCallback
        time.sleep(5)
      
        
        
                
  
    
client.disconnect()
#**dont connect to ibm watson simulator**#
#temp = round(random.uniform(99.9,105.2), 2)
    #pulse=random.randint(65,80)
    #bp=random.randint(120,140)
    

