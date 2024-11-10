/*
Feet to Inches Converter

You need to make a function that converts a foot value to inches.
1 foot has 12 inches.
The given code takes the foot value as input and passes it to the Converter method.

Task
Define a Converter method that takes the foot value as an argument and outputs the inches value.

Input Example⬅️: 8
Output Example➡️: 96
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        double foot = Convert.ToDouble(Console.ReadLine());
        double inches = Converter(foot);
        Console.WriteLine(inches);
        RunSimpleTests();
    }

    //your code goes here
    static double Converter(double foot)
    {
        double inches = foot * 12;
        return inches;
    }

    static void RunSimpleTests()
    {
        double foot;
        double inches;
        double expectedResult;

        foot = 8;
        inches = Converter(foot);
        expectedResult = 96;
        Console.WriteLine(inches == expectedResult);
        
        foot = 55;
        inches = Converter(foot);
        expectedResult = 660;
        Console.WriteLine(inches == expectedResult);
        
        foot = 12;
        inches = Converter(foot);
        expectedResult = 144;
        Console.WriteLine(inches == expectedResult);
        
        foot = 1000;
        inches = Converter(foot);
        expectedResult = 12000;
        Console.WriteLine(inches == expectedResult);
        
        foot = 1;
        inches = Converter(foot);
        expectedResult = 12;
        Console.WriteLine(inches == expectedResult);
    }
}