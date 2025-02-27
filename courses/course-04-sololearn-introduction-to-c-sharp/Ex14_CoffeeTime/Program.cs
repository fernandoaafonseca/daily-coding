/*
Coffee Time!

A coffee vending machine makes 3 types of coffee ☕:
1 - Americano
2 - Espresso
3 - Cappuccino
The given program takes the number from the customer as input.

Task
Complete the program to serve the corresponding coffee type. It should output Unknown if there is no match.

Input Example⬅️: 2
Output Example➡️: Espresso

Remember to terminate each case using the break statement. 
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("1 - Americano");
        Console.WriteLine("2 - Espresso");
        Console.WriteLine("3 - Cappuccino");

        Console.Write("Enter an option: ");
        int choice = Convert.ToInt32(Console.ReadLine());

        //your code goes here
        Console.WriteLine(CheckUserOption(choice));
        RunSimpleTests();
    }

    static string CheckUserOption(int choice)
    {
        switch (choice)
        {
            case 1:
                return "Americano";
            case 2:
                return "Espresso";
            case 3:
                return "Cappuccino";
            default:
                return "Unknown";
        }
    }

    static void RunSimpleTests()
    {
        int choice;

        choice = 1;
        Console.WriteLine(CheckUserOption(choice) == "Americano");

        choice = 2;
        Console.WriteLine(CheckUserOption(choice) == "Espresso");

        choice = 3;
        Console.WriteLine(CheckUserOption(choice) == "Cappuccino");

        choice = 5;
        Console.WriteLine(CheckUserOption(choice) == "Unknown");
    }
}