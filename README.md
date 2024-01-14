# mvd
Command to move files from Download folder to current directory

```
> mvd -h
usage: mvd [-h] [-d] [-s] [-i] [-t [minutes]] [-n [N]] [args ...]

Moves the last downloaded file to the current directory.

positional arguments:
  args                  Description of command.

options:
  -h, --help            show this help message and exit
  -d, --date            Add date YYYY-MM-DD to the start of the file namefile.
  -s, --sort            Adds NN- to the start of the namefile.
  -i, --invert          Inverts the order.
  -t [minutes], --time [minutes]
                        Matches all the files that have been downloaded in the last N minutes.
  -n [N], --number [N]  Matches the N most recent files.
  ```

## Info

To add the command to work with your terminal just added to your PATH or create a link like in this example:
```
ln -s mvd/main.py /usr/local/bin/mvd
```

