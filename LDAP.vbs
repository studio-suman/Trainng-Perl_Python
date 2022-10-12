set objSysInfo = CreateObject("ADSystemInfo")
set objUser = GetObject("LDAP://" & objSysInfo.UserName)
wscript.echo "DN: " & objUser.commonName