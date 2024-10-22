// See https://aka.ms/new-console-template for more information
Console.Write("Enter the first whole number: ");
int userInputNum1 = int.Parse(Console.ReadLine());

Console.Write("Enter the second whole number: ");
int userInputNum2 = int.Parse(Console.ReadLine());

int sum = userInputNum1 + userInputNum2;

Console.WriteLine($"The sum of {userInputNum1} + {userInputNum2} = {sum}.");