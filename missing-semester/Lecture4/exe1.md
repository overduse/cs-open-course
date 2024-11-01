# RegexOne

[Regex Website](https://regexone.com/)

## Tutorial Part

### Exercise 1

> Go ahead and try writing a pattern that matches all three rows, **it may be as simple as the common letters on each line**.
> 
> **Exercise 1**: Matching Characters
> | Task | Text |
> | --- | --- |
> | Match | abcdefg |
> | Match | abcde |
> | Match | abc |

SOLUTION: 'abc' or '\w{3}' or '\w*'


> Below are a few more lines of text containing digits. Try writing a pattern that matches all the digits in the strings below, and notice how your pattern matches **anywhere within the string**, not just starting at the first character. We will learn how to control this in a later lesson.
>
> **Exercise 1.5**: Matching Digits
> | Task | Text |
> | --- | --- |
> | Match | abc123xyz |
> | Match | define "123" |
> | Match | var g = 123; |

SOLUTION: '123' or '\d\d\d' or '\d{3}'


### Exercise 2

> Below are a couple strings with varying characters but the same length. Try to write a single pattern that can match the first three strings, but not the last (to be skipped). You may find that you will have to escape the dot metacharacter to match the period in some of the lines.
>
> **Exercise 2**: Matching With Wildcards
> | Task | Text |
> | ---- | ---- |
> | Match | cat. |
> | Match | 896. |
> | Match | ?=+. |
> | Skip | abc1 |

SOLUTION: '.*\.' , '...\.' and '.+\.' it's also okay.


### Exercise 3

> Below are a couple lines, where we only want to match the first three strings, but not the last three strings. Notice how we can't avoid matching the last three strings if we use the dot, but have to specifically define what letters to match using the notation above.
>
> **Exercise 3**: matching Characters
> | Task | Text |
> | ---- | ---- |
> | Match | can |
> | Match | man |
> | Match | fan |
> | Skip | dan |
> | Skip | ran |
> | Skip | pan |

SOLUTION: '[cmf]an' or '[^drp]an'


### Exercise 4

> With the strings below, try writing a pattern that matches only the live animals (hog, dog, but not bog). Notice how most patterns of this type can also be written using the technique from the last lesson as they are really two sides of the same coin. By having both choices, you can decide which one is easier to write and understand when composing your own patterns.
>
> **Exercise 4:** Excluding Characters
> | Task | Text |
> | ---- | ---- |
> | Match | hog |
> | Match | dog |
> | Skip | bog |

*SOLUTION*: '[hd]og' or '[^b]og'


### Exercise 5

> In the exercise below, notice how all the match and skip lines have a pattern, and use the bracket notation to match or skip each character from each line. Be aware that patterns are **case sensitive** and **a-z differs** from **A-Z** in terms of the characters it matches (lower vs upper case).
>
> **Exercise 5:** Matching Characters Ranges
> | Task | Text |
> | ---- | ---- |
> | Match | Ana |
> | Match | Bob |
> | Match | Cpc |
> | Skip | aax |
> | Skip | bby |
> | Skip | ccz |

SOLUTION: '[A=C][n-p][a-c]'


### Exercise 6

> In the lines below, the last string with only one z isn't what we would consider a proper spelling of the slang "wazzup?". Try writing a pattern that matches only the first two spellings by using the curly brace notation above.
>
> **Exercise 6:** Matching Repeated Characters
> | Task | Text |
> | ---- | ---- |
> | Match | wazzzzzup |
> | Match | wazzzup |
> | Skip | wazup |

SOLUTION: 'waz{3,5}up'


### Exercise 7

> Below are a few simple strings that you can match using both the star and plus metacharacters.
>
> **Exercise 7:** Matching Repeated Characters
> | Task | Text |
> | ---- | ---- |
> | Match | aaaabcc |
> | Match | aabbbbc |
> | Match | aacc |
> | Skip | a |

SOLUTION: 'aa+b*c*' , 'a(2,4)b(0,4)c(1,2)'


### Exercise 8

> In the strings below, notice how the the plurality of the word "file" depends on the number of files found. Try writing a pattern that uses the optionality metacharacter to match only the lines where one or more files were found.
>
> **Exercise 8:** Matching Optional Characters
> | Task | Text |
> | ---- | ---- |
> | Match | 1 file found? |
> | Match | 2 files found? |
> | Match | 24 files found?|
> | Skip | No files found. |

SOLUTION: '^\d+ files? found\?'


### Exercise 9

> In the strings below, you'll find that the content of each line is indented by some whitespace from the index of the line (**the number is a part of the text to match**). Try writing a pattern that can match each line containing whitespace characters between the number and the content. Notice that the whitespace characters are just like any other character and the special metacharacters like the star and the plus can be used as well.
>
> **Exercise 9:** Matching whitespaces
> | Task | Text |
> | ---- | ---- |
> | Match | 1.&emsp; abc |
> | Match | 2. &emsp;&emsp;abc |
> | Match | 3.&emsp;&emsp;&emsp;&emsp;abc |
> | Skip | 4.abc |

SOLUTION: '\d\.\s+abc'


### Exercise 10

> Note that this is different than the hat used inside a set of bracket **[^...]** for excluding characters, which can be confusing when reading regular expressions.
>
> Try to match each of the strings below using these new special characters.
>
> **Exercise 10:** Matching lines
> | Task | Text |
> | ---- | ---- |
> | Match | Mission: successful |
> | Skip | Last Mission: unsuccessful |
> | Skip | Next Mission: successful upon capture of target |

SOLUTION: '^Mission: successful$'


### Exercise 11

> Go ahead and try to use this to write a regular expression that matches only the filenames (not including extension) of the PDF files below.
>
> **Exercise 11:** Matching Groups
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | file_record_transcript.pdf | `file_record_transcript` |
> | Capture | file_07241999.pdf | `file_07241999` |
> | Skip | testfile_fake.pdf.tmp | None |

SOLUTION: '(^file_.*)\.pdf$'


### Exercise 12

> For the following strings, write an expression that matches **and captures** both the full date, as well as the year of the date.
>
> **Exercise 12:** Matching Nested Groups
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | Jan 1987 | `Jan 1987` `1987` |
> | Capture | May 1969 | `May 1969` `1969` |
> | Capture | Aug 2011 | `Aug 2011` `2011` |

SOLUTION: '(\w+ (\d+))'


### Exercise 13

> Below are a couple different common display resolutions, try to capture the width and height of each display.
>
> **Exercise 13:** Matching Nested Groups
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | 1280x720 | `1280` `720`|
> | Capture | 1920x1600 | `1920` `1600`|
> | Capture | 1024x768 | `1024` `768`|

SOLUTION: '(\d+)x(\d+)'


### Exercise 14

> Go ahead and try writing a conditional pattern that matches only the lines with small fuzzy creatures below.
>
> **Exercise 14:** Matching Conditional Text
> | Task | Text |
> | ---- | ---- |
> | Match | I love cats |
> | Match | I love dogs|
> | Skip | I love logs |
> | Skip | I love cogs |

SOLUTION: 'I love (cat|dog)s' or 'I love (cats|dogs)'


### Exercise 15

> Below are a number of different strings, try out the different types of metacharacters or anything we've learned in the previous lessons and continue on when you are ready.
>
> **Exercise 15:** Matching Other special Characters
> | Task | Text |
> | ---- | ---- |
> | Match | The quick brown fox jumps over the lazy dog. |
> | Match | There were 614 instances of students getting 90.0% or above. |
> | Match | The FCC had to censor the network for saying &$#*@! |

SOLUTION: '.*' (given solution)


## Practice Part

### Problem 1

> Below are a few different formats of numbers that you might encounter. Notice how you will have to match the decimal point itself and not an arbitrary character using the dot metacharacter. If you are having trouble skipping the last number, notice how that number ends the line compared to the rest.
> **Exercise 1:** Matching Numbers
> | Task | Text |
> | ---- | ---- |
> | Match | 3.14529 |
> | Match | -255.34 |
> | Match | 128 |
> | Match | 1.9e10 |
> | Match | 123,340.00 |
> | Skip | 720p |

SOLUTION: '^-?\d+(,\d+)*(\.\d+(e\d+)?)?$'


### Problem 2

> Below are a few phone numbers that you might encounter when using real data, write a single regular expressions that matches the number and captures the proper area code.
>
> **Exercise 2:** Matching Phone Numbers
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | 415-555-1234 | `415` |
> | Capture | 650-555-2345 | `650` |
> | Capture | (416)555-3456 | `416` |
> | Capture | 202 555 4567 | `202` |
> | Capture | 4035555678 | `403` |
> | Capture | 1 416 555 9292 | `416` |

SOLUTION: '(\d{3})' or '1?[\s-]?\(?R\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}'


### Problem 3

> Below are a few common emails, in this example, try to capture the name of the email, excluding the filter (+ character and afterwards) and domain (@ character and afterwards).
>
> **Exercise 3:** Matching Emails
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | tom@hogwarts.com | `tom` |
> | Capture | tom.riddle@hogwarts.com | `tom.riddle` |
> | Capture | tom.riddle+regexone@hogwarts.com | `tom.riddle` |
> | Capture | tom@hogwarts.eu.com | `tom` |
> | Capture | potter@hogwarts.com | `potter` |
> | Capture | harry@hogwarts.com | `harry` |
> | Capture | hermione+regexone@hogwarts.com | `hermione` |

SOLUTION: '^(.*?)[@+]' or '^(\w*)'


### Problem 4

> Go ahead and write regular expressions for the following examples.
>
> Exercise 4: Capturing HTML Tags
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | <a>This is a link</a> | `a` |
> | Capture | <a href='https://regexone.com'>Link</a> | `a` |
> | Capture | <div class='test_style'>Test</div> | `div` |
> | Capture | <div>Hello <span>world</span></div> | `div` |

SOLUTION: '<(\w+)' or '^<(\w*)\b'


### Problem 5

> In this simple example, extract the filenames and extension types of only image files (not including temporary files for images currently being edited). Image files are defined as **.jpg**,**.png**, and **.gif**.
>
> **Exercise 5:** Capturing Filename Data
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Skip | .bash_profile | None |
> | Skip | workspace.doc | None |
> | Capture | img0912.jpg | `img0912` `jpg` |
> | Capture | updated_img0912.png | `updated_img0912` `png` |
> | Skip | documentation.html | None |
> | Capture | favicon.gif | 'favicon' 'gif' |
> | Skip  | img0912.jpg.tmp | None |
> | Skip  | access.lock | None |

SOLUTION: '^(\w+)\.(jpg|png|gif)$' 


### Problem 6

> Write a simple regular expression to capture the content of each line, without the extra whitespace.
>
> **Exercise 6:** Matching lines
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | &emsp;&emsp;The quick brown fox...| The quick brown fox... |
> | Capture | &nbsp;&nbsp;jumps over the lazy dog. | jumps over the lazy dog. |

SOLUTION: '^\s*(.+)\s*$'


### Problem 7

> **Exercise 7:** Extracting information from a log file
>
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Skip | W/dalvikvm( 1553):threadid=1:uncaught exception | None |
> | Skip | E/( 1553):FATAL EXCEPTION:main | None |
> | Skip | E/( 1553):java.lang.StringIndexOutOfBoundsException | None |
> | Capture | E/( 1553): at widget.List.makeView(ListView.java:1727) | `makeView` `ListView.java` `1727` |
> | Capture | E/( 1553): at widget.List.fillDown(ListView.java:652)| `fillDown` `ListView.java` `652` |
> | Capture | E/( 1553): at widget.List.fillFrom(ListView.java:709)| `fillFrom` `ListView.java` `709` |

SOLUTION: '(\w+)\(([\w\.]+):(\d+)\)'


### Problem 8

> **Exercise 8:** Extracting Data From URLs
>
> | Task | Text | Capture Groups |
> | ---- | ---- | -------------- |
> | Capture | ftp://file_server.com:21/top_secret/life_changing_plans.pdf | `ftp` `file_server.com` `21` |
> | Capture | https://regexone.com/lesson/introduction#section | `https` `regexone.com` |
> | Capture | file://localhost:4040/zip_file | `file` `localhost` `4040` |
> | Capture | https://s3cur3-server.com:9999/ | `https` `s3cur3-server` `9999` |
> | Capture | market://search/angry%20birds | `market` `search` |

SOLUTION: '^(\w+)://([\w\.\-]+)(:(\d+)?)'
