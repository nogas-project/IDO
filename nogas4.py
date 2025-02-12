import time
from gas_detection import GasDetection
import requests
import pigpio
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()

pi = pigpio.pi()
pi.set_mode(21,pigpio.INPUT)
def getToken(): 
    try:
        headers = {"Content-Type": "application/json; charset=utf-8"}
        HOST=os.getenv("LOGIN_URL")
        CRED=os.getenv("CRED")
        login = requests.post(HOST, headers=headers, data=CRED) 
        login.close
        return login.text
    except:
        return None
    
def pushData(co_data):
    try:
        data={"co2_amount":co_data}
        token = getToken()
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json" }
        HOST=os.getenv("ADD_DATA_URL")
        response = requests.post(HOST, headers=headers, json=data)
        if response.status_code == 200:
            data = response.text
            print(data)
            response.close
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            response.close;
    except:
        print("Exception")
        
def checkData(co_data):
    if(co_data < 100):
        return "No danger !"
    if(co_data < 200): 
        return "it's alright !" 
    elif(co_data < 400): 
        return "Be careful, Danger !"
    elif(co_data < 800):
        return "Evacuate imediately !"
    elif(co_data < 1600):
        return "Death in couple hours !"
    elif(co_data > 3200):
        return "Imminent death !"
def alarm():
    print("BIB")
    
def main():
    print('Calibrating ...')
    detection = GasDetection()
    try:
        while True:
            ppm = detection.percentage()
            print('CO: {} ppm'.format(round(ppm[detection.CO_GAS],4)))
            message = checkData(ppm[detection.CO_GAS]);
            signal = pi.read(21)
            if(message =="Be careful, Danger !"):
                alarm()
            # time.sleep(0.5)
    except KeyboardInterrupt:
        print('\nAborted by user!')

if __name__ == '__main__':
    main()
