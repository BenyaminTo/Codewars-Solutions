using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RGB_To_Hex_Conversion
{
    internal class Kata
    {
       
        public static string Rgb(int r , int g, int b)
        {
            int R = Check(r);
            int G = Check(g);
            int B = Check(b);
            string hex = "";
            if (R.ToString("X").Length == 1)
            {
                hex += "0";
            }
            hex += R.ToString("X");
            if (G.ToString("X").Length == 1)
            {
                hex += "0";
            }
            hex += G.ToString("X");
            if (B.ToString("X").Length == 1)
            {
                hex += "0";
            }
            hex += B.ToString("X");

            return hex;
        }
        private static int Check(int x)
        {
            if (x > 255)
                return 255;
            else if (x < 0)
                return 0;
            else
                return x;
        }
        public static string Rgb_best(int r, int g, int b)
        {
            r = Math.Max(Math.Min(255, r), 0);
            g = Math.Max(Math.Min(255, g), 0);
            b = Math.Max(Math.Min(255, b), 0);
            return String.Format("{0:X2}{1:X2}{2:X2}", r, g, b);
        }
    }
}
