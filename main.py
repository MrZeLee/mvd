#! /usr/local/bin/python

import os
import shutil
import sys
import re
import datetime
import argparse



def main(arguments, date=None, order=None, invert=None, time=None, number=None):

    # Specify the download folder path
    download_folder = '~/Downloads'

    # Get the list of files in the download folder
    download_folder = os.path.expanduser(download_folder)
    files = os.listdir(download_folder)

    func = lambda x: datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(download_folder, x))) > (datetime.datetime.now() - datetime.timedelta(minutes=time))

    def order_map_func(x):
        regex = re.match(r'^(\d{1,2})-{1}[^-].*$',x)
        if regex:
            try:
                number = int(regex.groups()[0])
                return number
            except:
                return 0
        else:
            return 0

    if order:
        files_current_directory = os.listdir(os.getcwd())
        start = max(
                    [0]+list(filter(lambda x: x == 0,
                            list(map(order_map_func,files_current_directory)))
                        )
                    ) + 1
    else:
        start = -1

    if date:
        today = datetime.datetime.now().strftime("%Y-%m-%d") + "_"
    else:
        today = ""


    # Sort the files by modification time (most recent first)
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(download_folder, x)), reverse=True)
    if number:
        sorted_files = sorted_files[:number]

    if sorted_files:
        # Get the most recent file
        if time:
            most_recent_files = list(filter(func,sorted_files))
        else:
            if number:
                most_recent_files = sorted_files
            else:
                most_recent_files = [sorted_files[0]]

        if invert:
            most_recent_files = most_recent_files[::-1]

        for most_recent_file in most_recent_files:
            before = most_recent_file
            # Construct the source and destination paths
            source_path = os.path.join(download_folder, most_recent_file)

            if len(arguments) > 0:
                arguments = '_'.join(arguments)
                most_recent_file = arguments + most_recent_file

            base_name, extension = os.path.splitext(most_recent_file)

            if order:
                regex = re.match(r'^(?:\d{1,2}-+){0,1}(.*?)(?: *\( *\d* *\) *)* *$',base_name)
            else:
                regex = re.match(r'^(.*?)(?: *\( *\d* *\) *)* *$',base_name)

            if start != -1:
                start_to_string = str(start).zfill(2) + "-"
                start += 1
            else:
                start_to_string = ""

            most_recent_file = start_to_string + today + regex.groups()[0] + extension

            destination_path = os.path.join(os.getcwd(), most_recent_file)

            # Move the file to the current folder
            shutil.move(source_path, destination_path)
            print(f"{before} -> {most_recent_file}")
    else:
        print("No files found in the download folder.")

if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Moves the last downloaded file to the current directory.')

    # Add flags or options
    parser.add_argument('-d', '--date', action='store_true', help='Add date YYYY-MM-DD to the start of the file namefile.')
    parser.add_argument('-s', '--sort', action='store_true', help="Adds NN- to the start of the namefile.")
    parser.add_argument('-i', '--invert', action='store_true', help="Inverts the order.")
    parser.add_argument('-t','--time', type=int, nargs='?',metavar="minutes", help="Matches all the files that have been downloaded in the last N minutes.")
    parser.add_argument('-n', '--number', type=int, nargs='?', metavar="N", help="Matches the N most recent files.")

    parser.add_argument('args', nargs='*', help='Description of command.')

    # Parse the command-line arguments
    args = parser.parse_args(sys.argv[1:])

    # Call the main function
    main(args.args, args.date, args.sort, args.invert, args.time, args.number)