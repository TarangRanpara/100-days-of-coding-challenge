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

problem-9:

Given two weights of X and Y units,
How many different ways you can achieve a weight of D units using only the given weight.
Any of the given weights can be used any number of times (including 0 number of times).

Input Format:
The first line of input consists of an integer T denoting the number of test cases.
Each test case consists of only one line containing three space separated integers X, Y and D.
Output Format:
For each test case, print the answer in a separate line.

Example :
Sample Input
4
2,3,7
4,10,6
6,14,0
2,3,6 
Output 
1
0
1
2
Explanation
Test case 1:
D = 7 , X = 2 , Y = 3
7 can be achieved by using X two times and Y one time [2(2)+3(1)]=>[4+3=7].so answer = 1
Test case 2:
D = 6 , X = 4 , Y = 10
6 can not be achieved by X and Y. so answer 0.
Test case 3:
D = 0 , X = 6 , Y = 14
0 can be achieved by X zero times and Y zero time [6(0)+14(0)]=>[0+0=0].so answer = 1
Test case 4:
D = 6 , X =2 , Y = 3
6 can be achieved by using X three times or Y two times. so answer = 2

problem-10:

Ram purchased an array A having N integer values. After playing it for a while, he got bored of it and decided to update value of its element. In one second he can increase value of each array element by 1. He wants each array element's value to become greater than or equal to K. Please help Ram to find out the minimum amount of time it will take, for him to do so.

Input: 
First line consists of a single integer, T, denoting the number of test cases. 
First line of each test case consists of two space separated integers denoting N and K. 
Second line of each test case consists of N space separated integers denoting the array A.

Output:
For each test case, print the minimum time in which all array elements will become greater than or equal to K. Print a new line after each test case.

SAMPLE INPUT 
2
3 4
1 2 5
3 2
2 5 5
SAMPLE OUTPUT 
3
0

problem-11:

Write code to remove the duplicate characters in a string without using any additional buffer. 
One or two additional variables are fine. An extra copy of the array is not.

Input : one string 
output : one string  

Input : AXYZYZXB

Output : AXYZB

problem-12:

There is an array with every element repeated twice except one. Find that one element?

Input : Line 1: number of test case 
           Line 2: case 1: array length 
           Line 3: array values
        
Output : Number of unique value in given array for all test case 

Example :

Input : 
2
7
[1,1,5,5,7,7,8]
11
[1,1,2,99,2,3,3,4,4,5,5]

Output :
8
99

problem-13:

You have given one array you need to rearrange array in alternating positive and negative number.

Example :

Input : {5,4,9,2,-2,-4,1,-3}

Output : {-2,5,-4,4,-3,9,2,1}

problem-14:

Find the cube of the number by using recursion. 

Input : 2
Output : 8

problem-15:

Your task is pretty simple , given a string S , find the total count of numbers present in the string.

Input

The first line contains T , the number of test cases. The first line of each and every testcase will contain a integer N , the length of the string . The second line of each and every test case will contain a string S of length N.

Output

For each and every testcase , output the total count of numbers present in the string.

Example :

Input :
1
26
sadw96aeafae4awdw2wd100awd
Ouput :
4

problem-16:

Mighty is afraid of binary array. So he needs your help to complete task.

Task :
You will have one array consisting of only binary values (0,1). You can change only one bit (0 to 1 or 1 to 0) and this operation can be perform just one time. Using that one change you need to find the maximum values you can get from the array and give position of bit that gives the maximum value.

Example : 
Total numbers present in array : 3
1,0,0
Now you can change one value. 
so 1,0,1 so it's value = 5.
(4,2,1) ==> (1,0,1) so (4,0,1) => 5 
now changing other bit for same example 
1,1,0 => so it's value = 6
(4,2,1) ==> (1,1,0) so (4,2,0) => 6

Case 1:
Input:
3
1,0,0
Output :
6 , 1 
Since by changing one bit we get maximum value is 6 and the index of that bit is 
Values = >1,0,0
Indexs  => 0,1,2 
So 1



