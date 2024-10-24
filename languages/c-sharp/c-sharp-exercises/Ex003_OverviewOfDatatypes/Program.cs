using System.Globalization;

CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;


/*
*  REFERENCE TYPES
*/
// The reference types are: "object", "string" and "dynamic"
string myName = "Fernando";


/*
*  VALUE TYPES
*/

Console.WriteLine(new string('=', 40));
Console.WriteLine("OVERVIEW OF DATATYPES");
// "byte" is the only type that is "unsigned (u)" by default
// The default for other types is "signed (s)"
// sbyte -> -128 to 127
// byte -> 0 to 255
sbyte signedByte = -128;
byte unsignedByte = 255;
Console.WriteLine($"sbyte: {signedByte}");
Console.WriteLine($"byte: {unsignedByte}");
Console.WriteLine(new string('=', 40));

// short -> -32,768 to 32,767
// ushort -> 0 to 65,535
short signedShort = -32768;
ushort unsignedShort = 65535;
Console.WriteLine($"short: {signedShort}");
Console.WriteLine($"ushort: {unsignedShort}");
Console.WriteLine(new string('=', 40));

// int -> -2,147,483,648 to 2,147,483,647
// uint -> 0 to 4,294,967,295
int signedInt = -2147483648;
uint unsignedInt = 4294967295;
Console.WriteLine($"int: {signedInt}");
Console.WriteLine($"uint: {unsignedInt}");
Console.WriteLine(new string('=', 40));

// long -> -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
// ulong -> 0 to 18,446,744,073,709,551,615
long signedLong = -9223372036854775808;
ulong unsignedLong = 18446744073709551615;
Console.WriteLine($"long: {signedLong}");
Console.WriteLine($"ulong: {unsignedLong}");
Console.WriteLine(new string('=', 40));

// float -> ±1.5 x 10^-45 to ±3.4 x 10^38 (~6-9 digits of precision, 4 bytes)
float floatPi = 3.141592f;
Console.WriteLine($"float: {floatPi}");
Console.WriteLine(new string('=', 40));

// double -> ±5.0 x 10^-324 to ±1.7 x 10^308 (~15-17 digits of precision, 8 bytes)
double doublePi = 3.141592653589793;
Console.WriteLine($"double: {doublePi}");
Console.WriteLine(new string('=', 40));

// decimal -> ±1.0 x 10^-28 to ±7.9 x 10^28 (28-29 digits of precision, 16 bytes)
decimal decimalPi = 3.1415926535897932384626433832m;
Console.WriteLine($"decimal: {decimalPi}");
Console.WriteLine(new string('=', 40));