--[[
Create two variables with numbers, sum them and print the result.
]]


num_1 = 7
num_2 = 70

sum = num_1 + num_2

-- Lua denotes the string concatenation operator by " .. " (two dots). If any of its operands is a number, Lua converts that number to a string.
print(num_1 .. ' + ' .. num_2 .. ' = ' .. sum)