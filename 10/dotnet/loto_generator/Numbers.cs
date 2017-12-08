using System;
using System.Collections.Generic; 

namespace loto_generator
{
    public static class Numbers
    {
        public static int[] getNumbers(int len = 8, int maxNumber = 39)
        {
            // Instantiate the random number generator
            Random rnd = new Random();
            
            // We use an array to store our wining number
            // but a list would be the same
            int[] winingNumbers = new int[len];
            
            for (int i = 0; i < len; i++)
            {
                int secret;
                do
                {
                    secret = rnd.Next(1, maxNumber);
                } while (Array.Exists(winingNumbers, x => x == secret));
                winingNumbers[i] = secret;
            }
            Array.Sort(winingNumbers);
            return winingNumbers;
        }
    }
}