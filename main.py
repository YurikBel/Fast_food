from Listener import *
from Order import *
from dish import *
fri1 = Simple_dish('Картошка', '150р')
burger1 = Simple_dish('Бургер', '200')

fri = Simple_dish('Картошка', '150р')
burger = Simple_dish('Бургер', '200')
combo1 = Combo_dish('Комбо', '350', [fri, burger])
me = Client()
kitchen = Kitchen()

order = Order([fri1, combo1], 89456, [me, kitchen])
order.AddMeal(burger1)
print(order.GetSimpleMeals())
order.MakeMealReady(burger)
order.MakeMealReady(fri)
order.MakeMealReady(burger1)
order.MakeMealReady(fri1)


print(order.GetSimpleMeals())

print(order._dishes)
print(order.GetReceiptInfo())