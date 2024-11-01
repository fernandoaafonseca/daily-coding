/*
Country Cards

You need to make country cards for a school project 📇.
The given program takes the country and the name of its capital name as input.

Task
Complete the code to output a string in the format you are given in the sample output 👇.

Sample Input
Portugal
Lisbon

Sample Output
Country: Portugal, Capital: Lisbon

Note the space after the colon 🧐.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        string country = Console.ReadLine();
        string capital = Console.ReadLine();

        //your code goes here
        Console.WriteLine($"Country: {country}, Capital: {capital}");
    }
}