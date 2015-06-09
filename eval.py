#!/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import aiml
import subprocess
from itertools import izip

# Load Kernel from AIML
k1 = aiml.Kernel()
k2 = aiml.Kernel()

file1 = "aiml/bot1.aiml"
k1.learn(file1)

file2 = "aiml/bot2.aiml"
k2.learn(file2)

with open('input/music.txt') as textfile1, open('expected/music.txt') as textfile2:

    count = 0
    fail1 = 0
    invalid1 = 0
    fail2 = 0
    invalid2 = 0
    both_failed = 0

    for user, expected in izip(textfile1, textfile2):
        user = user.strip()
        expected = expected.strip()

        count+=1
        print ">>> User: "+user

        failed1 = 0
        failed2 = 0
        inval1 = 0
        inval2 = 0

        # - - - - - - - - - - - - - - - - - - -
        answer1 = k1.respond(user)
        if (answer1 == ""):
            print "\033[1;31m(1) FAILED\033[0m"
            fail1+=1
            failed1 = 1
        else:
            print "<<< AI_1: "+answer1+"\n\033[1;32m(1) PASSED\033[0m"
            if answer1 == expected:
                print "\033[1;32m(1) VALID\033[0m"
            else:
                print "\033[1;31m(1) INVALID\033[0m"
                invalid1 += 1
                inval1 = 1

        print "~\t~\t~\t~\t~\t~"

        answer2 = k2.respond(user)
        if (answer2 == ""):
            print "\033[1;31m(2) FAILED\033[0m"
            fail2+=1
            failed2 = 1
        else:
            print "<<< AI_2: "+answer2+"\n\033[1;32m(2) PASSED\033[0m"
            if answer2 == expected:
                print "\033[1;32m(2) VALID\033[0m"
            else:
                print "\033[1;31m(2) INVALID\033[0m"
                invalid2 += 1
                inval2 = 1

        if (failed1 and not failed2):
            print "> \033[1;34mNOT OK!\033[0m"
        if (inval1 and not inval2 and not failed2):
            print "> \033[1;34mNOT OK!\033[0m"
        if (failed2 and not failed1) or (inval2 and not inval1 and not failed1):
            print "+ \033[1;34mImprovement\033[0m"

        print "________________________________________________________\n"

print file1
print "====================================================="
understood = count-fail1
valid = understood-invalid1
print "#\tsentences: \t"+str(count)+"\t100.0%"
print "#\tunderstood:\t"+str(understood)+"\t"+str(understood/count*100.0)+"%"
print "#\tvalidated: \t"+str(valid)+"\t"+str(valid/count*100.0)+"%"
print "====================================================="

print ""

print file2
print "====================================================="
understood = count-fail2
valid = understood-invalid2
print "#\tsentences: \t"+str(count)+"\t100.0%"
print "#\tunderstood:\t"+str(understood)+"\t"+str(understood/count*100.0)+"%"
print "#\tvalidated: \t"+str(valid)+"\t"+str(valid/count*100.0)+"%"
print "====================================================="

print ""
if (both_failed == fail1):
    print "> \033[1;34mWhen (2) fails, (1) fails\033[0m"


print "\nEvaluation terminated"
