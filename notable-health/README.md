# Parser.py 

### Description 
Problem: Doctors often verbally dictate their clinical note after seeing a patient. These
dictations are transcribed word-for-word and then formatted to generate the final note. As part
of their dictation, doctor’s need a simple way to insert numbered lists. To accomplish this, we
have provided the doctor with some phrases that they can say in order to indicate the start of a
numbered list and every next item.

To start a numbered list, the doctor would say “Number n”, where n is a number from one to
nine, then say what they would want as the nth item in the numbered list. To indicate the start
of the next item in the numbered list, the doctor would say “Number next”, then say what they
would want as the next item in the numbered list. For example, the “Number next” item after
saying the “Number one” item would be the second item in the numbered list. The doctor
would then repeat the “Number next” steps until they reach the end of their numbered list.



### How-To Use
```
./parser.py sample_text
```
-----
### Improvements
1. This is disk heavy
    Ideally I should read the file once and then perform all the find and replaces in memory. 
    Or write a helper script in bash to to the regex lifting. 
2. Work out line breaks. The regex isn't fully replacing line breaks with spaces, easily fixable 
3. insert_at_number_n function doesn't take into account duplicates at that position. 
4. list_copier needs to be removed
5. some logic reorg would be great in main 

-----
### Notes 

I really enjoyed this problem, it was pretty straight forward with a few gotchas. Once you figured 
them out it was easy to work around. I wish all questions were like this. 

-----

