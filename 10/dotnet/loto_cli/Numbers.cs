using System;
using System.Collections.Generic; 

namespace loto_cli
{
    public static class Numbers
    {
        public static string getNumbers(int len = 8, int maxNumber = 39)
        {
            // Instantiate the random number generator
            Random rnd = new Random();
            
            // We use an array to store our wining number
            // but a list would be the same
            int[] selectedNumber = new int[len];
            
            for (int i = 0; i < len; i++)
            {
                int secret;
                do
                {
                    secret = rnd.Next(1, maxNumber);
                } while (Array.Exists(selectedNumber, x => x == secret));
                selectedNumber[i] = secret;
            }
            Array.Sort(selectedNumber);
            string stringifiedNumbers = string.Join(" ", selectedNumber);
            return stringifiedNumbers;
        }
    }
}