### Regular Expression summary

### Chapter 1 

#### Summary  of Metacharacter 

Metacharacter|Name|Matches
-------------|-------------|---------
.|dot|any one character 
[ ...] |character class| any character listed 
[^...] |negated character class  | any character not listed
^|caret | the position at the start of the line
$|dollar | the position at the end of the line
\\<| backslash less-than | the position at the start of the word
\\>|backslash greater-than | the position at the end of the word (not support by egrep) 
\| | or,bar | match either expression 

>
- The rules about which characters are and aren’t metacharacters (and exactly
what they mean) are dif ferent inside a character class.

#### Summary of  quantifier repetation metacharacter 

 |Minimum required| Maximum to try| Meaning|
 ---|----|----|---
 ?| none | 1 | one allowed;none required ( one optional) 
 *| none | no limit| unlimited allowed| none required (any amount ok) 
 +| 1 | no limit| unlimited allowed | one required (at least one) 
 {min,max}| min|max| min required;max allowed


#### lookaround 

Type | Regex | Successful if 
------------ | -------------| ----------
Positive Lookbehind | (?<=...) | successful if can match to the left 
Negative lookbehind  | (?<!...)| successful if can not match to the left
Positive Lookahead | (?=...) | successful if can match to the right 
Negative lookahead | (?!...) | successful if can not match to the right 
