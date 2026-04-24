using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Convert_PascalCase_string_into_snake_case
{
    internal class Kata
    {
        public static string ToUnderscore(int str)
        {
            return str.ToString();
            throw new NotImplementedException();
        }
        public static string ToUnderscore(string str)
        {
            string Underscore = "";
            Underscore += str[0];
            for (int i = 1; i < str.Count(); i++)
            {
                if ((int)str[i] >= 65 && (int)str[i] <= 90)
                {
                    Underscore += "_" + str[i];
                }
                else
                {
                    Underscore += str[i];
                }
            }//end of for
            return Underscore.ToLower();
            throw new NotImplementedException();
        }//end of method
    }//end of class Kata
    public static class KataBest
    {
        public static string ToUnderscore(int str)
        {
            return ToUnderscore(str.ToString());
        }

        public static string ToUnderscore(string str)
        {
            StringBuilder sb = new StringBuilder();
            foreach (var ch in str)
            {
                if (Char.IsUpper(ch))
                {
                    sb.Append('_');
                }
                sb.Append(Char.ToLower(ch));
            }
            return sb.ToString().TrimStart('_');
        }//end of method
    }//end of class KataBest
}//end of namespace