/*
Organized Robot🤖

You are developing a program that will be used in a robot that categorizes items by their color.
Each color corresponds to a box with a specific number.
For simplicity, our program will handle 3 colors:
🔴 red goes to box #1
🟢 green goes to box #2
⚫ black goes to box #3

Your program needs to take color as input and output the corresponding box in the given format.
In the case of an unsupported colors, the program should output unknown.

Input Example⬅️: green
Output Example➡️: box #2

Remember, you can use the if else statements to check for different conditions.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        string color = Console.ReadLine();

        //your code goes here
        string box = CheckColorBox(color);
        Console.WriteLine(box);

        RunSimpleTests();
    }

    static string CheckColorBox(string color)
    {
        if (color == "red")
        {
            return "box #1";
        }
        else if (color == "green")
        {
            return "box #2";
        }
        else if (color == "black")
        {
            return "box #3";
        }
        else
        {
            return "unknown";
        }
    }

    static void RunSimpleTests()
    {
        string color;

        color = "green";
        Console.WriteLine(CheckColorBox(color) == "box #2");

        color = "white";
        Console.WriteLine(CheckColorBox(color) == "unknown");

        color = "red";
        Console.WriteLine(CheckColorBox(color) == "box #1");

        color = "yellow";
        Console.WriteLine(CheckColorBox(color) == "unknown");
        
        color = "black";
        Console.WriteLine(CheckColorBox(color) == "box #3");

    }
}