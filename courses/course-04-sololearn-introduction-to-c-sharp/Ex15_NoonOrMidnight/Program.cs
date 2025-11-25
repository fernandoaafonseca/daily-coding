/*
Noon Or Midnight

Time flies when you’re having fun.
You are given a digital clock that measures time over a 24 hour day, and a program that takes the hour of the day as input.

Task
Complete the program so that it outputs AM to the console if the time is between 0 and 12 (inclusive), and outputs PM if the time is between 13 and 24 (inclusive).

Input Example⬅️: 13
Output Example➡️: PM

Assume the input number is positive and less than or equal to 24.
*/


using System;

public class Program
{
    static void Main(string[] args)
    {
        int hour = Convert.ToInt32(Console.ReadLine());

        //your code goes here
        string periodOfDay = hour <= 12 ? "AM": "PM";
        Console.WriteLine(periodOfDay);

        RunSimpleTests();
    }

    static void RunSimpleTests()
    {
        int hour;
        string periodOfDay;

        hour = 9;
        periodOfDay = hour <= 12 ? "AM": "PM";
        Console.WriteLine(periodOfDay == "AM");
        
        hour = 19;
        periodOfDay = hour <= 12 ? "AM": "PM";
        Console.WriteLine(periodOfDay == "PM");
                
        hour = 19;
        periodOfDay = hour <= 12 ? "AM": "PM";
        Console.WriteLine(periodOfDay == "PM");
                
        hour = 12;
        periodOfDay = hour <= 12 ? "AM": "PM";
        Console.WriteLine(periodOfDay == "AM");
                
        hour = 14;
        periodOfDay = hour <= 12 ? "AM": "PM";
        Console.WriteLine(periodOfDay == "PM");
    }
}