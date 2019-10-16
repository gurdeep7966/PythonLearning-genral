import wmi

c = wmi.WMI()
#print (c.Win32_OperatingSystem)
for os in c.Win32_OperatingSystem():
  print (os)
