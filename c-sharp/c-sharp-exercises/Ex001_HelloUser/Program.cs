/*
* - Create a new Console project:
* dotnet console -o NewProjectFolder
*
* - Inside the folder, run the project:
* dotnet run
*
* - To run and debug the project:
* Ctrl + Shift + P -> .NET: Generate Assets for Build and Debug
*
* - Compile the code:
* dotnet build
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
