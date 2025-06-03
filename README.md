# 🧮 File Difference Detector

This Python program compares the contents of two text files **line by line** and **character by character** to find the **first difference** between them. It then presents this difference in a clean, human-readable format. This is particularly useful for debugging text files, comparing logs, or evaluating student submissions in educational environments.

---
## Project description

The project consists of multiple problems. Each problem will utilize functions you wrote for the previous problems. You can also download all of the files used when testing your code as a zip file.

### Problem 1: Finding the first difference between two lines
First, you will write a function called singleline_diff that takes two single line strings. You may assume that both strings are always a single line and do not contain any newline characters. The function should return the index of the first character that differs between the two lines.  If the lines are the same, the function should return the constant IDENTICAL, which is already defined to be −1 in the provided template file.

If the lines are different lengths, but the entire shorter line matches the beginning of the longer line, then the first difference is located at the index that is one past the last character in the shorter line.  In other words, no character after the end of the shorter line is defined to be different than whatever character exists in the longer line at that location.

### Problem 2: Presenting the differences between two lines in a nicely formatted way
Next, you will write a function called singleline_diff_format that takes two single line strings and the index of the first difference and will generate a formatted string that will allow a user to clearly see where the first difference between two lines is located. A user is likely going to want to see where the difference is in the context of the lines, not just see a number. Your function will return a three line string that looks as follows:

abcd
==^
abef

The format of these three lines is:
1. The complete first line.
2. A separator line that consists of repeated equal signs ("=") up until the first difference. A "^" symbol indicates the position of the first difference.
3. The complete second line.

If either line contains a newline or carriage return character ("\n" or "\r") then the function returns an empty string (since the lines are not single lines and the output format will not make sense to a person reading it).

If the index is not a valid index that could indicate the position of the first difference of the two input lines, the function should also return an empty string (again because the output would not make sense otherwise).  It must therefore be between 0 and the length of the shorter line. Note that you do not need to check whether the index actually identifies the correct location of the first difference, as that should have been computed correctly prior to calling this function.

### Problem 3: Finding the first difference across multiple lines
Next, you will write a function called multiline_diff that takes two lists of single line strings. You may assume that the strings within the lists are all single lines. The function returns a tuple that indicates the line and index within that line where the first difference between the two lists occurs.  If the contents of the two lists are the same, the function should return the tuple (IDENTICAL, IDENTICAL)  (Recall that the constant IDENTICAL is already defined to be −1 in the provided template file.)

The definition of whether two lines are the same or different and the resulting index for location of a difference is the same as it was for 
singleline_diff.

The line on which the first difference occurs should be the index into the input lists that correspond to that line. If the input lists are different lengths, but the entire shorter list matches the beginning of the longer list, the first difference is located at the line that is one past the last line in the shorter list at index 0.  In other words, no character on the line after the end of the shorter list is defined to be different than whatever character exists on that line in the longer list.

### Problem 4: Getting lines from a file
Next, you will write a function called get_file_lines that takes a filename as input. You may assume that the input names a file that exists and is readable. The function returns a list of single line strings, where each element of the list is one line from the file. The strings within the returned list should not contain any newline or carriage return ("\n" or "\r") characters.

### Problem 5: Finding and formatting the first difference between two files
Finally, you will write a function called file_diff_format that takes two filenames as input. You may assume that the inputs name files that exist and are readable. The function returns a formatted string that will allow a user to clearly see where the first difference between two files is located. Your function will return a four line string that looks as follows:

Line 3:
abcd
==^
abef

The format of these four lines is:
1. A line that indicates which line the first difference occurs on (Line XXX:) where "XXX" is the line number (starting from 0).
2. The complete line XXX from the first file
3.A separator line that consists of repeated equal signs ("=") up until the first difference. A "^" symbol indicates the position of the first difference.
4. The complete line XXX from the second file.

The format of the second through fourth lines should be as they are defined for 
singleline_diff_format. The location of the first difference between the files should be defined in the same way that it was for 
multiline_diff.

If the two files are identical, the function should instead return the string "No differences\n".


## 🔍 Features

- Compares two files line-by-line
- Detects the **first mismatch** (line number and character index)
- Presents a 4-line formatted difference report
- Handles edge cases like:
  - One file being longer than the other
  - Empty files
  - Special characters and whitespace
- Returns `"No differences\n"` if files are identical

---

