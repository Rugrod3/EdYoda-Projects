food_item_list=[{'name':'veg','food_id':0,'price':200,'quantity':1,'stock':10}]
def add_food_item(name,food_id,price,quantity,stock):
    food_item_list.append({'Name':name,"Price":price,"food_id": food_id,"quantity": quantity,"Stock": stock})

food_item_list=food_item_list
def edit_food_item():
    m=input('please enter food id:')
    if m==food_item_list[m]['food_id']:
        food_item_list[m]["Name"]=input('name')
        food_item_list[m]["Price"]=input('price')
        food_item_list[m]["quantity"]=input('quantity')
        food_item_list[m]["Stock"]=input('stock')
        food_item_list[m]['food_id']=int(input('food_id'))
        
    else:
        print('enter correct food_id')

def view_food_list():
    print(food_item_list)

def remove_food_item():
    n=int(input("enter food id"))
    if n==food_item_list[n]['food_id']:
        food_item_list.pop(n)
        for w in range(0,len(food_item_list)):
            if w>n:
                food_item_list[w]['food_id']-=1
    return food_item_list