IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Returns the index where the first difference between line1 and line2 occurs.
    Returns IDENTICAL if the two lines are the same.
    """
    min_length = min(len(line1), len(line2))
    for idx in range(min_length):
        if line1[idx] != line2[idx]:
            return idx
    if len(line1) != len(line2):
        return min_length
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Returns a three-line formatted string showing the location of the first difference.
    """
    if '\n' in line1 or '\r' in line1 or '\n' in line2 or '\r' in line2:
        return ''
    if idx < 0 or idx > min(len(line1), len(line2)):
        return ''
    return f"{line1}\n{'=' * idx}^\n{line2}\n"


def multiline_diff(lines1, lines2):
    """
    Returns a tuple (line number, index) of the first difference between lines1 and lines2.
    Returns (IDENTICAL, IDENTICAL) if no difference is found.
    """
    min_lines = min(len(lines1), len(lines2))
    for line_num in range(min_lines):
        diff_idx = singleline_diff(lines1[line_num], lines2[line_num])
        if diff_idx != IDENTICAL:
            return (line_num, diff_idx)
    if len(lines1) != len(lines2):
        return (min_lines, 0)
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Reads a file and returns a list of lines without newline or return characters.
    """
    with open(filename, 'r') as f:
        return [line.rstrip('\n').rstrip('\r') for line in f]


def file_diff_format(filename1, filename2):
    """
    Returns a four-line string showing the location of the first difference between files.
    If files are identical, returns "No differences\n".
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    line_num, idx = multiline_diff(lines1, lines2)
    
    if line_num == IDENTICAL:
        return "No differences\n"
    
    line1 = lines1[line_num] if line_num < len(lines1) else ''
    line2 = lines2[line_num] if line_num < len(lines2) else ''
    
    diff_format = singleline_diff_format(line1, line2, idx)
    return f"Line {line_num}:\n{diff_format}"

if __name__ == "__main__":
    print(file_diff_format("C:/Users/hi/OneDrive/Attachments/Desktop/isp_diff_files/file1.txt",
                           "C:/Users/hi/OneDrive/Attachments/Desktop/isp_diff_files/file2.txt"))

'''
use the file path as directed in your system
'''
