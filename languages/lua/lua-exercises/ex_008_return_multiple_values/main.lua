--[[
Do the following:

    1. Create a function named 'get_player_stats' that returns
       three values:
           - health
           - mana
           - stamina

    2. Store the returned values into three variables:
           local h, m, s = get_player_stats()

    3. Print the three values with a clear format.

    4. Add comments explaining that Lua functions can return multiple values without wrapping them in tables or lists.
]]


--[[
This function returns three separate values: health, mana and stamina.
Lua supports multiple return values without needing lists or tables.
]]
local get_player_stats = function()
    local health = 100
    local mana = 20
    local stamina = 10
    return health, mana, stamina
end


local h, m, s = get_player_stats()
print('Health: ' .. h)
print('Mana: ' .. m)
print('Stamina: ' .. s)