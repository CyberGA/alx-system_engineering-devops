# DEVOPS
## Shell commands
- pwd: prints the current working directory
- ls: list content of a directory
- ls -l: Display current directory contents in a long format
- ls -la: Display contents both with hidden files
- ls -lna: Display contents both with hidden files with user and group IDs
- ln -s <dir> <link> - create a symbolic link
- cp -un `file` -  copy only file that does not exist
- [[:upper:]] - uppercase
- mkdir -p `directory/directory1/directory2` - create a directory with trailing slash
- flag -p - to show directories with a slash
- flag -a - to display hidden files
- flag -m - to display files with a comma
- flag -v - to sort files

### Creating a magic file
- first, create the magic file
````bash
<offset> <datatype> <regex> <filename> data
# replace <offset> - number
# replace <datatype> - can be string, ling, double, etc.
# replace <regex> - expression to match
# replace <filename>
!:mime filename
# create a mime(Multipurpose Internet Mail Extensions)
````
- Second, compile the file
```bash
file -C -m <filename.mgc>
````

### Shell Permisssions
- su <user> - Change user
- groups - display the groups the current user is part of
