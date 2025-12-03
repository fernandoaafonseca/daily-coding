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


local get_player_stats = function()
    health = 100
    mana = 20
    stamina = 10
    return health, mana, stamina
end


local h, m, s = get_player_stats()
print('Health: ' .. h)
print('Mana: ' .. m)
print('Stamina: ' .. s)