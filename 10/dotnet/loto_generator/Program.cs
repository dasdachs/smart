using System;

namespace loto_generator
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] winingNumbers = Numbers.getNumbers();
            string numbers = string.Join(" ", winingNumbers);
            
            Console.WriteLine("This weeks winning numbers are ... ");
            Console.WriteLine();
            Console.WriteLine(numbers);
            Console.WriteLine();
        }
    }
}
