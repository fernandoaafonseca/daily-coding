/*
Simple Variables Introduction
#########################################
Please, avoid changing the given source code for the exercise! So only add code, don't modify unless it is instructed to do so!
#########################################
Create a simple C# program that declares an integer variable, assigns it the value 10, and prints the value to the console.

Alert!

The result of execution for the default string should be:
"10"

The "Solution Explanation" tab above will unlock on the third failed attempt. There you should find our solution to this exercise. However, try to solve it yourself first!

We have faith in you 💕

- Learning objective:
Create a simple C# program that declares an integer variable, assigns it a value, and prints the value to the console.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        PrintNumber();
    }
    static void PrintNumber()
    {
        int myInt = 10;
        Console.WriteLine(myInt);
    }
}