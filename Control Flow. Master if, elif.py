


#IF ELSE STATEMENT
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
      
            
#FOR LOOP WITH IF, ELIF, ELSE STATEMENT
'''requests = [
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
        print("Unknown request")''' 

#WHILE LOOP WITH IF, ELIF, ELSE STATEMENT
"The while condition should not be used to do things —"
" just to repeat until it reaches the coder's satisfaction for it to stop."

"""valid_methods = ["GET", "POST", "DELETE"]
user_input=input("enter a valid metthod")
while user_input.upper() not in valid_methods:
    print("invalid method")
    user_input=input("Try again")
print(f" valid method received {user_input.upper()}")"""






valid_methods = ["GET", "POST", "DELETE"]
max_requests = 5
request_count = 0
user_input=input("enter a valid method \n")
while request_count<=max_requests and user_input.upper()!="STOP":
    if user_input.upper()  in valid_methods:
        print(f"Request processed: {user_input.upper()}")
    else:
        print("Invalid request — not processed")
    request_count+=1

    if request_count==max_requests:
        print(f"rate limit of {max_requests} exceeded")
    else:
        user_input=input("enter a request")

     
    
      



   
    
        
            
        
