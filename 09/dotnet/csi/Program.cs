using System;
using System.Collections.Generic;
using System.IO;

namespace csi
{
    class Program
    {
        static string getDNA()
        {
            using (StreamReader reader = new StreamReader("dna.txt"))
            {
                string dna = reader.ReadToEnd();
                return dna;
            } 
        }
        static string findSuspect()
        {
            // Get the dna results
            string results = getDNA();
            
            // Create a list with all the suspects
            List<Suspect> suspects = new List<Suspect>();
            suspects.Add(new Suspect("Eva", "Blonde", "Oval", "Blue", "Female", "White"));
            suspects.Add(new Suspect("Larisa", "Brown", "Oval", "Brown", "Female", "White"));
            suspects.Add(new Suspect("Matej", "Black", "Oval", "Blue", "Male", "White"));
            suspects.Add(new Suspect("Miha", "Brown", "Square", "Green", "Male", "White"));
            
            var found = false;
            string report = "Suspect not found!";

            foreach (Suspect suspect in suspects)
            {
                found = true;
                Dictionary<string, string> dna = Dna.getSuspectDNA(suspect);
                foreach (KeyValuePair<string, string> property in dna)
                {
                    if(property.Key == "name")
                    {
                        continue;    
                    }
                    if (!results.Contains(property.Value))
                    {
                        found = false;
                        break;
                    }
                }
                if (found)
                {
                    return $"It was {suspect.name}";
                }
            }

            return report;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("A hidious crime has occured.");
            Console.WriteLine();
            Console.WriteLine("We have a DNA sample ... ");
            Console.WriteLine();
            Console.WriteLine("... and a set of suspects.");
            Console.WriteLine();
            Console.WriteLine("Let's find out who comited the crime... ");
            Console.WriteLine("*dramatic music playing*");
            Console.WriteLine(findSuspect());
        }
    }
}
