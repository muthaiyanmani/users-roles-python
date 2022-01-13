
user_data = {}
role_arr =[]
#role_arr = ['CEO', ['COO',['Marketing','HR Lead']],['CTO',['Tech Lead']]]


def create_root():
    root = input("Enter root role name: ")
    role_arr.append(root)


def add_sub():
    role_name = input("Enter sub role name: ")
    parent_name = input("Enter reporting to role name :")
    if(parent_name in role_arr):
        role_arr.append([role_name])
    elif(parent_name in role_arr[1]):
        role_arr[1].append([role_name])
    elif(parent_name in role_arr[2]):
        role_arr[2].append([role_name])


def display():
    if role_arr:
        result = []
        result.append(role_arr[0])
        if len(role_arr) > 1:
            result.append(role_arr[1][0])
        if len(role_arr) > 2:
            result.append(role_arr[2][0])
        if len(role_arr)>1 and len(role_arr[1])>1:
            for i in range(len(role_arr[1][1])):
                result.append(role_arr[1][1][i])
        if len(role_arr)>2 and len(role_arr[2])>1:
            for i in range(len(role_arr[2][1])):
                result.append(role_arr[2][1][i])
        print()
        for item in result:
            print(item,end=" ")
        print()
    else:
        print("No roles found")

def delete():
    del_name = input("Enter role name to delete: ")
    role_transfer = input("Enter the role to be transferred:")
    # if(del_role in role_arr):
    if(del_name in role_arr):
        print("Role deleted")
        role_arr.remove(del_name)
        # role_arr.append([role_name])
    elif(del_name in role_arr[1]):
        role_arr[1].remove(del_name)
        print("Role deleted 1")
        # role_arr[1].append([role_name])
        # role_arr[1].append([role_name])
    elif(del_name in role_arr[2]):
        role_arr[2].remove(del_name)
        role_arr[2] = role_arr[2][0]
        print("Role deleted 2")
        # role_arr[2].append([role_name])


def add_users():
    if len(role_arr):
        user_name = input("Enter User Name: ")
        role_name = input("Enter Role: ")
        if(role_name in role_arr):
            user_data[role_name] = user_name
        elif(len(role_arr)>1 and len(role_arr[1][0])>1):
            if(role_name in role_arr[1][0]):
                user_data[role_name] = user_name
        elif(len(role_arr)>1 and len(role_arr[1][1])>1):
            if(role_name in role_arr[1][1]):
                user_data[role_name] = user_name
        elif(len(role_arr)>2 and len(role_arr[2][0])>1):
            if(role_name in role_arr[2][0]):
                user_data[role_name] = user_name
        elif(len(role_arr)>2 and len(role_arr[2][1])>1):
            if(role_name in role_arr[2][1]):
                user_data[role_name] = user_name
        else:
            print("Role not found")
    else:
        print("No roles found")


def display_users():
    if role_arr:
        result = []
        result.append(role_arr[0])
        if len(role_arr) > 1:
            result.append(role_arr[1][0])
        if len(role_arr) > 2:
            result.append(role_arr[2][0])
        if len(role_arr)>1 and len(role_arr[1])>1:
            for i in range(len(role_arr[1][1])):
                result.append(role_arr[1][1][i])
        if len(role_arr)>2 and len(role_arr[2])>1:
            for i in range(len(role_arr[2][1])):
                result.append(role_arr[2][1][i])
        print()
        for item in result:
            print(item," - ",user_data[item] if user_data.get(item) else "")
        print()
    else:
        print("No roles found")


# execution starts here
create_root()
while(True):
    print("\nOperations:\n 1.Add Sub Role. 2.Display 3.Delete 4.Add Users 5.Display Users")
    choice = int(input("Operations to be performed: "))
    print()
    if(choice == 1):
        add_sub()
    elif(choice == 2):
        display()
    elif(choice == 3):
        delete()
    elif(choice == 4):
        add_users()
    elif(choice == 5):
        display_users()
    else:
        print("Invalid choice.")

