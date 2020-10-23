# Fiddler
## Issue encountered with latest Fiddler 4 
-Fiddler 4 by default uses certmakerenroll to generate certificates even on windows 
-when using fiddler in a python program on windows you l found myself having problems because I would generate the Root trust certificate using makecert.exe for windows
-to fix this situation l just added a simple code that actually goes into the registry and changes fiddler's default certificate generator from certmakerenroll to makecert.exe
