using System;

namespace HelloUser
{
    class Program
    {
        static void Main()
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
}
