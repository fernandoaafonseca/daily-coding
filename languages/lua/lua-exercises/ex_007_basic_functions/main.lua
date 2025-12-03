--[[
Do the following:

    1. Create a function named "greet" that takes a single parameter "name" and prints a greeting message.

    2. Create a function named "add" that returns the sum of two numbers.
       Call it several times and print the results.

    3. Create a function named "multiply_and_print" that:
           - receives two numbers
           - multiplies them
           - prints the result
           - does NOT return anything

    4. Add comments explaining the difference between:
           - printing a value
           - returning a value

    Keep all variable names, function names and comments in English.
]]


--[[
Prints a greeting.
]]
local greet = function(name)
    print('Hello, ' .. name .. '!')
end


greet('Fernando')


--[[
Returns the sum of the two numbers.
]]
local add = function(x, y)
    -- Using locals prevents accidental global variables
    sum = x + y
    return sum
end


print(add(1, 2))
print(add(1, 2))


--[[
Prints x * y but does not return anything.
]]
multiply_and_print = function(x, y)
    result = x * y
    print(x .. ' * ' .. y .. ' = ' .. result)
end


multiply_and_print(2, 3)