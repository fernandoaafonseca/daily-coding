﻿/*
- Generated by ChatGPT

Create a program that uses a list of strings to store the names of your favorite games.
Tell the user to add more games to the list until he types "exit".
Then show all the games in an expanded format.
*/


using System;
using System.Collections.Generic;

class Program
{
    // List to store favorite games
    static List<string> favGames = new List<string>();

    static void Main(string[] args)
    {
        // Loop to keep showing the menu until the user chooses to exit
        while (true)
        {
            // Display the title of the application
            PrintTitle();
            // Display the menu options
            PrintMenuOptions();
            // Get the user's choice
            int userOption = GetUserOption();
            // Execute the chosen option
            ExecuteUserOption(userOption);
        }
    }

    /// <summary>
    /// Clears the console and displays the title for the application.
    /// </summary>
    static void PrintTitle()
    {
        Console.Clear();

        Console.WriteLine(new string('=', 19));
        Console.WriteLine("Favorite Games List");
        Console.WriteLine(new string('=', 19));
    }

    /// <summary>
    /// Displays the menu options for the user.
    /// This method will show the menu options for adding a new game,
    /// checking the list, or exiting the application.
    /// </summary>
    static void PrintMenuOptions()
    {

        Console.WriteLine("1 - Add a new game");
        Console.WriteLine("2 - Check the list");
        Console.WriteLine("3 - Exit");
        // Separator line for clarity
        Console.WriteLine(new string('=', 19));

    }

    /// <summary>
    /// Gets the user's option and ensures it is valid.
    /// </summary>
    /// <returns>
    /// An integer representing the user's choice (1, 2, or 3).
    /// </returns>
    static int GetUserOption()
    {
        while (true)
        {
            try
            {
                Console.Write("\nPlease select an option (1-3): ");
                string userInput = Console.ReadLine();

                // Try to convert the string to int
                if (int.TryParse(userInput, out int userOption))
                {
                    // Check if the number is in the desired range
                    if (userOption >= 1 && userOption <= 3)
                    {
                        // Return the valid user option
                        return userOption;
                    }
                }

                // Display error message if input is not valid
                Console.WriteLine("\n[!]");
                Console.WriteLine("Please enter a number between 1 and 3.");
                Console.WriteLine("Press any key to try again...");
                Console.ReadKey();
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occurred: " + ex.Message);
            }
        }
    }

    /// <summary>
    /// Executes the action corresponding to the user's choice.
    /// </summary>
    /// <param name="userOption">
    /// An integer representing the user's choice (1, 2, or 3).
    /// </param>
    static void ExecuteUserOption(int userOption)
    {
        switch (userOption)
        {
            case 1:
                AddNewGame();
                break;
            case 2:
                PrintList();
                break;
            // If the user chooses to exit, break the loop
            case 3:
                // Display the title
                PrintTitle();
                Console.WriteLine("[X] Exiting...");
                Console.WriteLine("\nPress any key to close the window...");
                Console.ReadKey();
                // Exit the application cleanly
                Environment.Exit(0);
                break;
        }
    }

    /// <summary>
    /// Adds a new game to the list of favorite games.
    /// </summary>
    static void AddNewGame()
    {

        // Initialize the validity flag
        bool gameNameIsValid = false;
        // Declare the variable to hold the new game name
        string newGame;

        // Loop until a valid game name is provided
        while (gameNameIsValid == false)
        {
            // Display the title before prompting for input
            PrintTitle();

            Console.Write("Enter the name of the new game: ");
            newGame = Console.ReadLine();

            // Check if the input is null or consists only of white-space characters
            if (string.IsNullOrWhiteSpace(newGame))
            {
                // Display the title before showing the error message
                PrintTitle();
                // Inform the user about the invalid input
                Console.WriteLine("[!] Game name cannot be empty. Please enter a valid name.");
                Console.WriteLine("\nPress any key to try again...");
                // Wait for user input before returning to the menu
                Console.ReadKey();
            }
            else
            {
                // Set the flag to true if the name is valid
                gameNameIsValid = true;
                // Add the valid game name to the list
                favGames.Add(newGame);
                // Confirm the addition
                Console.WriteLine($"\n[+] {newGame} added to the list.");
            }
        }
        Console.WriteLine("\nPress any key to return to the menu...");
        // Wait for user input before returning to the menu
        Console.ReadKey();
    }

    /// <summary>
    /// Displays the list of favorite games.
    /// </summary>
    static void PrintList()
    {
        // Display the title before showing the list
        PrintTitle();

        if (favGames.Count == 0)
        {
            // Display an error message if the list is empty
            Console.WriteLine("[!] The list is empty.");
            Console.WriteLine("\nPress any key to return to the menu...");
            // Wait for user input before returning to the menu
            Console.ReadKey();
        }
        else
        {
            Console.WriteLine("Your favorite games:");
            // Display the list of favorite games
            for (int i = 0; i < favGames.Count; i++)
            {
                Console.WriteLine($"- {i + 1}: {favGames[i]}");
            }
            Console.WriteLine("\nPress any key to return to the menu...");
            // Wait for user input before returning to the menu
            Console.ReadKey();
        }
    }
}