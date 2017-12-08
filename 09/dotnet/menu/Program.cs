using System;
using System.Collections.Generic;
using menu.table;

namespace menu
{
    class Dish
    {
        // This is a base class for dishes. The fields
        // will have to be both of type string, when we
        // display them.
        private string name;
        private float price;
        
        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
            }
        }
        public float Price
        {
            get
            {
                return price;
            }
            set
            {
                price = value;
            }
        }

        public Dish(string dishName, float dishPrice)
        {
            // This constructor is not needed, it is implemented for learning purposes
            name = dishName;
            price = dishPrice;
        }
        public List<string> getDish()
        {
            // To make it easier to pass around and to create a table
            // we transform the price field to a string. 
            List<string> stringified = new List<string>();
            stringified.Add(Name);
            stringified.Add(Price.ToString());
            return stringified;
        }
    }
    class Menu
    {
        private List<Dish> dishes = new List<Dish>();
        public List<Dish> Dishes
        {
            get
            {
                return dishes;
            }
            set
            {
                dishes = value;
            }
        }
        public void addDish(Dish dish)
        {
            Dishes.Add(dish);
        }
        public void removeDish(int index)
        {
            // Menu uses indexes to remove dishes from the menue
            // A method to search by dish name is not implemented
            // yet and for the purpose of this exercise it is not
            // neede.
            Dishes.RemoveAt(index);
        }
        public List<List<string>> getMenu()
        {
            List<List<string>> menuItems = new List<List<string>>();
            foreach (var dish in Dishes)
            {
                menuItems.Add(dish.getDish());
            }
            return menuItems;
        }
        
    }
    class Program
    {
        static float getPrice(string dishName)
        {
            bool done = false;
            var price = 0.0f;
            
            while (!done)
            {
                Console.WriteLine($"Please enter the price for {dishName} or press 'q' to exit: ");
                string priceString = Console.ReadLine();
                if (priceString == "q") {
                    Environment.Exit(-1);
                }
                try
                {
                    var _price = Single.Parse(priceString);
                    price = _price;
                    done = true;
                }
                catch (FormatException)
                {
                    Console.WriteLine("Please enter a positive number.");
                }
            }
            return price;
        }
        static void Main(string[] args)
        {
            var done = false;

            Console.WriteLine("Let's make a menu!");
            
            List<string> headers = new List<string>(new string[] {"Jed", "Cena"});
            Menu menu = new Menu();

            while (!done)
            {
                Console.WriteLine("Please add a dish by entering the name of the dish or press 'q' to quit.");
                string dish = Console.ReadLine();
                if (dish == "q")
                {
                    Environment.Exit(-1);
                }
                float price = getPrice(dish);
                Dish newDish = new Dish(dish, price);
                
                menu.addDish(newDish);
                Table table = new Table(menu.getMenu(), headers);
                table.drawTable();
                if (menu.Dishes.Count > 0)
                {
                    Console.WriteLine("Remove an item?");
                }
            }
        }
    }
}
