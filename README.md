# AIMLComparator
A simple Python script that allows you to compare two AIML bots

## Why do I want it?
You want to compare two chatterbots (basically, two different versions of the same bot).

## How does it work?
- The two bots read from the same file that contains some sentences that any user could say
- The program tells you if
    - The bot **has an answer** for that
    - The bot replied **correctly**
- The correctness of the reply is evaluated with a file containing the expected output.

## How to use it?
1. In ``eval.py`` change the following lines
```python
file1 = "aiml/bot1.aiml"
file2 = "aiml/bot2.aiml"
with open('input/meteo.txt') as textfile1, open('expected/meteo.txt') as textfile2:
```
``file1`` and ``file2`` are the two AIML bots, ``input/meteo.txt`` is the file containing the user input, and ``expected/meteo.txt`` contains the expected output given by the bots.
2. Simply type ``python eval.py`` in the terminal

## Typical output

<pre>
>>> User: Le temps d'aujourd hui annonce quoi?
<<< AI_1: Il va faire beau aujourd'hui
(1) PASSED
(1) VALID
~	~	~	~	~	~
WARNING: No match found for input: Le temps d'aujourd hui annonce quoi
(2) FAILED
+ Improvement
________________________________________________________

>>> User: J'ai raté la météo à la TV, quel temps fait il?
<<< AI_1: Il fera beau aujourd'hui à TV, quel temps fait il
(1) PASSED
(1) INVALID
~	~	~	~	~	~
<<< AI_2: Il fera beau aujourd'hui à TV, quel temps fait il
(2) PASSED
(2) INVALID
________________________________________________________

>>> User: La météo à Grenoble ce soir?
<<< AI_1: Ce soir, à Grenoble, il fera beau!
(1) PASSED
(1) VALID
~	~	~	~	~	~
<<< AI_2: Ce soir, à Grenoble, il fera beau!
(2) PASSED
(2) VALID
________________________________________________________

aiml/bot1.aiml
=====================================================
#	sentences: 	37	100.0%
#	understood:	31	83.7837837838%
#	validated: 	25	67.5675675676%
=====================================================

aiml/bot2.aiml
=====================================================
#	sentences: 	37	100.0%
#	understood:	18	48.6486486486%
#	validated: 	15	40.5405405405%
=====================================================
</pre>
