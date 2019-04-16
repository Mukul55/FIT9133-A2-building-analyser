###############################################################
# FIT9133 ASSIGNMENT 2
# TASK 1: Handling with File Contents and Preprocessing
# Author's name: MUKUL GUPTA
# Student ID : 29873150
# Program first created : 27 September 2018
# Program last updated : 12 October 2018
###############################################################

###################################################################################################################
#####################---------INRODUCTION-----------####################
# In this program, we begin by reading in all the transcripts of the given dataset, for both the SLI and TD groups.
# We will then conduct a number of pre-processing tasks to extract only the relevant contents or texts needed for
# analysis in the subsequent tasks

#####################---------ASSUMPTIONS-----------####################
# I have replaced [* m:+ed] with [*] in the pre-processing
# Also, I have not deleted : in words. example th:en is not changed

# import os package for reading files
import os
# import re package for using regular expressions
import re


# clean_file_group(files_group) function cleans the files for file groups like SLI and TD
def clean_file_group(files_group):
    # set the path_files where files_group folder is stored
    path_files = './ENNI Dataset/' + files_group + '/'

    # set the path for cleaned file, where the cleaned will be stored after pre processing
    path_clean_files = './ENNI Cleaned/' + files_group + '_cleaned/'

    # files contain the list of all files within the files_group
    files = []

    # for each file in the files_group folder, do the pre processing
    for each in os.listdir(path_files):

        # if the file ends with .txt extension, open the file and append the object in files list
        # file is opened in read mode as no changes are to be made in the file
        if each.endswith('.txt'):
            files.append(open(path_files + each, "r"))

        for file in files:
            # chi_lines contain the list of all children lines present in the file
            chi_lines = []
            # to extract all the characters in the file, file.read() is used
            file_text = file.read()
            # In some cases, chi lines have multiple lines, so in order to make it one line, we replace '\n\t' with ' '
            file_text = file_text.replace('\n\t', ' ')
            # then we split the file into lines by splitting the file by newline character i.e. '\n'
            lines = file_text.split('\n')
            # for all lines in the file, we find the words by splitting the line with space
            # then we extract the children lines (lines which start with '*CHI' which is present in the first
            # word of the child line
            # we then append the children line to chi_lines list separated by newline charater '\n'
            for line in lines:
                word = line.split(' ')
                if '*CHI' in word[0]:
                    chi_lines.append(line + '\n')
            # we remove the ending '\n'
            if chi_lines:
                chi_lines[-1] = chi_lines[-1].strip('\n')

            # we join all the lines in chi_lines list and store it in file_text which is string
            file_text = ''.join(chi_lines)

            # we now have all the chi lines from the file
            # we remove the *CHI: from the file_text which contains all the chi_lines
            pat = re.compile('(\*CHI:\s)')

            # re.sub(a,b,c) substitutes the pattern a in the c string with b
            # In this case we substitute '*CHI:' with ''
            file_text = re.sub(pat, '', file_text)

            ######################## 1a ########################

            # Remove '[' and ']' but retain [//],[/],[* m:+ed]

            # I have replaced [//],[/],[* m:+ed] with other character strings so they don't match the regex
            # string afterwards. They are replaced afterwards with the original strings.
            # Replace [/] with %%% in the file_text
            file_text = re.sub(r'\[\/\]', '%%%', file_text)
            # Replace [//] with !!!
            file_text = re.sub(r'\[\/\/\]', '!!!', file_text)
            # Replace [* m:+ed] with ###
            file_text = re.sub(r'\[\*\sm:\+ed\]', '###', file_text)
            # '\[.*?\]' is the regex expression for [] which can contain anything inside
            pat = re.compile('\[.*?\]')
            # replace all the elements matching the pattern with '' i.e. nothing
            file_text = re.sub(pat, '', file_text)

            # Replace %%% with [/]
            file_text = re.sub(r'%%%', '[/]', file_text)
            # Replace !!! with [//]
            file_text = re.sub(r'!!!', '[//]', file_text)
            # Replace ### with [*]
            file_text = re.sub(r'###', '[*]', file_text)

            ######################## 1b ########################

            # Remove '<' and '>'

            # '<|>' is the regex expression for < or >
            pat = re.compile('<|>')
            # replace all the elements matching the pattern with '' i.e. nothing
            file_text = re.sub(pat, '', file_text)

            ######################## 1c ########################

            # Remove words with prefixes '&' and '+'

            # '[&+]\S*' is the regex expression for words starting with &+
            pat = re.compile('[&+]\S*')
            # replace all the elements matching the pattern with '' i.e. nothing
            file_text = re.sub(pat, '', file_text)

            ######################## 1d ########################

            # Retain words with '(' as prefix and ')' as suffix but remove these two symbols

            # Replace (.) with @@@
            file_text = re.sub(r'\(\.\)', '@@@', file_text)
            # Replace (..) with ()
            file_text = re.sub(r'\(\..\)', '()', file_text)
            # Replace (...) with ()
            file_text = re.sub(r'\(\...\)', '()', file_text)

            # '(\(|\))' is the regex expression for symbols ( or )
            pat = re.compile('(\(|\))')
            # replace all the elements matching the pattern with '' i.e. nothing
            file_text = re.sub(pat, '', file_text)
            # Replace @@@ with (.)
            file_text = re.sub(r'@@@', '(.)', file_text)

            ######################## Writing file after pre-processing ########################
            # if the directory /ENNI Cleaned/ is not created, then create it
            if not os.path.exists(path_clean_files):
                os.makedirs(path_clean_files)
            # open the cleaned file with the cleaned file path in write mode
            clean_file = open(path_clean_files + each, 'w')
            # write the file_text into the clean file
            clean_file.write(file_text)
            # close the clean_file
            clean_file.close()
    # close all the files in files list
    for file in files:
        file.close()

    # if no exception occurs and function reaches till this point, i.e. everything is OK, then return 1
    return 1


# main function is where the pre-processing function is called for SLI and TD groups
def main():
    # call the pre-processing function for the SLI group
    file_cleaned_SLI = clean_file_group('SLI')
    # call the pre-processing function for TD group
    file_cleaned_TD = clean_file_group('TD')
    # If both the functions returned 1 then the trascripts were cleaned successfully, else
    # something went wrong
    if (file_cleaned_SLI == 1) & (file_cleaned_TD == 1):
        print('SLI and TD transcripts cleaned successfully')
    else:
        print('SLI and TD transcripts failed to clean')


# When the program is run, special variable __name__ is initialized to __main__
# Thus code only executes when we want to run the module as a program
# Reference: Mortensen, P. (2009). Retrieved from https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
