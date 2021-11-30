
class Item:
    def __init__(self, itemName, itemCost):
        self.itemName = itemName
        self.itemCost = itemCost

class drink(Item):
    def __init__(self, drinkSize, drinkIceLevel):
        self.drinkSize = drinkSize
        self.drinkIceLevel = drinkIceLevel

class Food(Item):
    def __init__(self, dietTags):
        self.dietTags = dietTags

class Customer:
    def __init__(self,Order,Total): 
        self.Order= Order
        self.Total = Total
class menu:
    def __init__(self, customer):
        self.apps = []
        self.drinks = []
        self.main_course = []
        self.deserts = []

        self.customer = customer
        
        Burger = Food("Gluten Free")
        Burger.itemName = "Burger"
        Burger.itemCost = 1.99

        Salad = Food("Vegetarian")
        Salad.itemName = "Salad"
        Salad.itemCost = 2.99

        self.main_course.append(Salad)
        self.main_course.append(Burger)

        Fries = Food(" ")
        Fries.itemCost = .99
        Fries.itemName = "Fries"

        OnionRings = Food(" ")
        OnionRings.itemCost = 1.49
        OnionRings.itemName = "Onion Rings"

        self.apps.append(Fries)
        self.apps.append(OnionRings)

        Coke = drink(None, None)
        Coke.itemName = "Coke"
        Coke.itemCost = .79

        Sprite = drink(None, None)
        Sprite.itemName = "Sprite"
        Sprite.itemCost = .79

        self.drinks.append(Coke)
        self.drinks.append(Sprite)
        
        Cake = Food("Vegan")
        Cake.itemName = "Cake"
        Cake.itemCost = 1.49

        IceCream = Food("Dairy Free")
        IceCream.itemName = "Ice Cream"
        IceCream.itemCost = 1.49

        self.deserts.append(Cake)
        self.deserts.append(IceCream)

        self.select()

    def print_menu(self): 
        print("[1] Appetizers")
        print("[2] Drinks")
        print("[3] Main Course")
        print("[4] Deserts")
        print("[5] Exit Menu")
    
    def select(self):
        while True:
            self.print_menu()
            selection = 0
            try:
                selection =  int(input("Select Option: "))
            except ValueError:
                print("Invalid option, please choose again: ")

            if selection == 1:
                #show list of appetizers
                print("\nAppetizers")
                for i in range(len(self.apps)):
                    print("[", i+1, "] ",self.apps[i].itemName, " ", self.apps[i].itemCost, " " , self.apps[i].dietTags)
                print("[ 3 ]  Go back")
                print("\n")

                select = 0
                try:
                    select =  int(input("Select Option: "))
                except ValueError:
                    print("Invalid option, please choose again: ")
                if(select - 1 > len(self.apps)):
                    print("Invalid selection, please try again")
                    continue
                if(select == len(self.apps)+1):
                    continue
                self.customer.Order.append(self.apps[select-1])
                self.customer.Total += self.apps[select-1].itemCost
                
            elif selection == 2:
                #show list of drinks
                print("\nDrinks")
                for i in range(len(self.drinks)):
                    print("[", i+1, "] ",self.drinks[i].itemName, " ", self.drinks[i].itemCost)
                print("[ 3 ]  Go back")
                print("\n")

                select = 0
                try:
                    select =  int(input("Select Option: "))
                except ValueError:
                    print("Invalid option, please choose again: ")
                if(select - 1 > len(self.drinks)):
                    print("Invalid selection, please try again")
                    continue
                if(select == len(self.drinks)+1):
                    continue
                print("What Size?")
                print("[1] Small")
                print("[2] Medium")
                print("[3] Large")
                print("[4]  Go back")
                print("\n")

                size = 0;
                try:
                    size =  int(input("Select Option: "))
                except ValueError:
                    print("Invalid option, please choose again: ")
                if(size > 4):
                    print("Invaid selection, please try again")
                if(size == 4):
                    continue
                print("Ice Level?")
                print("[1] 100%")
                print("[2] 50%")
                print("[3] No Ice")
                print("[4] Go back")
                print("\n")

                ice = 0;
                try:
                    ice =  int(input("Select Option: "))
                except ValueError:
                    print("Invalid option, please choose again: ")
                if(ice > 4):
                    print("Invaid selection, please try again")

                if(ice == 4):
                    continue


                self.customer.Order.append(self.drinks[select-1])

                self.customer.Total += self.drinks[select-1].itemCost

            elif selection == 3:
                #show list of Main Courses
                print("\nList of Main Courses")
                for i in range(len(self.main_course)):
                    print("[", i+1, "] ", self.main_course[i].itemName, " ", self.main_course[i].itemCost, " " ,self.main_course[i].dietTags)
                print("[ 3 ]  Go back")
                print("\n")

                select = 0
                try:
                    select =  int(input("Select Option: "))
                except ValueError:
                    print("Invalid option, please choose again: ")
                if(select - 1 > len(self.main_course)):
                    print("Invalid selection, please try again")
                    continue
                if(select == len(self.main_course)+1):
                    continue
                self.customer.Order.append(self.main_course[select-1])
                self.customer.Total += self.main_course[select-1].itemCost

            elif selection == 4:
                #show list of Deserts:
                print("\nList of Deserts")
                for i in range(len(self.deserts)):
                    print("[", i+1, "] ",self.deserts[i].itemName, " ", self.deserts[i].itemCost, " " ,self.deserts[i].dietTags)
                print("[ 3 ]  Go back")
                print("\n")

                select = 0
                try:
                    select =  int(input("Select Option: "))
                except ValueError:
                    print("Invalid option, please choose again: ")
                if(select - 1 > len(self.deserts)):
                    print("Invalid selection, please try again")
                    continue
                if(select == len(self.deserts)+1):
                    continue
                self.customer.Order.append(self.deserts[select-1])
                self.customer.Total += self.deserts[select-1].itemCost
                
            elif selection == 5:
                #exit from menu:
                print("\nThank you, have a great day!")
                break

def main():
    Order = []
    Total = 0
    customer = Customer(Order, Total)
    menu(customer)

    print("\nItems in Order")
    for i in range(len(Order)):
        print(customer.Order[i].itemName, "   ", customer.Order[i].itemCost)
    print("\nSubtotal for this order: " , round(customer.Total, 2))


    print("\nSales tax: 8.25%")

    print("\nTotal: ", round(customer.Total * 1.0825, 2))
        
if __name__ == "__main__":
    main()