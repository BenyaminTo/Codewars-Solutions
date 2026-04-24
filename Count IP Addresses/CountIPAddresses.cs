using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace Count_IP_Addresses
{
    internal class CountIPAddresses
    {
        public static long IpsBetween(string start, string end)
        {
            string[] startIP =  start.Split('.');
            string[] endIP = end.Split('.');
            long[] IPdifference = new long[4];
            long IPdiff = 0;
            for (int i = 0, j = 16777216; i < 4; i++, j /= 256)
            {
                IPdifference[i] = Convert.ToInt64(endIP[i]) - Convert.ToInt64(startIP[i]);
                IPdiff += IPdifference[i] * j;
            }
            return IPdiff;
        }
        public static long IpsBetween_Best(string start, string end)
        {
            return (long)(uint)IPAddress.NetworkToHostOrder((int)IPAddress.Parse(end).Address) - (long)(uint)IPAddress.NetworkToHostOrder((int)IPAddress.Parse(start).Address);

        }
    }
}

