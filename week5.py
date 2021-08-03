from csv import DictWriter
import json
import pprint
from prompt_toolkit import print_formatted_text, HTML
from functions import read_csv_file
from week5_functions import get_product,get_courier, new_product, delete_product,new_courier,delete_courier
from week5_functions import print_out_list,append_dict_into_csv_file, update_dict
from week5_functions import update_courier,update_product,save_list

orders = []
orders =   read_csv_file("orders.csv", orders)
order_status_list = ["Awaiting Payment","Preparing","Shipped","Delivered"]

def welcome():
    print("") 
    print("\t\033[34m  #################### \033[0m ")
    print("\t\033[1;37;40m     A Cup Of Joy  \033[0;37;40 ")
    print("\t\033[34m  ####################  \033[0m")
    
    enter = input("\n\t Press Enter To Use The App ")
    if  enter == "":
        main_menu()
    else:
        print("Invalid !!! Please Press Enter")
        welcome()
        
# def hello():
#     print("")
#     print("\t\033[1;34;40m     [0]  - Shop   \033[0m ")
#     print("\t\033[1;35;40m     [1]  - About Us        \033[0m  ")
#     print("\t\033[1;31;40m     [2]  - Delivery Information  \033[0m  ")
#     print("\t\033[1;32;40m     [3]  - Contact Us    \033[0m")
    
#     hello_input =  int(input("\n\033[1;37;40m Please Select An Options : \033[0m"))
#     if hello_input == 0:
#         Shop()
#     elif hello_input == 1:
#         About_Us()
#     elif hello_input == 2:
#         Delivery()
#     elif hello_input == 3:
#         Contact_Us()
#     else:
#         print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
#         hello

# def Shop():
#     main_menu()

# def About_Us ():    
#     print("\n\t\033[95m             About Us \033[0m")
#     print_formatted_text(HTML("""<i>
#         Hello and welcome to "A Cup Of Joy". 
#         We are the best selling coffee shop North London. 
#         We are currently based in Walthamstow.
#         We offer a variety of beverages made by our professionally trained barista.
#         We look forward to serving you at A Cup Of Joy!
#         </i>""")) 
    
#     exit_about_us = input("\n Please Enter e To go Back : ")
#     if exit_about_us == "e":
#         hello()
#     else:
#         print('\033[91m\n\t Wrong Value Entered...Please Enter e \033[0m')
#         About_Us()
        
# def Delivery():
#     print('\n\t\033[91m            Delivery \033[0m')  
#     print_formatted_text(HTML("""<i>
#         We do free local delivery in for any of our customer based in Walthamstow 
#         Delivery for anywhere else in London is €1.50.
#         Currently, We do not deliver outside London.
#         </i>"""))
#     exit_delivery = input("\n Please Enter e To go Back : ")
#     if exit_delivery == "e":
#         hello()
#     else:
#         print('\033[91m\n\t Wrong ValueEntered...Please Enter e \033[0m')
#         Delivery()
    
# def Contact_Us():
#     print('\n\t\033[92m          Contact Us \033[0m')
#     print_formatted_text(HTML("""<i>
#         You can contact us by:
    
#         Phone Number : +44 7953675981
#         Email : <u>cupofjoy@gmail.com</u>
#         </i>"""))
#     exit_Contact_Us = input("\n Please Enter e To go Back : ")
#     if exit_Contact_Us== "e":
#         hello()
#     else:
#         print('\033[91m\n\t Wrong ValueEntered...Please Enter e \033[0m')
#         About_Us()

def main_menu():
    main_menu_option = "" 
    print("") 
    print("\t------------------- ")
    print("\t\033[34m      Main Menu     \033[0m")
    print("\t-------------------")
    print("""\033[33m
        [0] - Exit App
        [1] - Product Menu Option
        [2] - Courier Menu Option
        [3] - Orders Menu Option
    \033[0m""")
    
    main_menu_option =  int(input("\n Please Select Main Menu Options : ")) 
        
    if main_menu_option == 0: 
        #save_list("products.csv", products)
        #save_list ("couriers.csv", couriers)
        save_list ("orders.csv", orders)
        print("\n\033[32m Products, Couriers and Orders Have Been Saved \033[0m ")
        print("\n\t\033[31m Thank you & Goodbye.\033[0m ")
        print("")
        exit()
                
    elif main_menu_option == 1:
        product_menu()
        
    elif main_menu_option == 2:
        courier_menu()
            
    elif main_menu_option == 3:
        orders_menu()
        
    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        main_menu()
        
def product_menu():
    product_menu_option =""
    print("") 
    print("\t --------------------")
    print("\t\033[34m*** Product Menu ***\033[0m") 
    print("\t --------------------")
    print("""\033[33m
        [0] - Main Menu
        [1] - Product List
        [2] - Create A New Product
        [3] - Update A Product
        [4] - Delete A Product
        \033[0m""")
    
    product_menu_option =  int(input("\n Please Select A Product Menu Options : "))
        
    if  product_menu_option == 0:
        main_menu()

    elif product_menu_option == 1:
        get_product()
        
    elif product_menu_option == 2:
        print_formatted_text(HTML(f"\n\t <u> <b> Making A New Product </b> </u> "))
        new_product()
        print("\n \033[34m Below Is The New Product List : \033[0m")
        get_product()
        
    elif product_menu_option == 3:
        print_formatted_text(HTML(f"\n\t <u> <b> Updating A Product </b> </u> "))
        update_product()
    
    elif product_menu_option == 4:
        print_formatted_text(HTML(f"\n\t <u> <b> Deleting A Product </b> </u> "))
        delete_product()
        print("\n \033[34m Below Is The New Product List : \033[0m")
        get_product()

    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        product_menu()

    again = input("\n\t\033[34m Is There Anything Else You Would Like To Do ? \033[0m \033[33m Yes\033[0m  or \033[31m No \033[0m") 
    again = again.lower()
    
    if again =="yes" or again =="y":
        product_menu()
    else:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()
    
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
    
    courier_menu_option =  int(input("\n Please Select A Courier Menu Options : "))
    
    if  courier_menu_option == 0:
        main_menu()
        
    elif courier_menu_option == 1:
        get_courier()
        
    elif courier_menu_option == 2:
        print_formatted_text(HTML(f"\n\t <u> <b> Making A New Courier </b> </u> "))
        new_courier()
        print("\n \033[34m Below Is The New Courier List : \033[0m")
        get_courier()

    elif courier_menu_option == 3:
        print_formatted_text(HTML(f"\n\t <u> <b> Updating A Courier </b> </u> "))
        update_courier()
    
    elif courier_menu_option == 4:
        print_formatted_text(HTML(f"\n\t <u> <b> Deleting A Courier </b> </u> "))
        delete_courier()
        print("\n \033[34m Below Is The New Courier List : \033[0m")
        get_courier()
        
    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        courier_menu()    
    
    again = input("\n\t\033[34m Is There Anything Else You Would Like To Do ? \033[0m \033[33m Yes\033[0m  or \033[31m No \033[0m") 
    again = again.lower()

    if again =="yes" or again =="y":
        courier_menu()
    else:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()        

def orders_menu():
    orders_menu_option = ""
    print("") 
    print("\t -----------------")
    print("\t\033[34m*** Orders Menu ***\033[0m")
    print("\t -----------------")
    print("""\033[33m
        [0] - Return To Main Menu
        [1] - Orders 
        [2] - Making An Order
        [3] - Update Existing Order Status
        [4] - Update Existing Order
        [5] - Delete Order
        \033[0m""")

    orders_menu_option =  int(input("\n Please Select A Order Menu Options : "))
    
    if orders_menu_option == 0:
        main_menu()
        
    elif orders_menu_option == 1:
        print_formatted_text(HTML(f"\n\t <u> <b> Below Are The Orders </b> </u> "))
        print(json.dumps(orders, sort_keys=False, separators =(".", ":"),  indent=4))
    
    elif orders_menu_option == 2:
        print_formatted_text(HTML(f"\n\t <u> <b> Making A New Order </b> </u> "))
        new_customer_name = input("\n Please Enter Your Name : ").title() # turns the first letters to capital letter
        new_customer_address = input("\n Please Enter Your Address : ")
        new_customer_phone_number = int(input("\n Please Enter Your Phone Number : "))
        
        get_product()
        products_indexes = input("\n Please Enter Product Indexes Separated By Comma: ").split(',')
        
        get_courier()
        courier_index = input("\n Please Enter A Courier Index: ")
        
        order_status = 'Preparing'
        order_dict = {}
        order_dict["Customer Name"] =  new_customer_name
        order_dict["Customer Address"] = new_customer_address
        order_dict["Customer Phone"] = new_customer_phone_number
        order_dict["Order Status"] = order_status
        order_dict["Courier"] = courier_index
        order_dict["Items"] = products_indexes
        print("")
        pprint.pprint(order_dict)
        
        right_order = input("\n\033[34m Are These The Right Details ?  Please Enter \033[0m   \033[33m Y For Yes \033[0m or \033[31m N for No \033[0m : ").lower()    
        if right_order =="y":
            orders.append(order_dict)
            field_names = ["Customer Name","Customer Address","Customer Phone", "Order Status","Courier","Items"]
            append_dict_into_csv_file("orders.csv", order_dict, field_names)
            print("\n\t\033[95m Your Order Is Preparing \033[0m")
            print("\n\033[32m Your New Order Is :\033[0m")
            print(json.dumps(order_dict, sort_keys=False, separators =(".", ":"),  indent=4))
            
            
        else:
            print("\n Please Make Your Order Again ")
            print("")
            orders_menu()

    elif orders_menu_option == 3:
        print_formatted_text(HTML(f"\n\t <u> <b> Updating An Existing Order Status </b> </u> "))
        
        print(json.dumps(orders, sort_keys=False, separators =(".", ":"),  indent=4))
        order_index_value = int(input("\n Please Select A Order Index Value : "))
        
        print_out_list(order_status_list)
        order_status_index_value = int(input("\n Please Select A Order Status Index Value : "))
        
        orders[order_index_value]["Order Status"] = order_status_list[order_status_index_value]
        print(f"\n Order Status Has Been Updated To : \033[34m {order_status_list[order_status_index_value]} \033[0m")
        print("The Order Is Now Changed Now : ")
        #print(json.dumps(order_dict, sort_keys=False, separators =(".", ":"),  indent=4))

    
    elif orders_menu_option == 4:
        print_formatted_text(HTML(f"\n\t <u> <b> Updating An Existing Order </b> </u> "))
        
        print(json.dumps(orders, sort_keys=False, separators =(".", ":"),  indent=4))
        order_index_value = int(input("\n Please Enter The Index Value Of The Product You Want To Update : "))
        updated_order = orders[order_index_value] 
        update_dict(updated_order)
        print('\033[95m\n\t This Is Your Updated Order : \033[0m')
        print(json.dumps(updated_order, sort_keys=False, separators =(".", ":"),  indent=4))
        
    elif orders_menu_option == 5:
        print_formatted_text(HTML(f"\n\t <u> <b> Deleting An Order </b> </u> "))
        print_out_list(orders)
        delete_order_value = int(input("\n Please Select A Order You Want To Delete : "))
        del orders[delete_order_value]
        print('\033[95m\n\t The New Order List Is :  \033[0m')
        print(json.dumps(orders, sort_keys=False, separators =(".", ":"),  indent=4))
        
    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        orders_menu() 
    
    again = input("\n\t\033[34m Is There Anything Else You Would Like To Do ? \033[0m \033[33m Yes\033[0m  or \033[31m No \033[0m") 
    again = again.lower()
    if again =="yes" or again =="y":
        orders_menu()
    else:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()        

welcome()