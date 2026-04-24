// See https://aka.ms/new-console-template for more information
 using System.ComponentModel;
using System.Text;
using System.Diagnostics;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Enter a Roman Number:");
        Console.WriteLine(RomanNumerals.FromRoman(Console.ReadLine()));
        Console.WriteLine("Enter a integer:");
        Console.WriteLine(RomanNumerals.ToRoman(Convert.ToInt32(Console.ReadLine())));
    }
}

public class RomanNumerals
{
    public static string ToRoman(int number)
    {
        if ((number < 0) || (number > 3999)) throw new ArgumentOutOfRangeException("insert value betwheen 1 and 3999");
        if (number < 1) return string.Empty;
        if (number >= 1000) return "M" + ToRoman(number - 1000);
        if (number >= 900) return "CM" + ToRoman(number - 900);
        if (number >= 500) return "D" + ToRoman(number - 500);
        if (number >= 400) return "CD" + ToRoman(number - 400);
        if (number >= 100) return "C" + ToRoman(number - 100);
        if (number >= 90) return "XC" + ToRoman(number - 90);
        if (number >= 50) return "L" + ToRoman(number - 50);
        if (number >= 40) return "XL" + ToRoman(number - 40);
        if (number >= 10) return "X" + ToRoman(number - 10);
        if (number >= 9) return "IX" + ToRoman(number - 9);
        if (number >= 5) return "V" + ToRoman(number - 5);
        if (number >= 4) return "IV" + ToRoman(number - 4);
        if (number >= 1) return "I" + ToRoman(number - 1);
        else return "Error!";
    }
    private static readonly Dictionary<char, int> RomanMap = new Dictionary<char, int>()
    {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };
    public static int FromRoman(string romanNumeral)
    {
        int number = 0;
        if (romanNumeral != null)
        {
            for (int i = 0; i < romanNumeral.Length; i++)
            {
                if (i + 1 < romanNumeral.Length && RomanMap[romanNumeral[i]] < RomanMap[romanNumeral[i + 1]])
                {
                    number -= RomanMap[romanNumeral[i]];
                }
                else
                {
                    number += RomanMap[romanNumeral[i]];
                }
            }
            return number;
        }
        else
            return 0;
    }
}
