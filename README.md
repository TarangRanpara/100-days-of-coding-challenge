# 100-days-of-coding-challenge
This is where I keep my code submitted for "100 days of coding challenge".

Problem-1: 

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example :
array [ 1,2,3,4,5] 
So now our 
minimum sum = 1+2+3+4 =>10  
maximum sum=>2+3+4+5 =>14 

so output of program : 10 14


problem-2:

You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3, she will be able to blow out  2 candles successfully, since the tallest candles are of height  4 and there are 2 such candles.

Case 1: 
Input : 4
4,4,1,3
Output : 2

Case 2:
input : 4
3,2,1,3
output : 2

problem-3:

Take one Number from user and print "Positive Number" or "Negative Number" ,
sounds easy ??

Now adding one more condition you are not allowed to use any Conditional statements like if , if else ,switch, while , for , a ? b 

Now it's Interesting right ??
Input : 5
Output : Positive Number 

Input : -6 
Output : Negative Number

problem-4:

Check given number is palindrome number or not ?

Easy ??

find nearest palindrome number of given number. 

Example 1:
input : 111
Output : 
111 is Palindrome Number 
Nearest Palindrome Number is 101 (111-101 =>10 and 121-101=>10 so take anyone)

Example 2:
input : 103
Ouput:
103 is Not Palindrome Number
Nearest Palindrome Number is 101 

problem-5:

Problem statement:
You have been given a String S
consisting of uppercase and lowercase English alphabets.
You need to change the case of each alphabet in this String.

Input String : abcdE
Output string : ABCDe

problem-6:

Write a program to check if two given String is Anagram of each other. Your function should return true if two Strings are Anagram, false otherwise. A string is said to be an anagram if it contains same characters and same length but in different order e.g. army and Mary are anagrams. You can ignore cases for this.

Input : 
1)Number of Strings 
2)each input contain 2 strings
Output : True or False 

Example 1:
Input : 2
1)
=>army , mary
2)
=>raj , jar

problem-7:

Find the first non repeated character from String. Example if given String is "Morning" then it should print "M"
Input : 1-string 
output : 1-char

Example :
Input : Kick
Output : I

problem-8:

Little guru is very fond of playing games. Recently, He found a few straws each of length 1 inches in the store room. He took all of them and decided to mark a rectangular area on the floor with straws and warn rest of the family members to not to enter that area so that he can play in peace. He wants to maximize that area. But, unable to do so, He seeks for your help. You being the elder brother of guru, write a program for him to find maximum area that he can cover in inches using N straws.

Input:

First line of input contains an integer t. 

then, t lines follow each containing a single integer

 N - No of straws.

Output:

Print the area of largest rectangle that can be formed using the given sticks. 
simple Input :
3
6
9
11
Simple Output :
2
4
6
