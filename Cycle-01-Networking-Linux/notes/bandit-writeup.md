level 0 : The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

ssh bandit0@bandit.labs.overthewire.org -p 2220







level 0-1 :The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If








level 1-2 : The password for the next level is stored in a file called - located in the home directory

cat ./-
263JGJPfgU6LtdEvgfWU1XP5yac29mFx









level 2-3 : The password for the next level is stored in a file called --spaces in this filename-- located in the home directory

cat -- "--spaces in this filename--" 
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx









level 3-4 : The password for the next level is stored in a hidden file in the inhere directory.

cat -- "...Hiding-From-You"
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ












level 4-5 : The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: OpenPGP Public Key
./-file02: OpenPGP Public Key
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat -- "-file07"
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw













level 5-6 : The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
human-readable
1033 bytes in size
not executable

find . -type f -size 1033c ! -executable
./inhere/maybehere07/.file2
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG




find / — Search from the root of the filesystem
/ means the root directory of the entire system.
find / searches the whole filesystem.
------------------------------------------------------------------------
find . — Search from the current directory
. means the current directory.
find . searches only inside the directory you are currently in and its subdirectories.







level 6-7 : The password for the next level is stored somewhere on the server and has all of the following properties:
owned by user bandit7
owned by group bandit6
33 bytes in size

find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
cat /var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj




find / → search from the root of the filesystem
-type f → only files
-user bandit7 → file owned by user bandit7
-group bandit6 → file owned by group bandit6
-size 33c → file size exactly 33 bytes
2>/dev/null → hides permission denied errors













level 7-8 : The password for the next level is stored in the file data.txt next to the word millionth

cat data.txt | grep millionth  / grep millionth data.txt
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

now , grep prints the whole line in which the the keyword is present 
but if we need to see the line next to the keyword line , then the format would had been : 
grep -A 1 millionth data.txt















level 8-9 : The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

sort data.txt | uniq -u 
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM



1️⃣ sort data.txt
Sorts all lines alphabetically.
This is important because uniq only works on adjacent duplicate lines.
2️⃣ | (pipe)
Sends the sorted output to the next command.
3️⃣ uniq -u
uniq removes duplicates.
-u → prints only lines that appear exactly once.




















level 9-10 : he password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

strings data.txt | grep = 
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey



strings extracts human-readable text sequences from binary or non-text files.
So it scans a file and prints continuous printable characters.













level 10-11 : The password for the next level is stored in the file data.txt, which contains base64 encoded data

base64 -d data.txt
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr



