    #ensure fiddler doesn't defalt to certmakerEnroll
    keyVal = r'Software\Microsoft\Fiddler2\Prefs\.default'
    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)

    SetValueEx(key, "fiddler.certmaker.prefercertenroll", 0, REG_SZ, "False")
    CloseKey(key)
