--[[
Do the following:

    1. Create two global variables (without using "local") and print their sum.
    2. Create two local variables (using "local") and print their sum.
    3. Inside an explicit block:

        do
            -- your code
        end

       Create local variables and try to access them after the block — and observe the error.
    4. Name everything in English:
        global_a
        global_b
        local_a
        local_b
        etc.
    5. Add clear and neatly formatted comments.
]]


-- Global variables are created by simply assigning to a name without "local".
-- They are accessible anywhere in the program.
global_a = 1
global_b = 2
print(global_a + global_b)

-- Local variables exist only inside the current block or scope.
local local_a = 3
local local_b = 4
print(local_a + local_b)


-- Creating a new local variable inside an explicit block
do
	local local_x = 5
    print(local_x)  -- This prints 5, because local_x exists inside this block
end

-- This prints nil because local_x only exists inside the block above.
print(local_x)