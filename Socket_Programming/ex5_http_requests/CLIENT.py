import requests
import time

print("--- HTTP Request Library Client ---")
print("This client will now send requests to your LOCAL Socket Server.")
time.sleep(1)

url = "http://localhost:5004"

while True:
    choice = input("\n1. Send GET Request\n2. Send POST Request\n3. Exit\nChoice: ")
    
    if choice == '1':
        print(f"Sending GET to {url}...")
        try:
            r = requests.get(url)
            print(f"Status Code: {r.status_code}")
            print(f"Server JSON: {r.json()}")
        except Exception as e:
            print(f"Error: {e}")
            
    elif choice == '2':
        print(f"Sending POST to {url}...")
        try:
            payload = {"lab": "Computer Networks", "experiment": 5}
            r = requests.post(url, json=payload)
            print(f"Status Code: {r.status_code}")
            print(f"Server JSON: {r.json()}")
        except Exception as e:
            print(f"Error: {e}")
            
    elif choice == '3':
        break
    else:
        print("Invalid choice.")

print("Client exiting.")
