# zoom-autologin
A python application to eradicate the hassle of logging in the meeting details and meeting settings on zoom every single time by automating the process.

For this to work on your system you will have to modify the argument (the address of the zoom executable file) written on line number 11 which will look like this:
    subprocess.call(r"C:\Users\nehac\AppData\Roaming\Zoom\bin\Zoom.exe")
Here instead of this: "C:\Users\nehac\AppData\Roaming\Zoom\bin\Zoom.exe" you will have to copy and paste the address of the zoom executable on your system.
