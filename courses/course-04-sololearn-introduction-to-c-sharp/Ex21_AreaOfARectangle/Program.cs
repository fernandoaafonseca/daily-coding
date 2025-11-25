/*
Area Of a Rectangle

We need to calculate the area of a given rectangle.
The given program takes the width and length as input.

Task
Fix and complete the Area method, which takes the length and width as arguments, to calculate and return the area.
Then call the method for the given inputs.

Example Input
7
4
Example Output
28

To find the area of a rectangle, multiply the length by the width.
*/

using System;

public class Program
{
    static void Main(string[] args)
    {
        int width = Convert.ToInt32(Console.ReadLine());
        int length = Convert.ToInt32(Console.ReadLine());

        //output the result
        int area = CalculateArea(width, length);
        Console.WriteLine(area);

        RunSimpleTests();
    }


    //fix the method
    static int CalculateArea(int width, int height)
    {
        int area = width * height;
        return area;
    }

    static void RunSimpleTests()
    {
        int width, height, area, expectedResult;

        width = 42;
        height = 35;
        expectedResult = 1470;
        area = CalculateArea(width, height);
        Console.WriteLine(area == expectedResult);

        width = 1;
        height = 42;
        expectedResult = 42;
        area = CalculateArea(width, height);
        Console.WriteLine(area == expectedResult);
        
        width = 100;
        height = 7;
        expectedResult = 700;
        area = CalculateArea(width, height);
        Console.WriteLine(area == expectedResult);
    }
}