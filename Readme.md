
# WebAutoLogin
A tool to automatically login to the SuperLoop Internet Gateway, using selenium webdriver and chromedriver.
## Windows Installation

1.  clone the repo:

		git clone https://github.com/Eviper01/WebAutoLogin

	 or
	 Download the repository as Zip.
2. Copy the contents of master into the startup folder located by pressing  <kbd>Win</kbd>+<kbd>R</kbd> and then type:

		shell:startup

3. Edit details.config
	replace \<YourUserName> with your username and replace \<YourPassword> with your password. For example:

        User: Joe.Blogs.threesome
        Password: abcd1234

4. Install chromewebdriver and add to the system path (also install google chrome if you havent already. It can be downloaded from https://chromedriver.chromium.org/downloads.

	To do this:
	run from an admin command prompt

		C:
		cd \
		mkdir bin
		setx /M path "%PATH%;C:\bin"
		cd bin
		explorer  .
and copy chromedriver.exe into the file that opens

Otherwise modify it from the GUI if thats what you want to do

5. run 	

		pip3 install selenium
	If it fails make sure python3 is installed and then try again.
6. That's it, next time you login your system should log you in after about 5 to 10 seconds.
## Other Systems
1.  clone the repo:

		git clone https://github.com/Eviper01/WebAutoLogin

	 or
	 Download the repository as Zip.
2. Edit details.config
	replace \<YourUserName> with your username and replace \<YourPassword> with your password.
3. Install chromewebdriver and add to the system path (also install google chrome if you havent already. It can be downloaded from https://chromedriver.chromium.org/downloads.
4. Using whatever method for your system ensure that WebAutoLogin.py is executed at startup
4. run 	

		pip3 install selenium
	If it fails make sure python3 is installed and then try again.
5. That's it, next time you login your system should log you in after about 5 to 10 seconds.
