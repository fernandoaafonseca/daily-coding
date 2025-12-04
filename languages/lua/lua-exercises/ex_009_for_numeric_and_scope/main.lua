--[[
Do the following:

    1. Write a numeric 'for' loop from 1 to 5 and print each number.

    2. After the loop, print 'i' and observe what happens.

    3. Add comments explaining that the loop variable exists only inside the loop block and becomes nil outside it.

    4. Use snake_case and single quotes everywhere.
]]


--[[
The loop variable 'i' exists only inside the for-loop block.
Outside of the loop, the variable 'i' is nil.
]]
for i = 1, 5 do
    print(i)
end

-- prints nil
print(i)