product_list = ['Ferrari', 'Lamborghini', 'Tesla', 'Hummer', 'Honda', 'BMW', 'Ford', 'Audi', 'Hyundai'] ## The Product List

def main_menu():
    main_menu_option = "" # its empty
    #main_menu
    print("") #### To put space before the menu heading
    print("\t -----------------")
    print("\t\033[34m*** Main Menu ***\033[0m") ### This is the Main Menu Heading
    print("\t -----------------")
    print("""\033[33m
        [0] -  Exit App
        [1] - Product Menu Option
       \033[0m""")
    
    main_menu_option =  int(input("\n Please Select Main Menu Options : ")) ## ask the user to select an option from main menu
    
    ## if the users input number not given
    while main_menu_option < 0 or main_menu_option > 1:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        main_menu_option = int(input("\n Please Select One Of The Two Options Given "))
    
    if main_menu_option == 0:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()
        
    elif main_menu_option == 1:
        product_menu()
        product_menu_option = int(input("\n Please Select Product Menu Options : "))
        
    
# Displays the product menu to the user 
def product_menu():
    again = ""
    #product_menu_option = "" # its empty
    print("") #### To put space before the product menu heading
    print("\t --------------------")
    print("\t\033[34m*** Product Menu ***\033[0m") ### This is the Product Menu Heading
    print("\t --------------------")
    print(""""\033[33m
        [0] - Main Menu
        [1] - Product List
        [2] - Create A New Product
        [3] - Update A Product
        [4] - Delete A Product
        \033[0m""")
    
    
    product_menu_option =  int(input("\n Please Select A Product Menu Options : "))
    while product_menu_option < 0 or product_menu_option > 4:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        product_menu_option = int(input("\n Please Select One Of The Five Options Given  "))

    if  product_menu_option == 0:
        main_menu()

    elif product_menu_option == 1:
        print("\n\033[32m The Product List Is :\033[0m",product_list)
         
    elif product_menu_option == 2:
        new_product = input("\n Please Enter A New Product Name : ")
        product_list.append(new_product)
        print("\n You Have Created A New Product")
        print("\n\033[32m The New Product List Is :\033[0m",product_list)
        
        
    elif product_menu_option == 3:
        for value, index in enumerate(product_list):
            print(value, index)
        product_index_value = int(input("\n Please Enter The Index value Of The Product You Want To Update : "))
        while product_index_value < 0 or product_index_value > 8:
            print("\n\033[31m The selection provided is invalid.\033[0m")
            product_index_value = int(input("\n Please Select Number from 0 to 8 "))
        new_product_name = input("\n Please Enter A New Product Name For The Product: ")
        product_list[product_index_value] = new_product_name
        print("\n\033[32m The Updated Product List Is :\033[0m",product_list)
        
    elif product_menu_option == 4:
        print("\n", [list((i, product_list[i])) for i in range(len(product_list))])
        delete_product_index_value = int(input("\n Please Enter The Index value Of The Product You Want To Delete : "))
        while delete_product_index_value < 0 or delete_product_index_value > 8:
            print("\n\033[31m The selection provided is invalid.\033[0m")
            delete_product_index_value = int(input("\n Please Select Number from 0 to 8 "))
        del product_list[delete_product_index_value] 
        print("\n\033[32m The New Product List Is :\033[0m",product_list)
        
        
        
        
        
    again = input("\n\t\033[34m Is There Anything Else You Would Like To Do ? \033[0m   \033[31m Yes\033[0m  or \033[33m No \033[0m") 
    again = again.lower()

    if again =="yes" or again =="y":
        product_menu()
    else:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()        
    
            
            

main_menu()     