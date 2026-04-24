using System;

namespace kata__binary_addition
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b;
            Console.WriteLine("enter two number:");
            a = Int32.Parse(Console.ReadLine());
            b = Int32.Parse(Console.ReadLine());
            Console.WriteLine(AddBinary(a, b));
        }
        public static string AddBinary(int a, int b)
        {
              int temp, sum = a + b;
              string strb = "";
              while (sum > 0 )
              {
                 temp = sum % 2;
                 strb += temp;
                 sum = sum / 2;
              }
              char[] array = strb.ToCharArray();
              Array.Reverse(array);
              return (new string(array));
              /*
                 return Convert.ToString(a + b, 2); //A much simpler solution
               */
        }
    }
}