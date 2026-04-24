using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Count_IP_Addresses
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter Start IP:");
            string stIP = Console.ReadLine();
            Console.WriteLine("Enter End IP:");
            string enIP = Console.ReadLine();
            Console.WriteLine(CountIPAddresses.IpsBetween_Best(stIP, enIP));
            Console.ReadLine();
        }
    }
}
