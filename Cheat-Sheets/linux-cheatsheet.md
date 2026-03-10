1. grep
Search for specific text inside files.
Example: grep "password" file.txt
Example: grep -r "admin" .

2. find
Search files based on name, size, or type.
Example: find /home -name "file.txt"
Example: find / -type f -name "*.log"

3. awk
Powerful text processing tool used to extract columns or patterns.
Example: awk '{print $1}' file.txt

4. sed
Stream editor used to replace or modify text.
Example: sed 's/apple/orange/g' file.txt

5. cut
Extract specific columns from text.
Example: cut -d ":" -f1 /etc/passwd

6. sort
Sort lines of text.
Example: sort file.txt
Example: sort -r file.txt

7. uniq
Remove duplicate lines from sorted output.
Example: sort file.txt | uniq

8. wc
Count lines, words, and characters.
Example: wc -l file.txt

9. tr
Translate or delete characters.
Example: tr 'a-z' 'A-Z' < file.txt

10. xargs
Convert input into command arguments.
Example: cat file.txt | xargs rm

11. tee
Write output to both terminal and file.
Example: ls | tee output.txt

12. watch
Run a command repeatedly and show live output.
Example: watch -n 2 ls

13. alias
Create command shortcuts.
Example: alias ll="ls -la"

14. history
Show previously executed commands.
Example: history

15. chmod
Change file permissions.
Example: chmod 755 script.sh

16. chown
Change file owner.
Example: chown user:user file.txt

17. df
Show disk usage of file systems.
Example: df -h

18. du
Show disk usage of directories.
Example: du -sh *

19. tar
Archive multiple files.
Example: tar -cvf archive.tar folder/
Example: tar -xvf archive.tar

20. gzip
Compress files.
Example: gzip file.txt

21. ps
Show running processes.
Example: ps aux

22. top
Display real-time running processes.

23. kill
Terminate processes using PID.
Example: kill 1234

24. killall
Kill processes by name.
Example: killall firefox

25. netstat
Show network connections and ports.
Example: netstat -tulnp

26. ss
Modern replacement for netstat.
Example: ss -tuln

27. ping
Check network connectivity.
Example: ping google.com

28. curl
Send HTTP requests or download data.
Example: curl http://example.com

29. wget
Download files from internet.
Example: wget http://example.com/file.zip

30. strings
Extract readable text from binary files.
Example: strings binaryfile
