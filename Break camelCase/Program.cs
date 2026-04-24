using System.Diagnostics;

[DebuggerDisplay($"{{{nameof(GetDebuggerDisplay)}(),nq}}")]
internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Please Enter a string:");
#pragma warning disable CS8604 // Possible null reference argument.
        Console.WriteLine(Kata.BreakCamelCase(str: Console.ReadLine()));
    }

    private string GetDebuggerDisplay()
    {
#pragma warning disable CS8603 // Possible null reference return.
        return ToString();
#pragma warning restore CS8603 // Possible null reference return.
    }
}
#pragma warning restore CS8604 // Possible null reference argument.
public class Kata
{
    public static string BreakCamelCase(string str)
    {
        string resault = "";
        int indexUp = 0;
        foreach (char c in str)
        {
            if (char.IsUpper(c) && indexUp != 0)
            {
                resault += " " + c; 
            }
            else
            {
                resault += c;
            }
            indexUp++;
        }
        return resault;
    }
}
