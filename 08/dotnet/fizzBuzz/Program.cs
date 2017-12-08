using System;

namespace fizzBuzz
{
    class Program
    {
        static void FizzBuzz(int num)
        {
            if (num % 15 == 0) {
                Console.WriteLine("FizzBuzz!");
            }
            else if (num % 5 == 0)
            {
                Console.WriteLine("Buzz!");
            }
            else if (num % 3 == 0)
            {
                Console.WriteLine("Fizz!");
            }
            else
            {
                Console.WriteLine(num);
            }
        }

        static void Main(string[] args)
        {
            bool done = false;

            Console.WriteLine("This is a simple fizzbuzz program that prints numbers from 1 to n.");
            
            while (!done)
            {
                Console.WriteLine("Please enter a number beetwen 1 and 100: ");
                try
                {
                    var finalNumber = Int32.Parse(Console.ReadLine()); 
                    if (finalNumber >= 1 && finalNumber <= 100)
                    {
                        for (int x = 1; x <= finalNumber; x++ )
                        {
                            FizzBuzz(x);
                        }
                        done = true;
                    }
                }
                catch (FormatException)
                {
                    Console.WriteLine("Please enter an intiger beetwen 1 and 100.");
                }
            }
            
        }
    }
}
