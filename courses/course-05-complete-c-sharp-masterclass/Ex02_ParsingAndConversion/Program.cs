using System.Globalization;

CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;


/*
In C#, the main difference between conversion and parsing is that conversion can work with multiple types, while parsing is used to convert a string to a specific type
*/


// IMPLICIT CONVERSION
/*
Implicit conversion occurs when the conversion is automatically performed by the compiler 
because the conversion is safe and there is no risk of data loss. 
For example, converting an int to a long or double is safe because both can represent larger ranges of values.
*/
Console.WriteLine(new string('=', 85));
Console.WriteLine("IMPLICIT CONVERSION");
Console.WriteLine(new string('=', 85));

int myInt = 42;
long myLong = myInt;
Console.WriteLine($"- The 'int' value '{myInt}' converted to 'long' is '{myLong}'.");

Console.WriteLine(new string('-', 85));
double myDouble = myInt;
Console.WriteLine($"- The 'int' value '{myInt}' converted to 'double' is '{myDouble}'.");

Console.WriteLine();


// EXPLICIT CONVERSION (CASTING)
/*
Explicit conversion, or casting, is required when there is a possibility of data loss or when 
converting from a larger data type to a smaller one. 
For instance, converting a long to an int may lead to data loss if the long value exceeds the range of an int.
*/
Console.WriteLine(new string('=', 85));
Console.WriteLine("EXPLICIT CONVERSION (CASTING)");
Console.WriteLine(new string('=', 85));

long myLong2 = 12345678987654321;
// Potential data loss warning
int myInt2 = (int)myLong2;
Console.WriteLine($"- The 'long' value '{myLong2}' converted to 'int' is '{myInt2}'.");

Console.WriteLine(new string('-', 85));
float myFloat = 42.0f;
// Casting from float to int may also lose precision
int myInt3 = (int)myFloat;
Console.WriteLine($"- The 'float' value '{myFloat:F1}' converted to 'int' is '{myInt3}'.");

Console.WriteLine();


// STRING CONVERSION AND PARSING
// CONVERSION
/*
Accepts null as input and will return 0 in this case.
Can convert other data types to int, such as float, double, etc.
*/
Console.WriteLine(new string('=', 85));
Console.WriteLine("STRING CONVERSION");
Console.WriteLine(new string('=', 85));

string myStringNumber1 = "42";
int myIntNumber1 = Convert.ToInt32(myStringNumber1);
Console.WriteLine($"- The 'string' value '{myStringNumber1}' converted to 'int' is '{myIntNumber1}'.");

Console.WriteLine();


// PARSING
/*
Throws an exception if the string is null or cannot be converted (e.g., if it contains non-numeric characters).
It is more appropriate when you are sure that the string is not null and is a valid number.
*/
Console.WriteLine(new string('=', 85));
Console.WriteLine("STRING PARSING");
Console.WriteLine(new string('=', 85));

string myStringNumber2 = "42";
int myIntNumber2 = int.Parse(myStringNumber2);
Console.WriteLine($"- The 'string' value '{myStringNumber2}' parsed to 'int' is '{myIntNumber2}'.");

Console.WriteLine();


// TRY-PARSING
/*
TryParse attempts to convert a string to a number without throwing an exception if it fails.
It returns a boolean indicating whether the conversion was successful and outputs the result.
This is useful when you cannot guarantee that the string is a valid number.
*/
Console.WriteLine(new string('=', 85));
Console.WriteLine("STRING TRY-PARSING");
Console.WriteLine(new string('=', 85));

// Parse the string to a boolean
string myStringBool = "true";
bool myBool = bool.TryParse(myStringBool, out myBool);
Console.WriteLine($"- The 'string' value '{myStringBool}' try-parsed to 'bool' is '{myBool}'.");

Console.WriteLine(new string('-', 85));
string myStringNumber3 = "42";
int myIntNumber3;
bool success = int.TryParse(myStringNumber3, out myIntNumber3);
Console.WriteLine($"- The 'string' value '{myStringNumber3}' try-parsed to 'int' is '{myIntNumber3}'.");

// Check success for parsing
if (success)
{
    // Parsing was successful, and myIntNumber3 contains the converted value
    Console.WriteLine("The parsing was successful.");
}
else
{
    // Parsing failed; handle the error accordingly
    Console.WriteLine("Parsing failed; the string could not be converted to an int.");
}

Console.WriteLine(new string('-', 85));
string myStringNumber4 = "forty-two";
int myIntNumber4;
bool success2 = int.TryParse(myStringNumber4, out myIntNumber4);
Console.WriteLine($"- The 'string' value '{myStringNumber4}' try-parsed to 'int' is '{myIntNumber4}'.");

// Check success for parsing
if (success2)
{
    // Parsing was successful, and myIntNumber4 contains the converted value
    Console.WriteLine("The parsing was successful.");
}
else
{
    // Parsing failed; handle the error accordingly
    Console.WriteLine($"Parsing failed; the 'string' value '{myStringNumber4}' could not be converted to an 'int'.");
    // Display the value of myIntNumber4 to clarify
    Console.WriteLine($"The value of the try-parsed 'int' is '{myIntNumber4}' (default value).");
}

Console.WriteLine(new string('=', 85));