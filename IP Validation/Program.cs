// See https://aka.ms/new-console-template for more information
using IP_Validation;

string[] test = new string[] { "0.0.0.0" , "12.255.56.1" , "137.255.156.100"
    , "" , "abc.def.ghi.jkl" , "123.456.789.0" , "12.34.56" , "12.34.56.00" ,
     "12.34.56.7.8" , "12.34.256.78" , "1234.34.56" , "pr12.34.56.78" , "12.34.56.78sf" ,
     "12.34.56 .1" , "12.34.56.-1" , "123.045.067.089"};
foreach (var item in test)
{
    Console.WriteLine(item + " : " + Kata.isValidIP(item));
}


