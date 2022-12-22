from math import floor
from re import finditer

def string_format(string, length=50, paragraph_size=0,space_size=1):
    """
    About:
    Shapes a body of text to match within 80%+ of the
    given length. 
    Adds line breaks after every nth time the line length in a string
    has been met,
    provided that part of the string is a space.
    Also makes paragraphs that fit roughly within the specified length. 
    The function does not guarantee a paragraph after every nth sentance,
    but will try to approximate as best as possible.
    """
    string_length = len(string)
    print(f"string length: {string_length}")
    ratio = string_length // length
    index_jump = floor(0.8 * length) 
    composite_string = ''
    nth_snippet = ''
    index_start = 0
    index_end_non_inclusive = 0
    DEFINITE_END = string_length - 1
    rotate = True
    space = False



    while rotate is True:
        for turn, rotation in enumerate(range(ratio)):
            index_start = index_end_non_inclusive
            index_end_non_inclusive += index_jump
            while string[index_end_non_inclusive] != " ":
                index_end_non_inclusive += 1
            if string[index_end_non_inclusive] == " ":
                nth_snippet = string[index_start:index_end_non_inclusive] # initialized nth_snippet
                #print(f"snippet: #{nth_snippet}#")
            try:
                if (turn + 1) % paragraph_size == 0:
                    space = True
            except ZeroDivisionError:
                pass
            
            # PARAGRAPH MODE ON 
                #check and see if paragraph mode is on and sentance is invalid

            if space == True and "." in nth_snippet[0:-1]:  # if its time for a space, and there is a period inside the middle of the snippet
                index_zero = nth_snippet[0]  # current nth_snippet character
                index_zero_value = 0 # index value
                hold_this = ''
                period_index = nth_snippet.find(".")
                if index_zero != " " or "\n":  # include char
                    index_zero_value = 0
                else:
                    index_zero_value = 1  # skip char
                hold_this = nth_snippet[index_zero_value:period_index + 1] + ("\n" * 2) + nth_snippet[period_index + 2:]
                print(f"Hold:#{hold_this}#")
                nth_snippet = hold_this
                nth_snippet += ("\n") * space_size
                nth_snippet.lstrip()
                #print(f"Hold2:#{hold_this}#")
                composite_string += nth_snippet.lstrip()
                space = False
            else:
                nth_snippet += "\n"
                composite_string += nth_snippet.lstrip()
        




        # CONDITIONS FOR TAIL END #        
        nth_snippet = string[index_end_non_inclusive:DEFINITE_END + 1]  # end of string established
        start = 0
        lenth_of_tail_end = len(nth_snippet)
        if lenth_of_tail_end <= length:  # length + length * .2 ? 
            pass
        else:
            left_over = length - lenth_of_tail_end
            while nth_snippet[left_over] != " ":
                try: 
                    left_over -= 1
                except IndexError:
                    left_over += 1
            if nth_snippet[left_over] == " ":
                hold_this = nth_snippet[start:left_over + 1] + "\n" + nth_snippet[left_over + 1:]  # split the last nth and add a breakline
            nth_snippet = hold_this
            #print(f" hold final #{hold_this}#")
            #nth_snippet = hold_this

        #remainder = (DEFINITE_END - index_end_non_inclusive) 

        #print(f"nth snippet: {nth_snippet} index end: {index_end_non_inclusive} str length: {string_length}  def end: {DEFINITE_END}") # debug
        composite_string += nth_snippet.lstrip()
        rotate = False
        return composite_string
    # TODO
    # the function has to account for spaces
    # FIX the algorithm that divides the last string into two:
    # check to see if the length of the tail is less than
    # or equal to the specified parameter length. 
    # if so, just leave it alone. 
    # if it is get the length total, attempt to chop off another remainder
    # slap the remaining on, then slap on the remainder.  



#print(string_format("Listen to rich people. It's that simple.", length=50))
#print(string_format("Raw action solves everything. Caution breeds fear.", length=40, paragraph_size=0))


#print(string_format("Listen to rich people. It's that simple.", length=50))


print(string_format("If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways.", paragraph_size=2, length=40))

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



