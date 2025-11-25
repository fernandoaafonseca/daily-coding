/*
Take your kindle!

Airlines are offering a special promotion for teenagers and are offering kindles to use during the flight.
The given program takes the passengers` age as input.

Task
Write a program to output Take your kindle , if the age is under or equal to 19.

Sample Input ⬇️
14

Sample Output ⬆️
Take your kindle

The program should output nothing if the age is above 19.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        int age = Convert.ToInt32(Console.ReadLine());

        // Output only if condition is met
        string message = TestCondition(age);
        if (!string.IsNullOrEmpty(message))
        {
            Console.WriteLine(message);
        }

        RunSimpleTests();
    }

    static string TestCondition(int age)
    {
        if (age <= 19)
        {
            return "Take your kindle";
        }
        return "";
    }

    static void RunSimpleTests()
    {
        int age;

        age = 19;
        Console.WriteLine(TestCondition(age) == "Take your kindle");

        age = 24;
        Console.WriteLine(TestCondition(age) == "");

        age = 14;
        Console.WriteLine(TestCondition(age) == "Take your kindle");

        age = 23;
        Console.WriteLine(TestCondition(age) == "");

        age = 18;
        Console.WriteLine(TestCondition(age) == "Take your kindle");
    }
}