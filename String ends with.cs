public class Kata
{
  public static bool Solution(string str, string ending)
        {
            for(int i = ending.Length - 1 , j = str.Length -1; i >= 0; i-- , j--){
                if( str[j] != ending[i] || ending.Length > str.Length)
                    return false;
            }
            return true;
    
        }
}