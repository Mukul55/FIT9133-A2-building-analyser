###############################################################
# FIT9133 ASSIGNMENT 2
# TASK 2: Building a Class for Data Analysis
# Author's name: MUKUL GUPTA
# Student ID : 29873150
# Program first created : 27 September 2018
# Program last updated : 12 October 2018
###############################################################

###################################################################################################################
#####################---------INRODUCTION-----------####################
# In this program, we create a class Analyser and generate a number of statistics for the two groups of children
# transcripts. This  class would be useful for the third part when we have to plot the statistics
# The statistics are printed out in the end.

# import re package for using regular expressions
import re


# calc_length(path) function calculates the length of the transcript.
# path of the transcript is passed as an argument
def calc_length(path):
    # file is opened in reading mode
    file = open(path, "r")
    # length of the file is calculated by summing 1 for all lines in the transcript
    total = sum(1 for line in file)
    # file is closed
    file.close()
    # total is returned which contains the length of the transcript
    return total


# calc_vocab_size(path) function calculates the size of the vocabulary indicated by number of unique words
def calc_vocab_size(path):
    # file is opened in reading mode
    file = open(path, "r")
    # '[^\s\[\*\]\.\(\)\/\!\?]+' regular expression represents all words but ignores spaces, ., !
    # including other symbols
    pat = '[^\s\[\*\]\.\(\)\/\!\?]+'
    # all the occurrences of the regex is found using re.findall
    match_pat = re.findall(pat, file.read())
    # file is closed
    file.close()
    # all the matched words are converted to set to find the unique words
    # length of the set i.e. number of unique words is returned
    return len(set(match_pat))


# calc_symbol_length(path, symbol) calculates repetition of certain CHAT symbols like [/], [//], (.) and [*]
def calc_symbol_length(path, symbol):
    # file is opened in reading mode
    file = open(path, "r")
    # symbol_count represents total number of symbols and is initialised to 1
    symbol_count = 0
    # for each line in the file, we split each word by space (' ') and if the word is same as the symbol, count
    # of the symbol that is represented by symbol_count is incremented by 1
    for line in file:
        for word in line.split():
            if word == symbol:
                symbol_count += 1
    # file is closed
    file.close()
    # symbol_count is returned
    return symbol_count


# Analyser class is created to calculate the statistics of the two groups from the cleaned files created in Task 1.
class Analyser:

    # this function initialises the six statistics that stores the statistics of a file as well as
    # statistics dictionary stats_dict which contains all the statistics of all the files in a specific child group
    def __init__(self):
        # length indicates the number of statements
        self.length = 0
        # vocab_size indicates the number of unique words i.e. the vocabulary
        self.vocab_size = 0
        # repetition indicates the number of repetition for certain words or phrases indicated by [/]
        self.repetition = 0
        # retrace indicates the number of retracing for certain words or phrases indicated by [//]
        self.retrace = 0
        # gram_error indicates the number of grammatical errors indicated by [*]
        # * m:+ed] was replaced by [*] in Task 1
        self.gram_error = 0
        # pauses indicates the number of pauses made indicated by (.)
        self.pauses = 0
        # stats_dict stores stats for every file in a specific child group
        # this will be used in task 3
        # values in the dictionary will be a list of all the stats in a particular child group
        self.stats_dict = {'Length of Transcript': [], 'Vocabulary Size': [], 'Repetition words [/]': [],
                           'Retracing words [//]': [], 'Grammatical errors': [], 'Number of Pauses': []}

    # get_stats_dict() returns the stats dictionary
    # this is used in task 3
    def get_stats_dict(self):
        return self.stats_dict

    # analyse_script() calculates all the stats using functions defined outside the class and stores the values
    # in the dictionary that can be used in Task 3
    def analyse_script(self, path):
        # length of the transcript is calculated by passing the file path
        self.length = calc_length(path)
        # vobulary size is calculated
        self.vocab_size = calc_vocab_size(path)
        # number of [/] symbols are calculated
        self.repetition = calc_symbol_length(path, '[/]')
        # number of [//] symbols are calculated
        self.retrace = calc_symbol_length(path, '[//]')
        # number of [*] symbols are calculated
        self.gram_error = calc_symbol_length(path, '[*]')
        # number of (.) symbols are calculated
        self.pauses = calc_symbol_length(path, '(.)')
        # all stats are appended in the list of the dictionary by their respective keys
        self.stats_dict['Length of Transcript'].append(self.length)
        self.stats_dict['Vocabulary Size'].append(self.vocab_size)
        self.stats_dict['Repetition words [/]'].append(self.repetition)
        self.stats_dict['Retracing words [//]'].append(self.retrace)
        self.stats_dict['Grammatical errors'].append(self.gram_error)
        self.stats_dict['Number of Pauses'].append(self.pauses)

    # __str__() is called when we print the object of the class
    # it defines how the object should be printed
    # all stat values are displayed for each file in a particular child group
    def __str__(self):
        return 'Length of transcript: ' + str(self.length) + '\tVocabulary Size: ' \
               + str(self.vocab_size) + '\tRepetition [/]: ' + str(self.repetition) + \
               '\tRetracing [//]: ' + str(self.retrace) + '\tGrammatical errors [*]: ' \
               + str(self.gram_error) + '\tPauses (.): ' + str(self.pauses)


# main function is where objects of the class are created and methods are called on those objects
def main():
    # we define the child group to 'SLI'
    files_group = 'SLI'
    # path of the cleaned files of SLI is given
    path_clean_files = './ENNI Cleaned/' + files_group + '_cleaned/'
    # object of the Analyser class is created for SLI group
    analyser_ObjSLI = Analyser()
    # for each file in the clean files stats are calculated for each of the file in SLI group
    # file_no takes values from 1 to 10
    for file_no in range(1, 11):
        # analyse_script method is called on the SLI group object
        analyser_ObjSLI.analyse_script(path_clean_files + 'SLI-' + str(file_no) + '.txt')
        print(files_group + ' ' + str(file_no) + ' statistics')
        # print function on the object calls the __str__ method and the object is printed using the
        # string defined in __str__
        print(analyser_ObjSLI)
        print('\n')

    # files_group is then set to 'TD'
    files_group = 'TD'
    # path of the cleaned files of TD is given
    path_clean_files = './ENNI Cleaned/' + files_group + '_cleaned/'
    # object of the Analyser class is created for TD group
    analyser_ObjTD = Analyser()
    # for each file in the clean files stats are calculated for each of the file in TD group
    # file_no takes values from 1 to 10
    for file_no in range(1, 11):
        # analyse_script method is called on the TD group object
        analyser_ObjTD.analyse_script(path_clean_files + 'TD-' + str(file_no) + '.txt')
        print(files_group + ' ' + str(file_no) + ' statistics')
        # print function on the object calls the __str__ method and the object is printed using the
        # string defined in __str__
        print(analyser_ObjTD)
        print('\n')


# When the program is run, special variable __name__ is initialized to __main__
# Reference: Mortensen, P. (2009). Retrieved from https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()