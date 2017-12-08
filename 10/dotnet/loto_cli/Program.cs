using System;
using Microsoft.Extensions.CommandLineUtils;

namespace loto_cli
{
    class Program
    {
        static void Main(string[] args)
        {
            var app = new CommandLineApplication();
            app.Name = "loto_cli";
            app.HelpOption("-?|-h|--help");

            app.OnExecute(() =>
                {
                    string winingNumbers = Numbers.getNumbers();
                    
                    Console.WriteLine("This weeks winning numbers are ... ");
                    Console.WriteLine();
                    Console.WriteLine(winingNumbers);
                    Console.WriteLine();
                    return 0;
                }
            );
        }
    }
}
