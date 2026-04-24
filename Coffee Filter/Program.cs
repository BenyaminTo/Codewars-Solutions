// See https://aka.ms/new-console-template for more information
using System.Collections.Immutable;
using System.Text;


static string search(int budjet , int[] prices)
{
    StringBuilder str = new();
    Array.Sort(prices);
    foreach (int price in prices)
        if (price >= budjet)
            str.Append(price + ",");
    return str.ToString().TrimEnd(',');
}
static string Search(int budget, int[] prices)
{
    return string.Join(",", prices.Where(i => i <= budget).OrderBy(i => i));
}