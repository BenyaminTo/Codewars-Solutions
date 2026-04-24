using System;

namespace kata_string_endswith
{
    class Program
    {
        static void Main(string[] args)
        {
            string str, ending;
            Console.WriteLine("enter two string:");
            str = Console.ReadLine();
            ending = Console.ReadLine();
            Console.WriteLine(Solution2(str, ending));
        }
        public static bool Solution1(string str, string ending)
        {
            for(int i = ending.Length - 1 , j = str.Length -1; i >= 0 ; i-- , j--){
                if( str[j] != ending[i]|| ending.Length > str.Length)
                    return false;
            }
            return true;
        }
        public static bool Solution2(string str, string ending)
        {
            return str.EndsWith(ending);
        }
    }
}