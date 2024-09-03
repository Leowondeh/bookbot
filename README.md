# Bookbot!
   Bookbot can read any text given as input and output statistics of said text, like number of words or characters.

# Usage
   Bookbot requires a [Python](https://www.python.org/) install.
   
   Run Bookbot using `python`/`py`/`python3` `main.py` (depending on your Python install) in a command line. It accepts any absolute or relative path from keyboard input.

   Available commands are: `exit`/`quit`/`q`/`x` and `options`/`opt`.

   Options include saving to a report.txt file (the file gets overwritten!) and exiting after a set delay upon completion. (more soon)

# Example result
   Here's an example result using [Frankenstein](https://en.wikipedia.org/wiki/Frankenstein) ([text source](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt)) as the input text:

```
======== REPORT for books/frankenstein.txt ========

    * Word Count: 77986

    * Character counts:
       - e was found 46043 times
       - t was found 30365 times
       - a was found 26743 times
       - o was found 25225 times
       - i was found 24613 times
       - n was found 24367 times
       - s was found 21155 times
       - r was found 20818 times
       - h was found 19725 times
       - d was found 16863 times
       - l was found 12739 times
       - m was found 10604 times
       - u was found 10407 times
       - c was found 9243 times
       - f was found 8731 times
       - y was found 7914 times
       - w was found 7638 times
       - p was found 6121 times
       - g was found 5974 times
       - b was found 5026 times
       - v was found 3833 times
       - k was found 1755 times
       - x was found 677 times
       - j was found 504 times
       - q was found 324 times
       - z was found 243 times
==================================================
   ```
# To-do list
   - [x] Add options
   - [x] Add CLI interface
   - [ ] Modify saving to allow old ones to persist
