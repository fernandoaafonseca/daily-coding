/*
Simple Operations
Ever wondered how many seconds are there in a month (30 days) 🕰️?
Let's calculate it! 

Task
Write a program to calculate and output the answer.

Hint
Remember, there are 24 hours in a day, 60 minutes in an hour, and 60 seconds in a minute.
Use the multiplication operator * inside the Console.WriteLine method.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        /*
        30 days
        1 day = 24 hours
        1 hour = 60 minutes
        1 minute = 60 seconds
        */

        //your code goes here
        int secsInOneMin = 60;
        int minsInOneHour = 60;
        int hoursInOneDay = 24;
        int daysInOneMonth = 30;

        int secsInOneMonth = secsInOneMin * minsInOneHour * hoursInOneDay * daysInOneMonth;
        Console.WriteLine(secsInOneMonth);
    }
}