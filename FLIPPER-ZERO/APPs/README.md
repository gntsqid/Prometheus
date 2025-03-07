# CUSTOM APPLICATIONS
This time around I am learning just how apps on the F0 are made.\
I have a bit of embedded C under my belt and want to branch out.

## BUILD
These are steps I took from this [tutorial](https://instantiator.dev/post/flipper-zero-app-tutorial-01/).\
First:
```Bash
git clone https://github.com/flipperdevices/flipperzero-ufbt.git
```
Install the python library tool:
```Bash
python3 -m pip install --updated ufbt
```
upgrade it:
```Bash
python3 -m pip install --upgrade ufbt --break-system-packages
```
choose which firmware version to work off of:
```Bash
ufbt update --channel=release
```
Create an app in a repo of your making (give it a name):
```Bash
mkdir my_app
cd my_app
ufbt create APPID=my_app
```
Finally, build it!
```Bash
ufbt
```
> Find the *.fap* file in the *dist* directory inside the parent directory you made to hold your app code

---
## UPDATE
Anytime the F0 itself gets a firmware update, we will need to update all of our apps.\
UFBT requires we do the following:
```Bash
# Fetch new SDK API
ufbt update
```
Clean the current application directory
```Bash
ufbt clean
```
Re-compile the application
```Bash
ufbt
```
