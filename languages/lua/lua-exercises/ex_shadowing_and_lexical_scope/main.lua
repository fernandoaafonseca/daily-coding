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


-- This is a global variable (accessible everywhere)
value = 42
print(value)

do
    -- This local variable shadows the global one inside this block
    local value = 7
    print('Value inside the block: ' .. value)
end

print('Value outside the block: ' .. value)

-- A new local variable (this shadows the global, but only after this line)
local value = 'outer'

do
    -- This shadows the previous local
   local value = 'inner'
    print('Value inside the inner block: ' .. value)
end

print('Value outside the inner block: ' .. value)