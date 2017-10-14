using System;

namespace guess
{
    class Program
    {
        static void Main()
        {
            // Get random number from 1 to 20
            Random rnd = new Random();
            int secret = rnd.Next(1,20);
            
            // Start a While loop
            Boolean looping = true;
            Console.WriteLine("I created a number beetwen 1 and 20, care to take a guess what it is?");
            while (looping) {
                string userInput = Console.ReadLine();
                try {
                    int guesed = Convert.ToInt32(userInput);
                    if (guesed == secret) {
                        Console.WriteLine("Correct! The secret number was {0}", secret);
                        break;
                    }
                    Console.WriteLine("Too bad! Try again!");
                } catch (FormatException) {
                    Console.WriteLine("Please, enter a number, or press CTR+c to exit the programm.");
                    continue;
                }
            }
        }
    }
}
