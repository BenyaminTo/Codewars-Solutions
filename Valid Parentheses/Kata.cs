using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
public class Kata
{
    public static bool ValidParentheses(string str)
    {
        int paR = 0, paL = 0;
        bool flag = true;
        if (str.Length == 0)
        {
            return flag;
        }
        if (str.Length % 2 != 0 || (str[0] == ')' && str.Length != 0))
        {
            flag = false;
            return flag;
        }
        for (int i = 0; i < str.Length;i++)
        {
            _ = (str[i] == '(') ? paL++ : paR++;
            if (paL == paR)
            {
                paL = paR = 0;
                if (i+1 < str.Length && str[i + 1] == ')')
                {
                    flag = false;
                    break;
                }
            }
            if (paL != paR && i == str.Length -1)
            {
                flag = false;
                break;
            }
        }
        return flag;
    }
}
public class Kata_Best
{
    public static bool ValidParentheses(string str)
    {
        int open = 0;
        foreach (char paren in str)
        {
            open += paren == '(' ? 1 : -1;
            if (open < 0)
            {
                return false;
            }
        }
        return open == 0;
    }
}

