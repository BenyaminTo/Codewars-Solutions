using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;

namespace IP_Validation
{
    public class Kata
    {
        public static bool isValidIP(string ipAddres)
        {
            bool is_valid = true;
            var splitedIPs = ipAddres.Split('.');
            if (splitedIPs.Count() == 4 && !ipAddres.Contains(' '))
            {
                foreach (string ip in splitedIPs)
                {
                    if (ip.StartsWith('0') && ip != "0")
                    {
                        is_valid = false;
                        break;
                    }
                    try
                    {
                        byte ipdec = Convert.ToByte(ip);
                        if (ipdec <= 255 && ipdec >= 0)
                            continue;
                        else
                            is_valid = false; break;
                    }
                    catch (Exception)
                    {
                        is_valid = false;
                        break;
                    }
                }
            }
            else
            {
                is_valid = false;
            }
            return is_valid;
        }
    }
    class KataBest
    {
        public static bool IsValidIp(string ipAddress)
        {
            var octets = ipAddress.Split(".");

            if (octets.Count() != 4) return false;

            foreach (var octet in octets)
            {
                if (!int.TryParse(octet, out int numericOctet))
                    return false;

                if (numericOctet < 0 || numericOctet > 255)
                    return false;

                if (!numericOctet.ToString().Equals(octet))
                    return false;
            }

            return true;
        }
    }
}
