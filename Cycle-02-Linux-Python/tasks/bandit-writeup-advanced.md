level 10-11 : The password for the next level is stored in the file data.txt, which contains base64 encoded data

base64 -d data.txt
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr









level 11-12 : The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4


What this does
tr = translate characters

'A-Za-z'        → all letters
'N-ZA-Mn-za-m'  → letters rotated by 13

So the command converts ROT13 text back to normal text.

















level 12-13 : The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn








Steps & Commands Used

1. Create a temporary working directory

mktemp -d
cd /tmp/<temp_dir>

Used to work safely in /tmp without modifying files in the home directory.

2. Copy the given file

cp ~/data.txt .

Copied the challenge file into the temp directory.

3. Reverse the hexdump

xxd -r data.txt > data

xxd -r = reverse hex dump back to original binary data

4. Identify file type

file data

Used to detect the actual format of the file after every extraction.

5. Extract based on file type

For gzip

mv data data.gz
gunzip data.gz

For bzip2

mv data data.bz2
bunzip2 data.bz2

For tar archive

tar -xf <filename>

These commands were repeated multiple times depending on what file showed.

6. Repeat the cycle

file <new_file>

After every extraction, checked the next layer type and decompressed again.

7. Final password retrieval

cat data8

Once file data8 returned ASCII text, the file was plain text, so cat was used to read the password.

Core Logic
hexdump → restore → identify → decompress → repeat → plain text





















level 13-14 : The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.

MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS




For Bandit Level 13 → 14, the first step was performed in the existing Bandit terminal where the prompt was bandit13@bandit:~$. In this terminal, the private SSH key was displayed using the command cat sshkey.private, and the complete key content (from -----BEGIN RSA PRIVATE KEY----- to -----END RSA PRIVATE KEY-----) was copied. After this, a new local terminal was opened on the user’s own machine (for example, Kali Linux), and a new file was created using nano bandit14_key. The copied key was pasted into this file and saved. Then the file permissions were restricted using chmod 600 bandit14_key so that SSH would accept it as a valid private key. Once the permissions were set, the login to the next level was performed from the local terminal only using ssh -i bandit14_key bandit14@bandit.labs.overthewire.org -p 2220. After successful authentication, the prompt changed to bandit14@bandit:~$. Finally, the password for the next level was obtained by running cat /etc/bandit_pass/bandit14, which displayed the password for Bandit Level 14.





















level 14-15 : The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.


8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo


To successfully retrieve the password for Bandit level 15, you must submit your current level's password to a network service running on the local machine. First, ensure you are logged into the server as bandit14 and view your current password by running the command cat /etc/bandit_pass/bandit14. Once you have copied that password, open a connection to the required port using Netcat by executing nc localhost 30000, and then paste the password into the prompt to receive the new flag. Alternatively, you can complete the entire process in a single, efficient step by piping the password directly into the network connection with the command cat /etc/bandit_pass/bandit14 | nc localhost 30000.



















level 15-16 : The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.
Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.


kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx





To retrieve the flag for Bandit level 16, you must securely submit the level 15 password to a local network service that requires SSL/TLS encryption. After logging into the server as bandit15, you must bypass standard plaintext tools like Netcat and instead use the OpenSSL client to handle the required encrypted handshake. You can solve this interactively by running openssl s_client -connect localhost:30001 and pasting your current password into the prompt once the connection is established. Alternatively, you can complete the process in a single, streamlined command by piping the password directly into the service using cat /etc/bandit_pass/bandit15 | openssl s_client -quiet -connect localhost:30001, which suppresses the verbose certificate details and immediately returns the new flag.

















level 16-17 : The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----



The workflow for this level required a shift from knowing your target to finding it using nmap -p 31000-32000 -sV localhost to scan for open ports and identify their services. The primary trap laid by the challenge was the inclusion of multiple "echo" servers; if you connected to ports like 31518, they would simply repeat your password back to you instead of giving you the flag. By identifying the unique service on port 31790 that actually processed your credentials via SSL, you were rewarded with an RSA Private Key instead of a standard password. This introduced a final hurdle: SSH security policies. You had to save the key to a file and use chmod 600 to restrict its permissions, as SSH will "fail open" and reject a private key if it's accessible by other users. After bypassing a final server-side restriction on internal SSH loops by connecting directly from your Kali Linux machine using ssh -i ~/bandit17.key bandit17@bandit.labs.overthewire.org -p 2220, you successfully gained access to the next level.

Key Commands Recap
Scan: nmap -p 31000-32000 -sV localhost

Connect: openssl s_client -quiet -connect localhost:31790

Secure: chmod 600 ~/bandit17.key

Login: ssh -i ~/bandit17.key bandit17@bandit.labs.overthewire.org -p 2220





















level 17-18 : There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

x2gLTTjFwMOhQ8oWNbmN362QKxfRqGlO



To successfully retrieve the password for Bandit Level 18, you must find the only line that differs between two files in the bandit17 home directory by executing the command diff passwords.old passwords.new, which reveals the new password (x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO) indicated by the > symbol in the output. However, logging into Level 18 normally triggers a script that instantly closes your connection with a "Byebye!" message. To bypass this trap and retrieve the Level 19 flag, you must open a terminal on your local Kali machine and force SSH to execute a command immediately upon login rather than spawning an interactive shell, which is accomplished by running the command ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme".
















level 18-19 : The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8



To retrieve the password for Bandit Level 19, you must bypass a "Byebye!" trap that immediately terminates any interactive SSH session upon login to bandit18. By executing the command ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme" from your local Kali terminal and entering the Level 18 password, you force the server to run a single remote command and display the contents of the flag file directly to your screen before the forced-logout script can trigger. This specific workflow successfully bypasses the shell initialization process, resulting in the acquisition of the next flag: cGwPMaKXVwDUNgPAVJbWYuGHVn9zl3j8.

















level 19-20 : To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

./bandit20-do cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO







To solve Bandit Level 20, you must utilize a setuid binary named bandit20-do which grants temporary bandit20 privileges to any command it executes. By running ls -l, you can identify the unique s permission bit that allows this elevation. Since you cannot directly access the password file as bandit19, you must use the binary to run a read command on your behalf by executing ./bandit20-do cat /etc/bandit_pass/bandit20. This bypasses standard permission checks, revealing the next flag: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO.
