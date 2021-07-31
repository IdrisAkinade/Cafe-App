from csv import DictWriter
from functions import read_csv_file,save_list
from week5_functions import get_product,get_courier, new_product, delete_product,new_courier,delete_courier
from week5_functions import print_out_list,append_dict_into_csv_file, update_dict


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
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
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
    
    product_menu_option =  int(input("\n Please Select A Product Menu Options : "))
        
    if  product_menu_option == 0:
        main_menu()

    elif product_menu_option == 1:
        get_product()
        
    elif product_menu_option == 2:
        new_product()
        
    
    # elif product_menu_option == 3:
    #     print_out_list(products)
    #     product_index_value = int(input("\n Please Enter The Index Value Of The Product You Want To Update : "))
    #     updated_product = products[product_index_value] 
    #     update_dict(updated_product) 
                
        
    elif product_menu_option == 4:   
        get_product()
        delete_product()

    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        product_menu_option = int(input("\n Please Select One Of The Five Options Given  "))       

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
        new_courier()

    elif courier_menu_option == 3:
        delete_item(couriers)
    
    elif courier_menu_option == 4:
        get_courier()
        delete_courier()
        
    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        courier_menu_option = int(input("\n Please Select One Of The Five Options Given  "))     
        
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
        [1] - Orders Dictionary
        [2] - Making An Order
        [3] - Update Existing Order Status
        [4] - Update Existing Order
        [5] - Delete Order
        \033[0m""")

    orders_menu_option =  int(input("\n Please Select A Order Menu Options : "))
    while orders_menu_option < 0 or orders_menu_option > 5:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        orders_menu_option = int(input("\n Please Select One Of The Five Options Given  "))
    
    if orders_menu_option == 0:
        main_menu()
        
    elif orders_menu_option == 1:
        for order in orders:
            print(order)
    
    elif orders_menu_option == 2:
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
        print(order_dict)
        
        right_order = input("\n\033[34m Are These The Right Details ?  Please Enter \033[0m   \033[33m Y For Yes \033[0m or \033[31m N for No \033[0m : ").lower()    
        if right_order =="y":
            orders.append(order_dict)
            field_names = ["Customer Name","Customer Address","Customer Phone", "Order Status","Courier","Items"]
            append_dict_into_csv_file("orders.csv", order_dict, field_names)
            print("\n Your Order Is Preparing")
            print("\n\033[32m Your New Order Is :\033[0m",orders[-1])
            
        else:
            print("\n Please Make Your Order Again ")
            print("")
            orders_menu()
        
        
    elif orders_menu_option == 3:
        print_out_list(orders)
        order_index_value = int(input("\n Please Select A Order Index Value : "))
        print_out_list(order_status_list)
        order_status_index_value = int(input("\n Please Select A Order Status Index Value : "))
        orders[order_index_value]["Order Status"] = order_status_index_value
        print (order_status_index_value)
        main_menu()
    

    elif orders_menu_option == 4:
        print_out_list(orders)
        order_index_value = int(input("\n Please Enter The Index Value Of The Product You Want To Update : "))
        updated_order = orders[order_index_value] 
        update_dict(updated_order)
        
        
        
    elif orders_menu_option == 5:
        print_out_list(orders)
        delete_order_value = int(input("\n Please Select A Order You Want To Delete : "))
        del orders[delete_order_value]
        print("\n  The New Order List Is : ",orders)
        
    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        orders_menu_option = int(input("\n Please Select One Of The Six Options Given  ")) 
        
    again = input("\n\t\033[34m Is There Anything Else You Would Like To Do ? \033[0m \033[33m Yes\033[0m  or \033[31m No \033[0m") 
    again = again.lower()
    if again =="yes" or again =="y":
        orders_menu()
    else:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()        


welcome()





welcome()