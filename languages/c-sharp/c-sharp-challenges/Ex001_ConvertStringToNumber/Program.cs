/*
Convert a String to a Number!

Note: This kata is inspired by Convert a Number to a String!. Try that one too.

Description
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7

Source: codewars.com
*/
using System;

public class Program
{
    static void Main(string[] args)
    {
        RunTests();
    }

    public static int StringToNumber(String numString)
    {
        //TODO: Convert str into a number
        int num = int.Parse(numString);
        return num;
    }

    public static void RunTests()
    {
        string numString;
        int num;
        int expectedResult;

        numString = "1234";
        num = StringToNumber(numString);
        expectedResult = 1234;
        Console.WriteLine(num == expectedResult);
        
        numString = "605";
        num = StringToNumber(numString);
        expectedResult = 605;
        Console.WriteLine(num == expectedResult);
        
        numString = "1405";
        num = StringToNumber(numString);
        expectedResult = 1405;
        Console.WriteLine(num == expectedResult);
        
        numString = "-7";
        num = StringToNumber(numString);
        expectedResult = -7;
        Console.WriteLine(num == expectedResult);
    }
}