import requests
import time

url = "https://www.google.com"
log_file = "internet_log.txt"

while True:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} connected")
            '''with open(log_file, "a") as file:
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Connected\n")'''
    except requests.RequestException:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} no conn")
        '''with open(log_file, "a") as file:
            
            file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Disconnected\n")'''
    
    time.sleep(1)
