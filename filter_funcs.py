from math import floor
from re import finditer
def string_indenter(string, length=50, paragraph_size=0,space_size=1):
    """
    About:
    Shapes a body of text to match within 80%+ of the
    given length. 
    Adds line breaks after every nth time the line length in a string
    has been met,
    provided that part of the string is a space.
    """
    string_length = len(string)
    ratio = string_length // length
    index_jump = floor(0.8 * length) 
    composite_string = ''
    nth_snippet = ''
    index_start = 0
    index_end_non_inclusive = 0
    DEFINITE_END = string_length - 1
    rotate = True
    space = True
    while rotate is True:
        for turn, rotation in enumerate(range(ratio)):
            index_start = index_end_non_inclusive
            index_end_non_inclusive += index_jump
            while string[index_end_non_inclusive] != " ":
                index_end_non_inclusive += 1
            if string[index_end_non_inclusive] == " ":
                nth_snippet = string[index_start:index_end_non_inclusive + 1] + "\n" 
            try:
                if (turn + 1) % paragraph_size == 0:
                    space = True
            except ZeroDivisionError:
                pass
            if space == True and "\n" not in nth_snippet[0:-1]:
                nth_snippet += ("\n") * space_size
                space = False
            composite_string += nth_snippet.lstrip()  # have to remove the + 1 counted in the above, chef's kiss  # lstrip()
        #remainder = (DEFINITE_END - index_end_non_inclusive) 
        nth_snippet = string[index_end_non_inclusive:DEFINITE_END + 1]
        #print(f"nth snippet: {nth_snippet} index end: {index_end_non_inclusive} str length: {string_length}  def end: {DEFINITE_END}") # debug
        composite_string += nth_snippet.lstrip()
        rotate = False
        return composite_string
    # TODO
    # the function has to account for spaces




def paragraph_maker(string, paragraph_size=3, space_size=1):
    """
    Info:
    Will write "copyright" style where each sentance is its own line. 
    There is a linebreak after every line.
    
    paragraph_size:
    Will seperate paragraphs after every nth line from paragraph_size.

    space_size:
    Determines the size of the linebreaks and of the space. 
    1 is default, 2 is double-spaced, ect. Must be an int.
    """
    default_pattern = r"\.\s?|\?\s?|!\s?" # space optional
    matches = finditer(default_pattern, string)
    start = 0
    end = 0
    split = False
    composite_string = ''
    for match_number, match in enumerate(matches):
        start = end
        if (match_number + 1) % paragraph_size == 0:  # check if every nth line
            split = True
        else:
            pass
        end = match.span()[1]   
        iter_string = string[start:end] # no need for +1 b/c  .span()[1] is already an overshoot of + 1
        if split == True:
            iter_string += ("\n" * 2) * space_size
            split = False
        else:
            iter_string += "\n" * space_size
        composite_string += iter_string
    return composite_string




if __name__ == "__main__":
    import time
    import re

    def space():
        print('\n' * 3)
    test_string = "Python does not currently have an equivalent to scanf(). Regular expressions are generally more powerful, though also more verbose, than scanf() format strings. The table below offers some more-or-less equivalent mappings between scanf() format tokens and regular expressions."
    bible_string = "1:1 In the beginning God created the heaven and the earth. 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters."

    #rec = time.time_ns()
    # test_1 = print(string_indenter(test_string, length=50))
    #print(time.time_ns() - rec)

    # pattern = r"\.\s?|\?\s?|!\s?"  # match is (before,on) -> index of exact would be str[on -1]
    # match = re.finditer(pattern, test_string)
    # for num, item in enumerate(match):
    #     print(num)
    #     print(item.group(), item.groups(), item.span())
    # print(len(test_string), test_string[275], test_string[274])
    # first_sent = test_string[0:55 + 1]
    # print(f"{first_sent} {'x' in first_sent}")

    # bible_paragraph = paragraph_maker(bible_string, paragraph_size=3)
    # print(bible_paragraph)
    bible_format = string_indenter(bible_string, paragraph_size=3)
    print(bible_format)