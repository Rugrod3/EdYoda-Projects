
import administator
import food
import user


while True:
    start=int(input('choose one of the following:\n1.admin\n2.user\n.0exit'))
    if start==1:
        username=input('username:')
        password=input('password:')
        administator.log_in(username,password)
        x=administator.log_in(username,password)
        if x==True:
            admin1=int(input('choose one of the following:\n1.add new food item\n2.edit food item using food id\n3.view list of all food item\n4.delete food item using food id\n0.exit'))
            if admin1==1:
                food.add_food_item(input('name'),input('food_id'),input('price'),input('quantity'),input('stock'))
            elif admin1==2:
                food.edit_food_item()
            elif admin1==3:
                food.view_food_list()
            elif admin1==4:
                food.remove_food_item()
            elif admin1==0:
                break
    elif start==2:
        user1=int(input('choose one of the following:\n1.exsisting user\n2.new user\n0.exit'))
        if user1==1:
            nameuser=input('nameuser')
            userpassword=input('userpassword')
            p=user.log_in_user(nameuser,userpassword)
        elif user1==2:
            user.new_user(input('name'),int(input('mobile number')),input('email'),input('address'),input('password')) 
            nameuser=input('nameuser')
            userpassword=input('userpassword')
            p=user.log_in_user(nameuser,userpassword)
        elif user1==0:
            break
        if p==True:
            option1=int(input('choose one of the following\n1.place new order\n2.view order history\n3.update profile\n0.exit'))
            if option1==1:
                user.place_new_order()
            elif option1==2:
                print(user.order_history)
            elif option1==3:
                user.update_profile()
            elif option1==0:
                break
    elif start==0:
        print('Thank You for Visiting')
        break










