using System.Collections.Generic;
using System.Linq;
using System;
using System.Text;

namespace Stop_gninnipS_My_sdroW
{
    class Program
    {
        public static string SpinWords(string sentence)
        {
            string[] str = sentence.Split(" ");
            string str_temp = "";
            foreach (string word in str)
            {
                if (word.Length >= 5)
                {
                    str_temp += Reverser(word.Reverse()) + " ";
                }
                else
                {
                    str_temp += word + " ";
                }
            }

            return str_temp.TrimEnd();
        }
        private static string Reverser(IEnumerable<char> enumerable)
        {
            string reversed = string.Empty;
            foreach (var _char in enumerable)
            {
                reversed += _char;               
            }
            return reversed;
        }
        public static void Main(string[] args)
        {
            string Words = Console.ReadLine();
            Console.WriteLine(SpinWords(Words));
        }
    }
}

