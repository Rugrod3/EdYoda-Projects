
import food
def log_in_user(nameuser,userpassword):
    pw = login_info_user.get(nameuser)
    if pw != userpassword:
        print('Wrong username or password')
        return False
    else:
        return True

login_info_user = {}
user_detail=[]
order_history=[]
def place_new_order():
    new_order=int(input('please enter the food id of the food you want to order:'))
    if food.food_item_list[new_order]['stock']!=0:
        if new_order in range(0,len(food.food_item_list)):
            print('you have ordered' )
            print(f'{food.food_item_list[new_order]["name"]}')
            order_history.append(food.food_item_list[new_order]['name'])
        else:
            print('enter correct food id')
        food.food_item_list[new_order]['stock']-=1
        return food.food_item_list
    else:
        print('sorry ')
        print(f'{food.food_item_list[new_order]["name"]}')
        print('is out of stock')

def new_user(name,mobile_number,email,address,password):
    user_detail.append({'name':name,'mobile_number':mobile_number,'email':email,'address':address,'password':password})
    login_info_user[name]=password

def update_profile(name,mobile_number,email,address,password):
    user_detail['name']=input('name')
    user_detail['mobile_number']=input('mobile_number')
    user_detail['email']=input('email')
    user_detail['address']=input('address')
    user_detail['password']=input('password')
    login_info_user[name]=password
    print(user_detail)

