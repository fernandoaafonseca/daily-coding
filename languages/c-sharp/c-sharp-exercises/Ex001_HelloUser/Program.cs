﻿/*
* - Create a new Console project:
* dotnet new console -o NewProjectFolder
*
* - To run and debug the project:
* Ctrl + Shift + P -> .NET: Generate Assets for Build and Debug
*
* - Compile the code:
* dotnet build
*
* - Compile the code in a new folder:
* dotnet build -c NewFolderName
*
* - Inside the folder, run the project:
* dotnet run
*/

namespace HelloUser;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter your name: ");
        string userName = Console.ReadLine();

        // Remove any leading or trailing spaces
        userName = userName.Trim();

        Console.WriteLine($"Hello, {userName}!");

        // Wait for a key pressing to close the window
        Console.WriteLine("Press any key to close the window.");
        Console.ReadKey();
    }
}
