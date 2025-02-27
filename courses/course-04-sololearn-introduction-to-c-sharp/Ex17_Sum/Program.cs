/*
Sum

Your math teacher asked you to calculate the sum of the numbers 1 to N, where N is a given number.
The given program takes a number as input.

Task
Write code to output the sum of the numbers from 1 to that number, inclusive.

Input Example⬅️: 10
Output Example➡️: 55

The sum of the numbers 1 to 10 is 55.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        int num = Convert.ToInt32(Console.ReadLine());

        //your code goes here
        int sum = Sum(num);
        Console.WriteLine(sum);

        RunSimpleTests();
    }

    static int Sum(int num)
    {
        int i = 1;
        int sum = 0;

        while (i <= num)
        {
            sum += i;
            i++;
        }
        return sum;
    }

    static void RunSimpleTests()
    {
        int num;
        int sum;
        int expectedResult;

        num = 4;
        sum = Sum(num);
        expectedResult = 10;
        Console.WriteLine(sum == expectedResult);
        
        num = 42;
        sum = Sum(num);
        expectedResult = 903;
        Console.WriteLine(sum == expectedResult);
        
        num = 236;
        sum = Sum(num);
        expectedResult = 27966;
        Console.WriteLine(sum == expectedResult);
        
        num = 100;
        sum = Sum(num);
        expectedResult = 5050;
        Console.WriteLine(sum == expectedResult);
    }
}