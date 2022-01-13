
user_data = {}
# role_arr =[]
role_arr = ['CEO', ['COO', ['Marketing', 'HR Lead']], ['CTO', ['Tech Lead']]]


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
            for i in range(len(role_arr[1])):
                if(type(role_arr[1][i]) != type([])):
                    result.append(role_arr[1][i])

        if len(role_arr) > 2:
            for i in range(len(role_arr[2])):
                if(type(role_arr[2][i]) != type([])):
                    result.append(role_arr[2][i])

        if len(role_arr) > 1 and len(role_arr[1]) > 1:
            for i in range(len(role_arr[1])):
                if(type(role_arr[1][i]) == type([])):
                    for j in range(len(role_arr[1][i])):
                        result.append(role_arr[1][i][j])

        if len(role_arr) > 2 and len(role_arr[2]) > 1:
            for i in range(len(role_arr[2])):
                if(type(role_arr[2][i]) == type([])):
                    for j in range(len(role_arr[2][i])):
                        result.append(role_arr[2][i][j])

        print()
        for item in result:
            print(item, end=" ")
        print()
    else:
        print("No roles found")

if len(role_arr) > 1:
            for i in range(len(role_arr[1])):
                if(type(role_arr[1][i]) != type([])):
                    result.append(role_arr[1][i])
def delete_user():
    if len(role_arr):
        del_name = input("Enter role name to delete: ")
        role_transfer = input("Enter the role to be transferred:")
        if(del_name in role_arr):
            role_arr.remove(del_name)
            # print("Deleted",del_name,role_transfer,role_arr)
            transfer_user(role_transfer, role_arr)
        elif(len(role_arr) > 1 and len(role_arr[1]) > 0 and del_name in role_arr[1]):
            role_arr[1].remove(del_name)
            # print("Deleted",del_name,role_transfer,role_arr[1])
            transfer_user(role_transfer, role_arr[1])
        elif(len(role_arr) > 1 and len(role_arr[1]) > 0 and del_name in role_arr[1]):
            role_arr[1].remove(del_name)
            # print("Deleted",del_name,role_transfer,role_arr[1])
            transfer_user(role_transfer, role_arr[1][1])
        elif(len(role_arr) > 2 and len(role_arr[2]) > 0 and del_name in role_arr[2]):
            role_arr[2].remove(del_name)
            # print("Deleted",del_name,role_transfer,role_arr[0])
            transfer_user(role_transfer, role_arr[2])
        elif(len(role_arr) > 2 and len(role_arr[2]) > 1 and del_name in role_arr[2]):
            role_arr[2].remove(del_name)
            # print("Deleted",del_name,role_transfer,role_arr[0])
            transfer_user(role_transfer, role_arr[2][1])
        else:
            print("Role not found")
    else:
        print("No roles found")


def transfer_user(name, role):
    if(name in role_arr):
        role_arr.remove(del_name)
    elif(len(role_arr) > 1 and len(role_arr[1]) > 0 and name in role_arr[1]):
            index = role_arr[1].index(name)
            role_arr[1][index] = [name]
            role_arr[1][index].append([role])
    elif(len(role_arr) > 1 and len(role_arr[1]) > 0 and name in role_arr[1]):
            index = role_arr[1][1].index(name)
            role_arr[1][1][index] = [name]
            role_arr[1][1][index].append([role])
    elif(len(role_arr) > 2 and len(role_arr[2]) > 0 and name in role_arr[2]):
            index = role_arr[2].index(name)
            role_arr[2][index] = [name]
            role_arr[2][index].append([role])
    elif(len(role_arr) > 2 and len(role_arr[2]) > 1 and name in role_arr[2]):
            index = role_arr[2][1].index(name)
            role_arr[2][2][index] = [name]
            role_arr[2][2][index].append([role])
    else:
        print("Transfer role not found")


def add_user():
    if len(role_arr):
        user_name = input("Enter User Name: ")
        role_name = input("Enter Role: ")
        if(role_name in role_arr):
            user_data[role_name] = user_name
        elif(len(role_arr) > 1 and len(role_arr[1][0]) > 1):
            if(role_name in role_arr[1][0]):
                user_data[role_name] = user_name
        elif(len(role_arr) > 1 and len(role_arr[1][1]) > 1):
            if(role_name in role_arr[1][1]):
                user_data[role_name] = user_name
        elif(len(role_arr) > 2 and len(role_arr[2][0]) > 1):
            if(role_name in role_arr[2][0]):
                user_data[role_name] = user_name
        elif(len(role_arr) > 2 and len(role_arr[2][1]) > 1):
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
            for i in range(len(role_arr[1])):
                if(type(role_arr[1][i]) != type([])):
                    result.append(role_arr[1][i])

        if len(role_arr) > 2:
            for i in range(len(role_arr[2])):
                if(type(role_arr[2][i]) != type([])):
                    result.append(role_arr[2][i])

        if len(role_arr) > 1 and len(role_arr[1]) > 1:
            for i in range(len(role_arr[1])):
                if(type(role_arr[1][i]) == type([])):
                    for j in range(len(role_arr[1][i])):
                        result.append(role_arr[1][i][j])

        if len(role_arr) > 2 and len(role_arr[2]) > 1:
            for i in range(len(role_arr[2])):
                if(type(role_arr[2][i]) == type([])):
                    for j in range(len(role_arr[2][i])):
                        result.append(role_arr[2][i][j])

        print()
        for item in result:
            print(item, " - ", user_data[item] if user_data.get(item) else "")
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
        delete_user()
    elif(choice == 4):
        add_user()
    elif(choice == 5):
        display_users()
    else:
        print("Invalid choice.")
