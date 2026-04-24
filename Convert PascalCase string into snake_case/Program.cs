using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Convert_PascalCase_string_into_snake_case
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter your string or number:");
            Console.WriteLine(KataBest.ToUnderscore(Console.ReadLine()));
            Console.ReadKey();
        }
    }
}
