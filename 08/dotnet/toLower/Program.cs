using System;

namespace toLower
{
    class Program
    {
        public static int Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Please enter a string.");
                return 1;
            }
            string input = args[0];
            Console.WriteLine(input.ToLower());
            return 1;
        }
    }
}
