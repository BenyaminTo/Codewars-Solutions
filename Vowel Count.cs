using System;
using System.Linq;

public static class Kata
{
    public static int GetVowelCount(string str)
    {
        int vowelCount = 0;
        for(int i = 0 ; i < str.Length ; i++)
          {
          switch(str[i])
            {
               case 'a':
                 vowelCount++;
                 break;
                case 'e':
                 vowelCount++;
                 break;
                case 'i':
                 vowelCount++;
                  break;
                case 'o':
                 vowelCount++;
                 break;
                case 'u':
                 vowelCount++;
                 break;
                default:
                 continue;
          }
        }
        return vowelCount;
    }
}