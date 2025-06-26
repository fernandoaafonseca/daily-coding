/*
Fixing Simple Bugs

Instructions:
Please, avoid changing the given source code for the exercise! So only add code, don't modify unless it is instructed to do so!

#########################################
Create a C# program that correctly calculates and displays the average of three numbers. The provided code has several bugs that prevent it from compiling and running correctly.

Alert!

The result of execution for the default string should be:
"The average is: 20"

The "Solution Explanation" tab above will unlock on the third failed attempt. There you should find our solution to this exercise. However, try to solve it yourself first!

We have faith in you 💕

- Learning objective:
Your task is to identify and correct these bugs to ensure the program functions as intended.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        CalculateAverage();
    }
    static void CalculateAverage()
    {
        int num1 = 10;
        int num2 = 20;
        int num3 = 30;
        int average = (num1 + num2 + num3) / 3;
        Console.WriteLine($"The average is: {average}");
    }
}