# Telephone_Book
   [A Telephone Book Conversion (pypi)](https://pypi.org/project/phonewordzp/)

  ![Phone Pad](https://i.stack.imgur.com/mhJ3f.png)

    Package Installation:
              1.need to install regular expression by: [pip install re]
              2.need to install English Dictionary package pyenchant by: [pip install pyenchant]
              3.After that install phonewordzp by: [pip install phonewordzp]
              
    Run phonewordzp:
              phonewordzp is a object oriented class, that require an input string with word and letter's combinations equals to 10 or 11. 
              Every function has a display for display elapsed time used in this function
              For every functions, other char will be taken care of by regular expression. For instance '(765)-683-7890', '765-683-7890' can both be used as a string for input
              1. Initialize onject class: phone_obj = Telephone_Book('(765)-683-7890')
              2. Use word_to_numbers(), given an input of combinations of words and numbers, generate return numbers only. 
                    - number = '1-800-PAINTER'
                    - phone_obj = Telephone_Book(number)
                    - print(phone_obj.words_to_number())
                 Output:
                    Request Time: 0.00013589859008789062

                    1-800-724-6837
              3. Use all_wordifications(), given a list of numbers, generate all matched combinations of English Words and numbers. 
                 Note: To iterate through all the combinations for words and numbers requires computations and divide and conquer. 
                       In order to generate solutions in limited stack size, the original string is divided by 0s and 1s since they don't have mapping.
                       Even though, the longest divide part is length == 8.The function will reject for subsequence "785789898"
                    - number = '1-800-724-6837'
                    - phone_obj = Telephone_Book(number)
                    - print(phone_obj.all_wordifications())
                 Output:
                    Request Time: 0.228956937789917

                   ['1-T00-7-246837', '1-T00-P-246837', '1-T00-Q-246837', '1-T00-R-246837', '1-T00-S-246837', '1-T00-72-46837', '1-T00-72-INTER', '1-T00-PA-46837', '1-T00-PA-INTER', '1-T00-PB-46837', '1-T00-PB-INTER', '1-T00-PC-46837', '1-T00-PC-INTER', '1-T00-QA-46837', '1-T00-QA-INTER', '1-T00-QB-46837', '1-T00-QB-INTER', '1-T00-QC-46837', '1-T00-QC-INTER', '1-T00-RA-46837', '1-T00-RA-INTER', '1-T00-RB-46837', '1-T00-RB-INTER', '1-T00-RC-46837', '1-T00-RC-INTER', '1-T00-SA-46837', '1-T00-SA-INTER', '1-T00-SB-46837', '1-T00-SB-INTER', '1-T00-SC-46837', '1-T00-SC-INTER', '1-T00-724-6837', '1-T00-724-MUDS', '1-T00-724-OTES', '1-T00-724-OVER', '1-T00-RAG-6837', '1-T00-RAG-MUDS', '1-T00-RAG-OTES', '1-T00-RAG-OVER', '1-T00-RAG-6837', '1-T00-RAG-MUDS', '1-T00-RAG-OTES', '1-T00-RAG-OVER', '1-T00-RBI-6837', '1-T00-RBI-MUDS', '1-T00-RBI-OTES', '1-T00-RBI-OVER', '1-T00-SAG-6837', '1-T00-SAG-MUDS', '1-T00-SAG-OTES', '1-T00-SAG-OVER', '1-T00-SAG-6837', '1-T00-SAG-MUDS', '1-T00-SAG-OTES', '1-T00-SAG-OVER', '1-T00-SCI-6837', '1-T00-SCI-MUDS', '1-T00-SCI-OTES', '1-T00-SCI-OVER', '1-T00-7246-837', '1-T00-PAIN-837', '1-T00-RAIN-837', '1-T00-SAGO-837', '1-T00-SAGO-837', '1-T00-72468-37', '1-T00-72468-DP', '1-T00-72468-DR', '1-T00-72468-ER', '1-T00-72468-ES', '1-T00-72468-FR', '1-T00-PAINT-37', '1-T00-PAINT-DP', '1-T00-PAINT-DR', '1-T00-PAINT-ER', '1-T00-PAINT-ES', '1-T00-PAINT-FR', '1-T00-SAINT-37', '1-T00-SAINT-DP', '1-T00-SAINT-DR', '1-T00-SAINT-ER', '1-T00-SAINT-ES', '1-T00-SAINT-FR', '1-T00-724683-7', '1-T00-724683-P', '1-T00-724683-Q', '1-T00-724683-R', '1-T00-724683-S', '1-U00-7-246837', '1-U00-P-246837', '1-U00-Q-246837', '1-U00-R-246837', '1-U00-S-246837', '1-U00-72-46837', '1-U00-72-INTER', '1-U00-PA-46837', '1-U00-PA-INTER', '1-U00-PB-46837', '1-U00-PB-INTER', '1-U00-PC-46837', '1-U00-PC-INTER', '1-U00-QA-46837', '1-U00-QA-INTER', '1-U00-QB-46837', '1-U00-QB-INTER', '1-U00-QC-46837', '1-U00-QC-INTER', '1-U00-RA-46837', '1-U00-RA-INTER', '1-U00-RB-46837', '1-U00-RB-INTER', '1-U00-RC-46837', '1-U00-RC-INTER', '1-U00-SA-46837', '1-U00-SA-INTER', '1-U00-SB-46837', '1-U00-SB-INTER', '1-U00-SC-46837', '1-U00-SC-INTER', '1-U00-724-6837', '1-U00-724-MUDS', '1-U00-724-OTES', '1-U00-724-OVER', '1-U00-RAG-6837', '1-U00-RAG-MUDS', '1-U00-RAG-OTES', '1-U00-RAG-OVER', '1-U00-RAG-6837', '1-U00-RAG-MUDS', '1-U00-RAG-OTES', '1-U00-RAG-OVER', '1-U00-RBI-6837', '1-U00-RBI-MUDS', '1-U00-RBI-OTES', '1-U00-RBI-OVER', '1-U00-SAG-6837', '1-U00-SAG-MUDS', '1-U00-SAG-OTES', '1-U00-SAG-OVER', '1-U00-SAG-6837', '1-U00-SAG-MUDS', '1-U00-SAG-OTES', '1-U00-SAG-OVER', '1-U00-SCI-6837', '1-U00-SCI-MUDS', '1-U00-SCI-OTES', '1-U00-SCI-OVER', '1-U00-7246-837', '1-U00-PAIN-837', '1-U00-RAIN-837', '1-U00-SAGO-837', '1-U00-SAGO-837', '1-U00-72468-37', '1-U00-72468-DP', '1-U00-72468-DR', '1-U00-72468-ER', '1-U00-72468-ES', '1-U00-72468-FR', '1-U00-PAINT-37', '1-U00-PAINT-DP', '1-U00-PAINT-DR', '1-U00-PAINT-ER', '1-U00-PAINT-ES', '1-U00-PAINT-FR', '1-U00-SAINT-37', '1-U00-SAINT-DP', '1-U00-SAINT-DR', '1-U00-SAINT-ER', '1-U00-SAINT-ES', '1-U00-SAINT-FR', '1-U00-724683-7', '1-U00-724683-P', '1-U00-724683-Q', '1-U00-724683-R', '1-U00-724683-S', '1-V00-7-246837', '1-V00-P-246837', '1-V00-Q-246837', '1-V00-R-246837', '1-V00-S-246837', '1-V00-72-46837', '1-V00-72-INTER', '1-V00-PA-46837', '1-V00-PA-INTER', '1-V00-PB-46837', '1-V00-PB-INTER', '1-V00-PC-46837', '1-V00-PC-INTER', '1-V00-QA-46837', '1-V00-QA-INTER', '1-V00-QB-46837', '1-V00-QB-INTER', '1-V00-QC-46837', '1-V00-QC-INTER', '1-V00-RA-46837', '1-V00-RA-INTER', '1-V00-RB-46837', '1-V00-RB-INTER', '1-V00-RC-46837', '1-V00-RC-INTER', '1-V00-SA-46837', '1-V00-SA-INTER', '1-V00-SB-46837', '1-V00-SB-INTER', '1-V00-SC-46837', '1-V00-SC-INTER', '1-V00-724-6837', '1-V00-724-MUDS', '1-V00-724-OTES', '1-V00-724-OVER', '1-V00-RAG-6837', '1-V00-RAG-MUDS', '1-V00-RAG-OTES', '1-V00-RAG-OVER', '1-V00-RAG-6837', '1-V00-RAG-MUDS', '1-V00-RAG-OTES', '1-V00-RAG-OVER', '1-V00-RBI-6837', '1-V00-RBI-MUDS', '1-V00-RBI-OTES', '1-V00-RBI-OVER', '1-V00-SAG-6837', '1-V00-SAG-MUDS', '1-V00-SAG-OTES', '1-V00-SAG-OVER', '1-V00-SAG-6837', '1-V00-SAG-MUDS', '1-V00-SAG-OTES', '1-V00-SAG-OVER', '1-V00-SCI-6837', '1-V00-SCI-MUDS', '1-V00-SCI-OTES', '1-V00-SCI-OVER', '1-V00-7246-837', '1-V00-PAIN-837', '1-V00-RAIN-837', '1-V00-SAGO-837', '1-V00-SAGO-837', '1-V00-72468-37', '1-V00-72468-DP', '1-V00-72468-DR', '1-V00-72468-ER', '1-V00-72468-ES', '1-V00-72468-FR', '1-V00-PAINT-37', '1-V00-PAINT-DP', '1-V00-PAINT-DR', '1-V00-PAINT-ER', '1-V00-PAINT-ES', '1-V00-PAINT-FR', '1-V00-SAINT-37', '1-V00-SAINT-DP', '1-V00-SAINT-DR', '1-V00-SAINT-ER', '1-V00-SAINT-ES', '1-V00-SAINT-FR', '1-V00-724683-7', '1-V00-724683-P', '1-V00-724683-Q', '1-V00-724683-R', '1-V00-724683-S', '1-800-7-246837', '1-800-P-246837', '1-800-Q-246837', '1-800-R-246837', '1-800-S-246837', '1-800-72-46837', '1-800-72-INTER', '1-800-PA-46837', '1-800-PA-INTER', '1-800-PB-46837', '1-800-PB-INTER', '1-800-PC-46837', '1-800-PC-INTER', '1-800-QA-46837', '1-800-QA-INTER', '1-800-QB-46837', '1-800-QB-INTER', '1-800-QC-46837', '1-800-QC-INTER', '1-800-RA-46837', '1-800-RA-INTER', '1-800-RB-46837', '1-800-RB-INTER', '1-800-RC-46837', '1-800-RC-INTER', '1-800-SA-46837', '1-800-SA-INTER', '1-800-SB-46837', '1-800-SB-INTER', '1-800-SC-46837', '1-800-SC-INTER', '1-800-724-6837', '1-800-724-MUDS', '1-800-724-OTES', '1-800-724-OVER', '1-800-RAG-6837', '1-800-RAG-MUDS', '1-800-RAG-OTES', '1-800-RAG-OVER', '1-800-RAG-6837', '1-800-RAG-MUDS', '1-800-RAG-OTES', '1-800-RAG-OVER', '1-800-RBI-6837', '1-800-RBI-MUDS', '1-800-RBI-OTES', '1-800-RBI-OVER', '1-800-SAG-6837', '1-800-SAG-MUDS', '1-800-SAG-OTES', '1-800-SAG-OVER', '1-800-SAG-6837', '1-800-SAG-MUDS', '1-800-SAG-OTES', '1-800-SAG-OVER', '1-800-SCI-6837', '1-800-SCI-MUDS', '1-800-SCI-OTES', '1-800-SCI-OVER', '1-800-7246-837', '1-800-PAIN-837', '1-800-RAIN-837', '1-800-SAGO-837', '1-800-SAGO-837', '1-800-72468-37', '1-800-72468-DP', '1-800-72468-DR', '1-800-72468-ER', '1-800-72468-ES', '1-800-72468-FR', '1-800-PAINT-37', '1-800-PAINT-DP', '1-800-PAINT-DR', '1-800-PAINT-ER', '1-800-PAINT-ES', '1-800-PAINT-FR', '1-800-SAINT-37', '1-800-SAINT-DP', '1-800-SAINT-DR', '1-800-SAINT-ER', '1-800-SAINT-ES', '1-800-SAINT-FR', '1-800-724683-7', '1-800-724683-P', '1-800-724683-Q', '1-800-724683-R', '1-800-724683-S']
                   
            4. Use number_to_words(), given a list of numbers, return one solution of words+numbers combinations. 
               To simplify computations and code effcient. called all_wordifications and randomly return a solution from solutions
                    - number = '1-800-724-6837'
                    - phone_obj = Telephone_Book(number)
                    - print(phone_obj.number_to_words())
                    
                 Output:
                    Request Time: 0.22414898872375488

                    1-T00-Q-24683
    Project Scope:
    
        1. 50% times are used to analyze the problems, rest time for debugging and coding.
        2. Be speed effcient, use regular expression and pyenchant so doesn't need to work with managing chars and built english dictionary.
        3. Be aware of the sizes of the problem. Broke down to smaller problem if you can (0s and 1s use as divider).
        4. for substring '228', generate all substrings from 228 and use hash_table to store the possible English words. 
           Then, re-assemble solutions according to hash_tables's solution.
              - For instance solutions for '228':'CAT'
                                      ('2', '28'): ['2', 'AT']
          Iterate through substring's solutions, and attached to the class inheritance hash_table by hash_table['228'] = solutions from '228'.
          The smaller hash_table get destroyed when local function exited. 
        5. By updating only combination's that is a valid word, total combinations get reduced and manageble if substring is not too large(<= 8).
        6. Use Git Branch to update new contents once the basic structure has been created.
        7. Some reference for package usages:
          pyenchant https://pypi.org/project/pyenchant/
          re https://www.programiz.com/python-programming/regex
          generate combinations from telephone numbers: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
          get all combinations substring: https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
          git usage: https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/
