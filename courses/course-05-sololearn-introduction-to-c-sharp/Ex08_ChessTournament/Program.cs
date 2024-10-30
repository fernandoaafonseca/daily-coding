/*
Chess Tournament

You are making a program for a chess tournament that needs to calculate the points earned by a player.
A win is worth 1 point, while a tie is worth 0.5 points.
The given program declares two variables: wins and ties.

Task
Create a program to take the values for wins and ties as input, then calculate and output the points earned by the player.

Hint
Multiply the ties value by 0.5, to get the points earned for ties.
You need to take the values as input by using the Console.ReadLine method, and convert them to integers.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        int wins;
        int ties;

        //your code goes here
        wins = int.Parse(Console.ReadLine());
        ties = int.Parse(Console.ReadLine());

        double totalPoints = wins + ties * 0.5;
        Console.WriteLine(totalPoints);

        Tests();
    }

    static void Tests()
    {
        int wins;
        int ties;
        double totalPoints;

        wins = 54;
        ties = 31;
        totalPoints = wins + ties * 0.5;
        Console.WriteLine(totalPoints == 69.5);

        wins = 5;
        ties = 6;
        totalPoints = wins + ties * 0.5;
        Console.WriteLine(totalPoints == 8);
        
        wins = 14;
        ties = 7;
        totalPoints = wins + ties * 0.5;
        Console.WriteLine(totalPoints == 17.5);
                
        wins = 1;
        ties = 2;
        totalPoints = wins + ties * 0.5;
        Console.WriteLine(totalPoints == 2);
    }
}