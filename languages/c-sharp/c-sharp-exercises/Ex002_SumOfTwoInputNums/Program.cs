using System.Globalization;

// Set the culture to en-US, which uses a period as the decimal separator
CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;

Console.Write("Enter the first number: ");
float userInputNum1 = float.Parse(Console.ReadLine());

Console.Write("Enter the second number: ");
float userInputNum2 = float.Parse(Console.ReadLine());

float sum = userInputNum1 + userInputNum2;
// Round the result to 2 decimal places
sum = MathF.Round(sum, 2);

Console.WriteLine($"The sum of {userInputNum1} + {userInputNum2} = {sum}.");