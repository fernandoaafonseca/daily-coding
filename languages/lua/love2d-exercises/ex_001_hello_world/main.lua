--[[
--> Running Games
 
LÖVE can load a game in two ways:
 
From a folder that contains a main.lua file.
From a .love file that has a main.lua file in the top-most directory level (aka root)
For creating .love files see Game Distribution.
 
 
- Linux
On Linux, you can use one of these command lines:
 
love /home/path/to/gamedir/
love /home/path/to/packagedgame.love
 
If you installed LÖVE system-wide, you can double click on .love files in your file manager as well.
 
 
- Windows
ZeroBrane Studio, Sublime Text, Notepad++, and SciTE allow you to launch the game from within their code editors.
Otherwise, the easiest way to run the game is to drag the folder onto either love.exe or a shortcut to love.exe. Remember to drag the folder containing main.lua, and not main.lua itself.
 
You can also launch the game from the command line:
 
"C:\Program Files\LOVE\love.exe" "C:\games\mygame"
"C:\Program Files\LOVE\love.exe" "C:\games\packagedgame.love"
 
You can create a shortcut to do this; simply make a shortcut to love.exe, right-click on it and select "Properties", and then put the command line you want in the "Target" box for the shortcut.
On Windows, there is a special command-line option which will attach a console to the window, allowing you to see the result of print calls (equivalent to setting t.console=true in conf.lua or running lovec.exe (since 0.10.2)):
 
"C:\Program Files\LOVE\love.exe" --console
 
 
Source:
https://www.love2d.org/wiki/Getting_Started
]]


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


function love.load()
    love.window.setMode(WINDOW_WIDTH, WINDOW_HEIGHT, {
        resizable = false,
        vsync = true,
        fullscreen = false
    })
end


function love.draw()
    love.graphics.printf("Hello World", 0, WINDOW_HEIGHT / 2 - 6, WINDOW_WIDTH, 'center')
end
