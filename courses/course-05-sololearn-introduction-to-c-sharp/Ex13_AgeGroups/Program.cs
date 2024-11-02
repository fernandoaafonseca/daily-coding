/*
Age Groups

The given program takes the age of a person as input.

Task
Write a program to output their age group.
Here are the age groups you need to handle:
Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64

Input Example⬅️: 42
Output Example➡️: Adult

Use the logical AND operator &&.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter the age: ");
        int age = Convert.ToInt32(Console.ReadLine());

        //your code goes here
        Console.WriteLine($"{CheckAgeGroup(age)}");

        RunSimpleTests();

    }

    static string CheckAgeGroup(int age)
    {
        if (age >= 0 && age <= 11)
        {
            return "Child";
        }
        else if (age >= 12 && age <= 17)
        {
            return "Teen";
        }
        else if (age >= 18 && age <= 64)
        {
            return "Adult";
        }
        else
        {
            return "Invalid age";
        }
    }

    static void RunSimpleTests()
    {
        int age;

        age = 19;
        Console.WriteLine(CheckAgeGroup(age) == "Adult");

        age = 15;
        Console.WriteLine(CheckAgeGroup(age) == "Teen");

        age = 33;
        Console.WriteLine(CheckAgeGroup(age) == "Adult");

        age = 5;
        Console.WriteLine(CheckAgeGroup(age) == "Child");

        age = 2;
        Console.WriteLine(CheckAgeGroup(age) == "Child");

        age = -1;
        Console.WriteLine(CheckAgeGroup(age) == "Invalid age");

        age = 65;
        Console.WriteLine(CheckAgeGroup(age) == "Invalid age");
    }
}