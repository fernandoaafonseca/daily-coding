--[[
Do the following:

    1. Create a global variable named "value" and assign any number to it.
    2. Print its value.
    3. Create a local variable with the same name ("value") inside a block:

        do
            -- local value = ...
        end

       Then print both values:
           - The one inside the block
           - The one outside the block

    4. Explain in comments what "variable shadowing" means in Lua.
    5. Add an additional test by creating:

           local value = "outer"
           do
               local value = "inner"
               -- print inside the block
           end

       Then print again outside the block.
       Observe how each "value" refers to a different variable.

    6. Keep all variable names and comments in English.
]]


value = 42
print(value)


do
    local value = 7
    print('Value inside the block: ' .. value)
end

print('Value outside the block: ' .. value)


local value = 'outer'


do
   local value = 'inner'
   print(value)
end

print(value)