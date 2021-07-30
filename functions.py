import csv
from csv import DictReader,DictWriter

import os
from time import sleep
# The screen clear function
def screen_clear():
    _ = os.system('cls')
    sleep(5)
    screen_clear()



def read_and_append_to_file (file_name, list_to_read):
    with open(file_name,"r") as temp_var_name:
        for item in temp_var_name.readlines():
            list_to_read.append(item.replace("\n",""))
            
            
    
def save_list (file_name, list_name):
    with open (file_name, "w", newline='') as saved_list:
        #if list_name:
        writer =  csv.DictWriter(saved_list, fieldnames=list_name[0].keys())
        writer.writeheader()
        writer.writerows(list_name)



            
def read_csv_file (file_name, csv_to_read):
    with open(file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row)
        return csv_list


def append_dict_into_csv_file(file_name, dict_of_elem, field_names):
    with open(file_name, 'a+', newline='') as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)



def print_out_list (list_name):
    for key, value in enumerate(list_name):
        print(key,value)
    return key,value


    


def update_product():
    print_out_list(products)
    product_index_value = int(input("\n Please Enter The Index Value Of The Product You Want To Update : "))
    updated_product = products[product_index_value] 
    update_dict(updated_product) 
    
def update_couriers():
    print_out_list(couriers)
    courier_index_value = int(input("\n Please Enter The Index Value Of The Product You Want To Update : "))
    updated_courier = couriers[courier_index_value] 
    update_dict(updated_courier) 

def update_orders():
    print_out_list(orders)
    order_index_value = int(input("\n Please Enter The Index Value Of The Product You Want To Update : "))
    updated_order = orders[order_index_value] 
    update_dict(updated_order)


def update_dict(item):
    olditem = item.copy()
    for key, value in item.items():
        print(f"{key} currently has a value of {value}")
        updated_value = input(f"\n Please Enter A New value for {key}: ")
        if updated_value == "":
            item[key] = value
        else: 
            item[key] = updated_value
    print(f"\n {olditem} Is Now Updated To {item}")
            

def delete_item(list_to_delete_from):
    print_out_list(list_to_delete_from)
    delete_index_value = int(input("\n Please Enter The Index value Of The Item You Want To Delete : "))
    
    if int(delete_index_value) not in list(range(len(list_to_delete_from))):
        print('Please Enter A Valid Index ')
        delete_item(list_to_delete_from)
    else:
        deleted_index = list_to_delete_from.pop(int(delete_index_value))
        print(f'{deleted_index} Has Now Been Deleted')
        print(list_to_delete_from)


def delete_index(list_name, deleted_input):
    del list_name[deleted_input]






# Displays welcome message to the user
def welcome():
    print("") 
    print("\t\033[34m  ############################## \033[0m ")
    print("\t\033[1;37;40m    Welcome To Automobile Gurus  \033[0;37;40 ")
    print("\t\033[34m  ##############################  \033[0m")
    enter = input("\n Press Enter To Use The App ")
    if  enter == "":
        main_menu()
    else:
        print("Invalid !!! Please Press Enter")
        welcome()
        
# Displays the main menu to the user
def main_menu():
    main_menu_option = "" 
    print("") 
    print("\t\033[34m  ###################\033[0m ")
    print("\t\033[34m  #    Main Menu    #\033[0m")
    print("\t \033[34m ###################\033[0m")
    print("""\033[33m
        [0] - Exit App
        [1] - Product Menu Option
        [2] - Courier Menu Option
    \033[0m""")


# Displays the product menu to the user 
def product_menu():
    product_menu_option = ""
    print("") 
    print("\t --------------------")
    print("\t\033[34m*** Product Menu ***\033[0m") 
    print("\t --------------------")
    print(""""\033[33m
        [0] - Main Menu
        [1] - Product List
        [2] - Create A New Product
        [3] - Update A Product
        [4] - Delete A Product
        \033[0m""")

# Displays the courier menu to the user
def courier_menu():
    courier_menu_option = ""
    print("") 
    print("\t -----------------")
    print("\t\033[34m*** Courier Menu ***\033[0m")
    print("\t -----------------")
    print("""\033[33m
        [0] - Return To Main Menu
        [1] - Couriers List
        [2] - Create A New Courier
        [3] - Update A Courier
        [4] - Delete A Courier
        \033[0m""")

# Displays the order menu to the user
def orders_menu():
    orders_menu_option = ""
    print("") 
    print("\t -----------------")
    print("\t\033[34m*** Orders Menu ***\033[0m")
    print("\t -----------------")
    print("""\033[33m
        [0] - Return To Main Menu
        [1] - Orders Dictionary
        [2] - Making An Order
        [3] - Update Existing Order Status
        [4] - Update Existing Order
        [5] - Delete Courier
        \033[0m""")
    












# elif user_input == 3:
#         for key, value in enumerate(orders):
#             print(key, value)

#         order_index = int(input("""\033[33m\nPlease select an order to update:   \033[0m"""))
#         print('')

#         for key, value in enumerate(order_status):
#             print(key, value)

#         status_input = int(
#             input("""\033[33m\nChoose an order status to update on the order list:   \033[0m"""))
#         order_to_update = orders[order_index]
        
#         order_to_update['Status'] = order_status[status_input]
#         print("""\033[33m\nOrder status has been updated\033[0m""")
#         print(order_to_update)



def update_dict(item):
    olditem = item.copy()
    for key, value in item.items():
        print(f"{key} currently has a value of {value}")
        updated_value = input(f"\n Please Enter A New value for {key}: ")
        if updated_value == "":
            item[key] = value
        else: 
            item[key] = updated_value
    print(f"\n {olditem} Is Now Updated To {item}")
            
            
            
            
            
            
    for key, value in enumerate orders:
        print(key, value)
    order_index = int(input(''' \033[33m\n\tSelect an order to update:    \033[0m'''))
    updated_order = orders[order_index] 
    old_order = updated_order.copy()
    for key, value in enumerate updated_order.items():
        print(key, value)
        chosen_order = input(f'\n{key} Has value of {value}. Enter new value for {key}: ')
        if chosen_order == '':
            orders[key] = value
            print('\nNothing has been changed')
        else:
            order[key] = chosen_order
    print('Your order has been updated:', chosen_order)




              
              
              for key, value in enumerate(orders):
                print(key, value)
        order_index = int(input('''
        \033[33m\n\tSelect an order to update:    \033[0m'''))
        chosen_order = orders[order_index]

        new_order = orders.copy()

        for key, value in chosen_order.items():

            chosen_value = input(
                f'\n{key} Has value of {value}. Enter new value for {key}: ')

        if chosen_value == '':
            chosen_order[key] = value
            print('\nNothing has been changed')
        else:
            chosen_order[key] = chosen_value

        print('Your order has been up
