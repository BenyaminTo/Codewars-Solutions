using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace RGB_To_Hex_Conversion
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int r, g, b;    
            Console.WriteLine("Please enter three parmeters:");
            r = int.Parse(Console.ReadLine());
            g = int.Parse(Console.ReadLine());
            b = int.Parse(Console.ReadLine());
            Kata kata = new Kata();
            Console.WriteLine(Kata.Rgb_best(r ,g ,b));
            Console.ReadLine();
        }
    }
}
