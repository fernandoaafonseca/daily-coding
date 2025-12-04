--[[
Do the following:

    1. Create a function named 'square' and store it in a variable.

    2. Then assign the same function to a second variable named 'square_copy'.

    3. Call both variables and show that they behave identically.

    4. Add a comment explaining that in Lua, functions are values just like numbers or strings, and can be stored in variables or passed around freely.
]]

--[[
Functions in Lua are values. They can be stored in variables,
copied, and passed around just like numbers or strings.
]]

square = function(n)
    return n * n
end


square_copy = square

print(square(4))
print(square_copy(4))