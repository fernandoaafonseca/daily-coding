/*
Strings

The given code declares a text variable with a value of "ABCD".

Task
Write a program to output each letter on a separate line, like this 👇:
A
B
C
D

Use \n between the letters 😉.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        string text = "ABCD";
        foreach (char c in text)
        {
            Console.WriteLine(c);
        }
    }
}