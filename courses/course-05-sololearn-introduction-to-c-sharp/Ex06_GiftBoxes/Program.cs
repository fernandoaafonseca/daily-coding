/*
Gift Boxes

You are making gift boxes 🎁. Each box contains 9 items.

Task
Given 200 items in total, you need to calculate and output how many items will be left over if you create gift boxes from all of the items.

The modulo operator % can be useful in solving this challenge.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        int items = 200;
        int itemInBox = 9;

        //your code goes here
        int remainder = items % itemInBox;
        Console.WriteLine(remainder);
    }
}