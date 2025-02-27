/*
Factorial

The factorial of a number N is equal to 1 * 2 * 3 * ... * N
For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.
The given program takes a number from the input.

Task
Create a program to calculate and output the factorial of that input number.
Use a for loop to make the calculation, and start the loop from the number 1.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        int num = Convert.ToInt32(Console.ReadLine());

        //your code goes here
        int factorial = CalcFactorial(num);
        Console.WriteLine(factorial);

        RunSimpleTests();
        
    }

    static int CalcFactorial(int num)
    {
        int factorial = 1;
        for (int i = num; i > 0; i--)
        {
            factorial *= i;
        }
        return factorial;
    }

    static void RunSimpleTests()
    {
        int num;
        int factorial;
        int expectedResult;

        num = 10;
        factorial = CalcFactorial(num);
        expectedResult = 3628800;
        Console.WriteLine(factorial == expectedResult);
        
        num = 8;
        factorial = CalcFactorial(num);
        expectedResult = 40320;
        Console.WriteLine(factorial == expectedResult);
        
        num = 2;
        factorial = CalcFactorial(num);
        expectedResult = 2;
        Console.WriteLine(factorial == expectedResult);
        
        num = 12;
        factorial = CalcFactorial(num);
        expectedResult = 479001600;
        Console.WriteLine(factorial == expectedResult);
        
        num = 4;
        factorial = CalcFactorial(num);
        expectedResult = 24;
        Console.WriteLine(factorial == expectedResult);
    }
}