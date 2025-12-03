--[[
Do the following:

    1. Create a function named "create_counter" that:
           - declares a local variable "count" initialized to 0
           - returns an inner function that increments "count" and prints its value

    2. Call "create_counter" and store the result in a variable named "counter_a".
       Call "counter_a" several times and observe how the value increases.

    3. Create a second counter named "counter_b" using the same function.
       Call "counter_b" several times and observe that it has its own independent state.

    4. Add comments explaining:
           - what an upvalue is
           - how closures allow a function to remember variables
           - why counter_a and counter_b do not interfere with each other
]]


--[[
This function returns a closure that increments the internal 'count' variable on every call. The variable 'count' becomes an upvalue, which means the inner function keeps a reference to it even after create_counter() has finished running.
]]
local create_counter = function()
    -- This becomes an upvalue captured by the inner function
    local count = 0

    return function()
        count = count + 1
        print('Inner function count: ' .. count)
    -- Closes the inner function
    end
-- Closes the outer function
end


local counter_a = create_counter()
counter_a()
counter_a()
counter_a()

local counter_b = create_counter()
counter_b()
counter_b()
counter_b()