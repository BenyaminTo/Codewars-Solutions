// See https://aka.ms/new-console-template for more information
Console.WriteLine("");
int[] arr = { 1, 2, 0, 1, 0, 1, 0, 3, 0, 1 };
Console.WriteLine(Kata.MoveZeroes(arr));
public class Kata
{
    public static int[] MoveZeroes(int[] arr)
    {
        // TODO: Program me
        int[] resault = new int[arr.Length];
        int item, j = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] != 0)
            {
                resault[j] = arr[i];
                j++;
            }
        }
        return resault;
    }
}
