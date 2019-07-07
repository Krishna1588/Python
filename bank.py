data={"alpha":
          {"password":[1234],"balance" :[2000]},
    "beta":
        {"password":[5678],"balance" :[5000]}
     }
chance=3
user=input("enter your name:")
for i in data:
    if i==user:
        while chance > 0:
            code = int(input("Enter the password"))
            if code == data[i]["password"][-1]:
                print("press 1 for checking the balance")
                print("press 2 for withdrawing")
                print("press 3 for change password")

                option = int(input("Enter the option"))
                if option == 1:
                    print("your current balance is :", data[i]["balance"][-1])
                    continue
                if option == 2:
                    withdraw = int(input("Enter the amount:"))
                    data[i]["balance"] = data[i]["balance"][-1] - withdraw
                    print("Amount withdrawn:", withdraw)
                    print("your current balance is :", data[i]["balance"])
                    continue
                if option == 3:
                    password = int(input("Enter new password"))
                    if password!=data[i]["password"][-1]:
                        print("your password is changed")
                        continue
                    else:
                        print("Pls enter different password")
                        password = int(input("Enter new password"))
                        print("your password is changed")
                        break
            else:
                chance -= 1
                print("incorrect password")
                assert(chance==0),"Account blocked"

