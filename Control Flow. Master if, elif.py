'''server_online=True
is_active=True
account_exist=True
user_role=input("whatt is your role")
password_correct=False

if server_online:
    if not account_exist:
        print("account not found")
    else:
        if is_active:
             if not password_correct:
               if user_role=="admin":
                     print("welcome admin full access")
               elif user_role=="editor":
                     print("Welcome editor — read and write access")
               elif user_role=="viewer":
                     print("Welcome viewer — read only access")
               else:
                     print("Role not recognized")
             else:
                 print("worng password")
                     
        else:
            print("account suspended")           
else:
    print("server down try again later")'''
      
            

requests = [
    {"method": "GET", "status_code": 200},
    {"method": "POST", "status_code": 201},
    {"method": "GET", "status_code": 401},
    {"method": "DELETE", "status_code": 400},
    {"method": "PUT", "status_code": 500},
]

for request in requests:
    if request["method"]=="GET" and request["status_code"] is 200:
        print("GET request successfu")
    elif request["method"]=="POST" and request["status_code"] is 201:
        print("POST request successful")
    elif  request["status_code"] == 401:
        print("Unauthorized — login required")
    elif  request["status_code"] == 400:
        print("Bad request — client error")  
    else:
        print("Unknown request") 

