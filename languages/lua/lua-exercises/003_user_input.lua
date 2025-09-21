--[[
Ask the user to type their name and print a greeting message.
]]

-- Prompt the user for input
print('Please enter your name: ')

-- Read the input and store it in a variable
local user_name = io.read()

print('Hi, ' .. user_name .. '!')
