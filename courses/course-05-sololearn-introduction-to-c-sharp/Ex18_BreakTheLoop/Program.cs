/*
Break The Loop

The given code declares a loop and calculates the multiplication of all numbers from 1 to 10000.

Task
Make the necessary changes to break the loop when the result is larger than 10000 and output the result.

Hint
Use an if statement inside the loop and break the loop based on the given condition.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        int num = 1;

        for (int i = 1; i <= 100; i++)
        {
            //your code goes here
            if (num > 10000)
            {
                break;
            }
            num *= i;
        }
        Console.WriteLine(num);
    }
}