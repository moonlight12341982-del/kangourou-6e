Last login: Sat Jan 17 17:48:17 on console

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
FRPARMAC0036980:~ mbachir$ mkdir programation
FRPARMAC0036980:~ mbachir$ cd programation/
FRPARMAC0036980:programation mbachir$ vi calculatrice.py

[1]+  Stopped                 vi calculatrice.py
FRPARMAC0036980:programation mbachir$ vi calculatrice.py
FRPARMAC0036980:programation mbachir$ vi calculatrice.py
FRPARMAC0036980:programation mbachir$ vi calculatrice.py
FRPARMAC0036980:programation mbachir$ vi calculatrice.py
FRPARMAC0036980:programation mbachir$ 
FRPARMAC0036980:programation mbachir$ ls -la
total 32
drwxr-xr-x   4 mbachir  staff    128 22 jan 19:05 .
drwxr-xr-x+ 33 mbachir  staff   1056 22 jan 19:05 ..
-rw-------   1 mbachir  staff  12288 22 jan 19:04 .calculatrice.py.swp
-rw-r--r--   1 mbachir  staff   2004 22 jan 19:05 calculatrice.py
FRPARMAC0036980:programation mbachir$ rm -f .calculatrice.py.swp 
FRPARMAC0036980:programation mbachir$ vi calculatrice.py
FRPARMAC0036980:programation mbachir$ python3 calculatrice.py 
  File "/Users/mbachir/programation/calculatrice.py", line 69
    print("Erre
               ^
SyntaxError: EOL while scanning string literal
FRPARMAC0036980:programation mbachir$ vi calculatrice.py
FRPARMAC0036980:programation mbachir$ vi calculatrice.py
FRPARMAC0036980:programation mbachir$ python3 calculatrice.py 

=== CALCULATRICE ===
1) Addition (+)
2) Soustraction (-)
3) Multiplication (*)
4) Division (/)
5) Calculer une expression (ex: 2*(3+4)/5)
0) Quitter
Ton choix : 1
Nombre A : 20
Nombre B : 50
Résultat : 20.0 + 50.0 = 70.0

=== CALCULATRICE ===
1) Addition (+)
2) Soustraction (-)
3) Multiplication (*)
4) Division (/)
5) Calculer une expression (ex: 2*(3+4)/5)
0) Quitter
Ton choix : 2
Nombre A : 15
Nombre B : 7
Résultat : 15.0 - 7.0 = 8.0

=== CALCULATRICE ===
1) Addition (+)
2) Soustraction (-)
3) Multiplication (*)
4) Division (/)
5) Calculer une expression (ex: 2*(3+4)/5)
0) Quitter
Ton choix : 5
Expression : 4+5*3
Résultat : 19.0

=== CALCULATRICE ===
1) Addition (+)
2) Soustraction (-)
3) Multiplication (*)
4) Division (/)
5) Calculer une expression (ex: 2*(3+4)/5)
0) Quitter
Ton choix : 0
Au revoir !
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
[12, 16, 18, 20]
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
[12, 16, 18, 20]
20
(10, 20, 15)
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{1, 2, 3, 4}
{1, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 32, in <module>
    nombres.remove(1)
KeyError: 1
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
P
PYTHON
Jython
P
python
Python
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
P
PYTHON
Jython
python
Python
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
P
PYTHON
Jython
python
P0thon
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
deque(['A', 'B', 'C'])
position 1 A
position 2 B
P
PYTHON
Jython
python
P0thon
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
deque(['A', 'B', 'C'])
position 1 A
deque(['B', 'C'])
position 2 B
deque(['C'])
P
PYTHON
Jython
python
P0thon
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
pile [1, 2, 3]
3
[1, 2]
deque(['A', 'B', 'C'])
position 1 A
deque(['B', 'C'])
position 2 B
deque(['C'])
P
PYTHON
Jython
python
P0thon
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
pile [1, 2, 3]
3
[1, 2]
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 16, in <module>
    test = deque()
NameError: name 'deque' is not defined
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
  File "/Users/mbachir/programation/test.py", line 1
    liste = list (input("Entrer les nombre :").split()))
                                                       ^
SyntaxError: unmatched ')'
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Entrer les nombre :orange pomme pomme banane
['orange', 'pomme', 'pomme', 'banane']
pile [1, 2, 3]
3
[1, 2]
deque(['A', 'B', 'C'])
position 1 A
deque(['B', 'C'])
position 2 B
deque(['C'])
P
PYTHON
Jython
python
P0thon
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
orange test café lait orange 
['orange', 'test', 'café', 'lait', 'orange']
pile [1, 2, 3]
3
[1, 2]
deque(['A', 'B', 'C'])
position 1 A
deque(['B', 'C'])
position 2 B
deque(['C'])
P
PYTHON
Jython
python
P0thon
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donner votre listelait objet cafe test
['lait', 'objet', 'cafe', 'test']
pile [1, 2, 3]
3
[1, 2]
deque(['A', 'B', 'C'])
position 1 A
deque(['B', 'C'])
position 2 B
deque(['C'])
P
PYTHON
Jython
python
P0thon
12
la liste des note [12, 16, 18, 20]
la coordonnes a la position 1 est 20
(10, 20, 15)
Ali
{'nom': 'Ali', 'age': 20, 'note': 17, 'classe': 'L1'}
{2, 3, 4, 6}
{2, 3, 4, 5}
{3}
{1, 2, 3, 4, 5}
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
  File "/Users/mbachir/programation/test.py", line 13
    /*
    ^
SyntaxError: invalid syntax
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matiere math francais anglais
['math', 'francais', 'anglais']
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 6, in <module>
    notes=list(input ("donner les notes pour la matiere", matiere[x]).split())
TypeError: list indices must be integers or slices, not str
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matieremath francais anglais
['math', 'francais', 'anglais']
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 5, in <module>
    for x in len(matiere) :
TypeError: 'int' object is not iterable
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matieremath francais
['math', 'francais']
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 7, in <module>
    notes=list(input ("donner les notes pour la matiere", matiere[x]).split())
TypeError: list indices must be integers or slices, not str
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matieremath anglais
['math', 'anglais']
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 7, in <module>
    notes=list(input ("donner les notes pour la matiere", matiere[x]).split())
TypeError: list indices must be integers or slices, not str
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matieremath physic
['math', 'physic']
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 7, in <module>
    notes=list(input ("donner les notes pour la matiere", matiere[x]).split())
TypeError: list indices must be integers or slices, not str
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matieremath physic
['math', 'physic']
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 7, in <module>
    notes=list(input ("donner les notes pour la matiere", matiere[i]).split())
TypeError: input expected at most 1 argument, got 2
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matieremath physic
['math', 'physic']
donner les notes pour la matiere {matiere[i]}: 20 19
donner les notes pour la matiere {matiere[i]}: 18 19
2
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 13, in <module>
    print ("la moyenne de toutes les matieres est ", sum(moyenne)/len(moyenne) ) 
ZeroDivisionError: division by zero
FRPARMAC0036980:programation mbachir$ vi test.py
FRPARMAC0036980:programation mbachir$ python3 test.py 
Donnez vos matieremath
['math']
donner les notes pour la matiere {matiere[x]}: q
1
Traceback (most recent call last):
  File "/Users/mbachir/programation/test.py", line 13, in <module>
    print ("la moyenne de toutes les matieres est ", sum(moyenne)/len(moyenne) ) 
ZeroDivisionError: division by zero
FRPARMAC0036980:programation mbachir$ vi webscraping.py
FRPARMAC0036980:programation mbachir$ python webscraping.py
-bash: python: command not found
FRPARMAC0036980:programation mbachir$ python3 webscraping.py
Traceback (most recent call last):
  File "/Users/mbachir/programation/webscraping.py", line 1, in <module>
    from playwright.sync_api import sync_playwright
ModuleNotFoundError: No module named 'playwright'
FRPARMAC0036980:programation mbachir$ pip install playwright beautifulsoup4 pandas
-bash: pip: command not found
FRPARMAC0036980:programation mbachir$ pip install playwright beautifulsoup4 pandas 
-bash: pip: command not found
FRPARMAC0036980:programation mbachir$ pip3 install playwright beautifulsoup4 pandas 
Defaulting to user installation because normal site-packages is not writeable
Collecting playwright
  Downloading playwright-1.57.0-py3-none-macosx_11_0_universal2.whl.metadata (3.5 kB)
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
Collecting pandas
  Downloading pandas-2.3.3-cp39-cp39-macosx_10_9_x86_64.whl.metadata (91 kB)
Collecting pyee<14,>=13 (from playwright)
  Downloading pyee-13.0.0-py3-none-any.whl.metadata (2.9 kB)
Collecting greenlet<4.0.0,>=3.1.1 (from playwright)
  Downloading greenlet-3.2.4-cp39-cp39-macosx_11_0_universal2.whl.metadata (4.1 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4)
  Downloading soupsieve-2.8.3-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: typing-extensions>=4.0.0 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from beautifulsoup4) (4.12.2)
Collecting numpy>=1.22.4 (from pandas)
  Downloading numpy-2.0.2-cp39-cp39-macosx_14_0_x86_64.whl.metadata (60 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from pandas) (2.9.0.post0)
Collecting pytz>=2020.1 (from pandas)
  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Requirement already satisfied: six>=1.5 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas) (1.15.0)
Downloading playwright-1.57.0-py3-none-macosx_11_0_universal2.whl (42.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.0/42.0 MB 84.0 MB/s eta 0:00:00
Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
Downloading pandas-2.3.3-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 71.2 MB/s eta 0:00:00
Downloading greenlet-3.2.4-cp39-cp39-macosx_11_0_universal2.whl (269 kB)
Downloading numpy-2.0.2-cp39-cp39-macosx_14_0_x86_64.whl (6.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 69.3 MB/s eta 0:00:00
Downloading pyee-13.0.0-py3-none-any.whl (15 kB)
Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading soupsieve-2.8.3-py3-none-any.whl (37 kB)
Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: pytz, tzdata, soupsieve, pyee, numpy, greenlet, playwright, pandas, beautifulsoup4
  WARNING: The scripts f2py and numpy-config are installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script playwright is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed beautifulsoup4-4.14.3 greenlet-3.2.4 numpy-2.0.2 pandas-2.3.3 playwright-1.57.0 pyee-13.0.0 pytz-2025.2 soupsieve-2.8.3 tzdata-2025.3

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
FRPARMAC0036980:programation mbachir$ playwright install
-bash: playwright: command not found
FRPARMAC0036980:programation mbachir$ python3 -m playwright install
Downloading Chromium 143.0.7499.4 (playwright build v1200) from https://cdn.playwright.dev/dbazure/download/playwright/builds/chromium/1200/chromium-mac.zip
(node:12813) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
167.8 MiB [====================] 100% 0.0s
Chromium 143.0.7499.4 (playwright build v1200) downloaded to /Users/mbachir/Library/Caches/ms-playwright/chromium-1200
Downloading Chromium Headless Shell 143.0.7499.4 (playwright build v1200) from https://cdn.playwright.dev/dbazure/download/playwright/builds/chromium/1200/chromium-headless-shell-mac.zip
(node:12873) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
93.8 MiB [====================] 100% 0.0s
Chromium Headless Shell 143.0.7499.4 (playwright build v1200) downloaded to /Users/mbachir/Library/Caches/ms-playwright/chromium_headless_shell-1200
Downloading Firefox 144.0.2 (playwright build v1497) from https://cdn.playwright.dev/dbazure/download/playwright/builds/firefox/1497/firefox-mac.zip
(node:12920) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
98.7 MiB [====================] 100% 0.0s
Firefox 144.0.2 (playwright build v1497) downloaded to /Users/mbachir/Library/Caches/ms-playwright/firefox-1497
Downloading Webkit 26.0 (playwright build v2227) from https://cdn.playwright.dev/dbazure/download/playwright/builds/webkit/2227/webkit-mac-15.zip
(node:12933) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
76.3 MiB [====================] 100% 0.0s
Webkit 26.0 (playwright build v2227) downloaded to /Users/mbachir/Library/Caches/ms-playwright/webkit-2227
Downloading FFMPEG playwright build v1011 from https://cdn.playwright.dev/dbazure/download/playwright/builds/ffmpeg/1011/ffmpeg-mac.zip
(node:13376) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
(Use `node --trace-deprecation ...` to show where the warning was created)
1.3 MiB [====================] 100% 0.0s
FFMPEG playwright build v1011 downloaded to /Users/mbachir/Library/Caches/ms-playwright/ffmpeg-1011
FRPARMAC0036980:programation mbachir$ python3 webscraping.py
Empty DataFrame
Columns: []
Index: []
Total: 0
FRPARMAC0036980:programation mbachir$ cp webscraping.py webscraping_imp.py 
FRPARMAC0036980:programation mbachir$ vi webscraping_imp.py 
FRPARMAC0036980:programation mbachir$ vi job_searching.py 
FRPARMAC0036980:programation mbachir$ python3 job_searching.py 
Page 1: 0 offres
Page 2: 0 offres
Page 3: 0 offres
Empty DataFrame
Columns: []
Index: []
CSV enregistré: jobs_chef_de_projet_integration.csv
FRPARMAC0036980:programation mbachir$ vi job_searching.py 
FRPARMAC0036980:programation mbachir$ rm -f job_searching.py 
FRPARMAC0036980:programation mbachir$ vi job_searching.py 
FRPARMAC0036980:programation mbachir$ python3 job_searching.py 
[DEBUG] Aucun lien /fr/jobs/ détecté. Fichiers: debug_page_1.png/.html
Page 1: 0 offres
Page 2: 0 offres
Page 3: 0 offres
CSV enregistré: jobs_chef_de_projet_integration.csv
Empty DataFrame
Columns: []
Index: []
FRPARMAC0036980:programation mbachir$ pip3 install nltk scikit-learn
Defaulting to user installation because normal site-packages is not writeable
Collecting nltk
  Downloading nltk-3.9.2-py3-none-any.whl.metadata (3.2 kB)
Collecting scikit-learn
  Downloading scikit_learn-1.6.1-cp39-cp39-macosx_10_9_x86_64.whl.metadata (31 kB)
Collecting click (from nltk)
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting joblib (from nltk)
  Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting regex>=2021.8.3 (from nltk)
  Downloading regex-2026.1.15-cp39-cp39-macosx_10_9_x86_64.whl.metadata (40 kB)
Collecting tqdm (from nltk)
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Requirement already satisfied: numpy>=1.19.5 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from scikit-learn) (2.0.2)
Collecting scipy>=1.6.0 (from scikit-learn)
  Downloading scipy-1.13.1-cp39-cp39-macosx_10_9_x86_64.whl.metadata (60 kB)
Collecting threadpoolctl>=3.1.0 (from scikit-learn)
  Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Downloading nltk-3.9.2-py3-none-any.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 29.7 MB/s eta 0:00:00
Downloading scikit_learn-1.6.1-cp39-cp39-macosx_10_9_x86_64.whl (12.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.1/12.1 MB 74.5 MB/s eta 0:00:00
Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
Downloading regex-2026.1.15-cp39-cp39-macosx_10_9_x86_64.whl (290 kB)
Downloading scipy-1.13.1-cp39-cp39-macosx_10_9_x86_64.whl (39.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 39.4/39.4 MB 67.1 MB/s eta 0:00:00
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
Installing collected packages: tqdm, threadpoolctl, scipy, regex, joblib, click, scikit-learn, nltk
  WARNING: The script tqdm is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script nltk is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed click-8.1.8 joblib-1.5.3 nltk-3.9.2 regex-2026.1.15 scikit-learn-1.6.1 scipy-1.13.1 threadpoolctl-3.6.0 tqdm-4.67.1

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
FRPARMAC0036980:programation mbachir$ vi chatbot.py
FRPARMAC0036980:programation mbachir$ python3 chatbot.py
^CTraceback (most recent call last):
  File "/Users/mbachir/programation/chatbot.py", line 3, in <module>
    import nltk
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/__init__.py", line 134, in <module>
    from nltk.collocations import *
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/collocations.py", line 36, in <module>
    from nltk.metrics import (
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/metrics/__init__.py", line 18, in <module>
    from nltk.metrics.association import (
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/metrics/association.py", line 26, in <module>
    from scipy.stats import fisher_exact
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/scipy/stats/__init__.py", line 606, in <module>
    from ._stats_py import *
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/scipy/stats/_stats_py.py", line 49, in <module>
    from . import distributions
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/scipy/stats/distributions.py", line 14, in <module>
    from ._levy_stable import levy_stable
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/scipy/stats/_levy_stable/__init__.py", line 17, in <module>
    from .levyst import Nolan
  File "<frozen importlib._bootstrap>", line 398, in parent
KeyboardInterrupt

FRPARMAC0036980:programation mbachir$ python3 chatbot.py
quel est l avantage d un chat bot
[nltk_data] Downloading package punkt to /Users/mbachir/nltk_data...
[nltk_data]   Unzipping tokenizers/punkt.zip.
[nltk_data] Downloading package wordnet to /Users/mbachir/nltk_data...
[nltk_data] Downloading package omw-1.4 to /Users/mbachir/nltk_data...
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/mbachir/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.
Traceback (most recent call last):
  File "/Users/mbachir/programation/chatbot.py", line 158, in <module>
    main()
  File "/Users/mbachir/programation/chatbot.py", line 145, in main
    bot = NLTKChatbot(INTENTS, threshold=0.35)
  File "/Users/mbachir/programation/chatbot.py", line 120, in __init__
    self.doc_matrix = self.vectorizer.fit_transform(self.documents)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 2104, in fit_transform
    X = super().fit_transform(raw_documents)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/base.py", line 1389, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 1376, in fit_transform
    vocabulary, X = self._count_vocab(raw_documents, self.fixed_vocabulary_)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 1263, in _count_vocab
    for feature in analyze(doc):
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 104, in _analyze
    doc = preprocessor(doc)
  File "/Users/mbachir/programation/chatbot.py", line 45, in normalize
    tokens = word_tokenize(text)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tokenize/__init__.py", line 142, in word_tokenize
    sentences = [text] if preserve_line else sent_tokenize(text, language)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tokenize/__init__.py", line 119, in sent_tokenize
    tokenizer = _get_punkt_tokenizer(language)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tokenize/__init__.py", line 105, in _get_punkt_tokenizer
    return PunktTokenizer(language)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tokenize/punkt.py", line 1744, in __init__
    self.load_lang(lang)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tokenize/punkt.py", line 1749, in load_lang
    lang_dir = find(f"tokenizers/punkt_tab/{lang}/")
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/data.py", line 579, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource punkt_tab not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('punkt_tab')
  
  For more information see: https://www.nltk.org/data.html

  Attempted to load tokenizers/punkt_tab/english/

  Searched in:
    - '/Users/mbachir/nltk_data'
    - '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/nltk_data'
    - '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/share/nltk_data'
    - '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

FRPARMAC0036980:programation mbachir$ quel est l avantage d un chat bot
-bash: quel: command not found
FRPARMAC0036980:programation mbachir$ vi chatbot.py
FRPARMAC0036980:programation mbachir$ python3 chatbot.py
q[nltk_data] Downloading package punkt to /Users/mbachir/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package punkt_tab to
[nltk_data]     /Users/mbachir/nltk_data...
u[nltk_data]   Unzipping tokenizers/punkt_tab.zip.
[nltk_data] Downloading package wordnet to /Users/mbachir/nltk_data...
e[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package omw-1.4 to /Users/mbachir/nltk_data...
[nltk_data]   Package omw-1.4 is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/mbachir/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
[nltk_data] Downloading package punkt to /Users/mbachir/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to /Users/mbachir/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package omw-1.4 to /Users/mbachir/nltk_data...
[nltk_data]   Package omw-1.4 is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/mbachir/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
Traceback (most recent call last):
  File "/Users/mbachir/programation/chatbot.py", line 164, in <module>
    main()
  File "/Users/mbachir/programation/chatbot.py", line 151, in main
    bot = NLTKChatbot(INTENTS, threshold=0.35)
  File "/Users/mbachir/programation/chatbot.py", line 126, in __init__
    self.doc_matrix = self.vectorizer.fit_transform(self.documents)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 2104, in fit_transform
    X = super().fit_transform(raw_documents)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/base.py", line 1389, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 1376, in fit_transform
    vocabulary, X = self._count_vocab(raw_documents, self.fixed_vocabulary_)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 1263, in _count_vocab
    for feature in analyze(doc):
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/sklearn/feature_extraction/text.py", line 104, in _analyze
    doc = preprocessor(doc)
  File "/Users/mbachir/programation/chatbot.py", line 52, in normalize
    tags = pos_tag(tokens)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tag/__init__.py", line 168, in pos_tag
    tagger = _get_tagger(lang)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tag/__init__.py", line 110, in _get_tagger
    tagger = PerceptronTagger()
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tag/perceptron.py", line 180, in __init__
    self.load_from_json(lang, loc)
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/tag/perceptron.py", line 277, in load_from_json
    loc = find(f"taggers/averaged_perceptron_tagger_{lang}")
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/nltk/data.py", line 579, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource averaged_perceptron_tagger_eng not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('averaged_perceptron_tagger_eng')
  
  For more information see: https://www.nltk.org/data.html

  Attempted to load taggers/averaged_perceptron_tagger_eng

  Searched in:
    - '/Users/mbachir/nltk_data'
    - '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/nltk_data'
    - '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/share/nltk_data'
    - '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

FRPARMAC0036980:programation mbachir$ vi chatbot.py
FRPARMAC0036980:programation mbachir$ python3 chatbot.py
[nltk_data] Downloading package punkt to /Users/mbachir/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package punkt_tab to
[nltk_data]     /Users/mbachir/nltk_data...
[nltk_data]   Package punkt_tab is already up-to-date!
[nltk_data] Downloading package wordnet to /Users/mbachir/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package omw-1.4 to /Users/mbachir/nltk_data...
[nltk_data]   Package omw-1.4 is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger_eng to
[nltk_data]     /Users/mbachir/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger_eng.zip.
[nltk_data] Downloading package punkt to /Users/mbachir/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to /Users/mbachir/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package omw-1.4 to /Users/mbachir/nltk_data...
[nltk_data]   Package omw-1.4 is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/mbachir/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
NLTK-Bot : Salut ! (tape 'quit' pour quitter)
Toi : quel est ta fonction
NLTK-Bot : Pas de souci 😊
Toi : c'est quoi le role du chatbot
NLTK-Bot : On peut m’appeler NLTK-Bot !
Toi : comment tu peux m aider 
NLTK-Bot : On peut m’appeler NLTK-Bot !
Toi : ^CTraceback (most recent call last):
  File "/Users/mbachir/programation/chatbot.py", line 174, in <module>
    main()
  File "/Users/mbachir/programation/chatbot.py", line 165, in main
    msg = input("Toi : ")
KeyboardInterrupt

FRPARMAC0036980:programation mbachir$ pip3 install tensorflow
Defaulting to user installation because normal site-packages is not writeable
Collecting tensorflow
  Downloading tensorflow-2.16.2-cp39-cp39-macosx_10_15_x86_64.whl.metadata (4.1 kB)
Collecting absl-py>=1.0.0 (from tensorflow)
  Downloading absl_py-2.3.1-py3-none-any.whl.metadata (3.3 kB)
Collecting astunparse>=1.6.0 (from tensorflow)
  Downloading astunparse-1.6.3-py2.py3-none-any.whl.metadata (4.4 kB)
Collecting flatbuffers>=23.5.26 (from tensorflow)
  Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
Collecting gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 (from tensorflow)
  Downloading gast-0.7.0-py3-none-any.whl.metadata (1.5 kB)
Collecting google-pasta>=0.1.1 (from tensorflow)
  Downloading google_pasta-0.2.0-py3-none-any.whl.metadata (814 bytes)
Collecting h5py>=3.10.0 (from tensorflow)
  Downloading h5py-3.14.0-cp39-cp39-macosx_10_9_x86_64.whl.metadata (2.7 kB)
Collecting libclang>=13.0.0 (from tensorflow)
  Downloading libclang-18.1.1-py2.py3-none-macosx_10_9_x86_64.whl.metadata (5.2 kB)
Collecting ml-dtypes~=0.3.1 (from tensorflow)
  Downloading ml_dtypes-0.3.2-cp39-cp39-macosx_10_9_universal2.whl.metadata (20 kB)
Collecting opt-einsum>=2.3.2 (from tensorflow)
  Downloading opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
Collecting packaging (from tensorflow)
  Downloading packaging-26.0-py3-none-any.whl.metadata (3.3 kB)
Collecting protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 (from tensorflow)
  Downloading protobuf-4.25.8-cp37-abi3-macosx_10_9_universal2.whl.metadata (541 bytes)
Collecting requests<3,>=2.21.0 (from tensorflow)
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Requirement already satisfied: setuptools in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from tensorflow) (58.0.4)
Requirement already satisfied: six>=1.12.0 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from tensorflow) (1.15.0)
Collecting termcolor>=1.1.0 (from tensorflow)
  Downloading termcolor-3.1.0-py3-none-any.whl.metadata (6.4 kB)
Requirement already satisfied: typing-extensions>=3.6.6 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from tensorflow) (4.12.2)
Collecting wrapt>=1.11.0 (from tensorflow)
  Downloading wrapt-2.0.1-cp39-cp39-macosx_10_9_x86_64.whl.metadata (9.0 kB)
Collecting grpcio<2.0,>=1.24.3 (from tensorflow)
  Downloading grpcio-1.76.0-cp39-cp39-macosx_11_0_universal2.whl.metadata (3.7 kB)
Collecting tensorboard<2.17,>=2.16 (from tensorflow)
  Downloading tensorboard-2.16.2-py3-none-any.whl.metadata (1.6 kB)
Collecting keras>=3.0.0 (from tensorflow)
  Downloading keras-3.10.0-py3-none-any.whl.metadata (6.0 kB)
Collecting tensorflow-io-gcs-filesystem>=0.23.1 (from tensorflow)
  Downloading tensorflow_io_gcs_filesystem-0.37.1-cp39-cp39-macosx_10_14_x86_64.whl.metadata (14 kB)
Collecting numpy<2.0.0,>=1.23.5 (from tensorflow)
  Downloading numpy-1.26.4-cp39-cp39-macosx_10_9_x86_64.whl.metadata (61 kB)
Requirement already satisfied: wheel<1.0,>=0.23.0 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from astunparse>=1.6.0->tensorflow) (0.37.0)
Collecting rich (from keras>=3.0.0->tensorflow)
  Downloading rich-14.2.0-py3-none-any.whl.metadata (18 kB)
Collecting namex (from keras>=3.0.0->tensorflow)
  Downloading namex-0.1.0-py3-none-any.whl.metadata (322 bytes)
Collecting optree (from keras>=3.0.0->tensorflow)
  Downloading optree-0.18.0-cp39-cp39-macosx_10_9_x86_64.whl.metadata (34 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.21.0->tensorflow)
  Downloading charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.21.0->tensorflow)
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.21.0->tensorflow)
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2017.4.17 (from requests<3,>=2.21.0->tensorflow)
  Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Collecting markdown>=2.6.8 (from tensorboard<2.17,>=2.16->tensorflow)
  Downloading markdown-3.9-py3-none-any.whl.metadata (5.1 kB)
Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard<2.17,>=2.16->tensorflow)
  Downloading tensorboard_data_server-0.7.2-py3-none-macosx_10_9_x86_64.whl.metadata (1.1 kB)
Collecting werkzeug>=1.0.1 (from tensorboard<2.17,>=2.16->tensorflow)
  Downloading werkzeug-3.1.5-py3-none-any.whl.metadata (4.0 kB)
Collecting importlib-metadata>=4.4 (from markdown>=2.6.8->tensorboard<2.17,>=2.16->tensorflow)
  Downloading importlib_metadata-8.7.1-py3-none-any.whl.metadata (4.7 kB)
Collecting markupsafe>=2.1.1 (from werkzeug>=1.0.1->tensorboard<2.17,>=2.16->tensorflow)
  Downloading markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl.metadata (2.7 kB)
Collecting markdown-it-py>=2.2.0 (from rich->keras>=3.0.0->tensorflow)
  Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich->keras>=3.0.0->tensorflow)
  Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting zipp>=3.20 (from importlib-metadata>=4.4->markdown>=2.6.8->tensorboard<2.17,>=2.16->tensorflow)
  Downloading zipp-3.23.0-py3-none-any.whl.metadata (3.6 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->keras>=3.0.0->tensorflow)
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Downloading tensorflow-2.16.2-cp39-cp39-macosx_10_15_x86_64.whl (259.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 259.5/259.5 MB 86.6 MB/s eta 0:00:00
Downloading absl_py-2.3.1-py3-none-any.whl (135 kB)
Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
Downloading gast-0.7.0-py3-none-any.whl (22 kB)
Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)
Downloading grpcio-1.76.0-cp39-cp39-macosx_11_0_universal2.whl (11.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.8/11.8 MB 74.8 MB/s eta 0:00:00
Downloading h5py-3.14.0-cp39-cp39-macosx_10_9_x86_64.whl (3.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 51.0 MB/s eta 0:00:00
Downloading keras-3.10.0-py3-none-any.whl (1.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 30.2 MB/s eta 0:00:00
Downloading libclang-18.1.1-py2.py3-none-macosx_10_9_x86_64.whl (26.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 26.5/26.5 MB 84.3 MB/s eta 0:00:00
Downloading ml_dtypes-0.3.2-cp39-cp39-macosx_10_9_universal2.whl (389 kB)
Downloading numpy-1.26.4-cp39-cp39-macosx_10_9_x86_64.whl (20.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.6/20.6 MB 84.6 MB/s eta 0:00:00
Downloading opt_einsum-3.4.0-py3-none-any.whl (71 kB)
Downloading protobuf-4.25.8-cp37-abi3-macosx_10_9_universal2.whl (394 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading tensorboard-2.16.2-py3-none-any.whl (5.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.5/5.5 MB 62.3 MB/s eta 0:00:00
Downloading tensorflow_io_gcs_filesystem-0.37.1-cp39-cp39-macosx_10_14_x86_64.whl (2.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 43.1 MB/s eta 0:00:00
Downloading termcolor-3.1.0-py3-none-any.whl (7.7 kB)
Downloading wrapt-2.0.1-cp39-cp39-macosx_10_9_x86_64.whl (60 kB)
Downloading packaging-26.0-py3-none-any.whl (74 kB)
Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
Downloading charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl (209 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading markdown-3.9-py3-none-any.whl (107 kB)
Downloading tensorboard_data_server-0.7.2-py3-none-macosx_10_9_x86_64.whl (4.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.8/4.8 MB 59.5 MB/s eta 0:00:00
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading werkzeug-3.1.5-py3-none-any.whl (225 kB)
Downloading namex-0.1.0-py3-none-any.whl (5.9 kB)
Downloading optree-0.18.0-cp39-cp39-macosx_10_9_x86_64.whl (353 kB)
Downloading rich-14.2.0-py3-none-any.whl (243 kB)
Downloading importlib_metadata-8.7.1-py3-none-any.whl (27 kB)
Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Downloading markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl (11 kB)
Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 27.1 MB/s eta 0:00:00
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Installing collected packages: namex, libclang, flatbuffers, zipp, wrapt, urllib3, termcolor, tensorflow-io-gcs-filesystem, tensorboard-data-server, pygments, protobuf, packaging, optree, opt-einsum, numpy, mdurl, markupsafe, idna, grpcio, google-pasta, gast, charset_normalizer, certifi, astunparse, absl-py, werkzeug, requests, ml-dtypes, markdown-it-py, importlib-metadata, h5py, rich, markdown, tensorboard, keras, tensorflow
  WARNING: The script pygmentize is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Attempting uninstall: numpy
    Found existing installation: numpy 2.0.2
    Uninstalling numpy-2.0.2:
      Successfully uninstalled numpy-2.0.2
  WARNING: The script f2py is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script normalizer is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script markdown-it is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script markdown_py is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script tensorboard is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts import_pb_to_tensorboard, saved_model_cli, tensorboard, tf_upgrade_v2, tflite_convert, toco and toco_from_protos are installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed absl-py-2.3.1 astunparse-1.6.3 certifi-2026.1.4 charset_normalizer-3.4.4 flatbuffers-25.12.19 gast-0.7.0 google-pasta-0.2.0 grpcio-1.76.0 h5py-3.14.0 idna-3.11 importlib-metadata-8.7.1 keras-3.10.0 libclang-18.1.1 markdown-3.9 markdown-it-py-3.0.0 markupsafe-3.0.3 mdurl-0.1.2 ml-dtypes-0.3.2 namex-0.1.0 numpy-1.26.4 opt-einsum-3.4.0 optree-0.18.0 packaging-26.0 protobuf-4.25.8 pygments-2.19.2 requests-2.32.5 rich-14.2.0 tensorboard-2.16.2 tensorboard-data-server-0.7.2 tensorflow-2.16.2 tensorflow-io-gcs-filesystem-0.37.1 termcolor-3.1.0 urllib3-2.6.3 werkzeug-3.1.5 wrapt-2.0.1 zipp-3.23.0

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
FRPARMAC0036980:programation mbachir$ vi jeu_donnees_mnist.py
FRPARMAC0036980:programation mbachir$ python3 jeu_donnees_mnist.py
2026-01-22 22:44:47.538096: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
/Users/mbachir/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11490434/11490434 ━━━━━━━━━━━━━━━━━━━━ 1s 0us/step 
(60000, 28, 28)
(60000,)
FRPARMAC0036980:programation mbachir$ vi morpion.py
FRPARMAC0036980:programation mbachir$ python3 morpion.py
=== MORPION (Tic-Tac-Toe) ===

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Joueur X, choisis une case (1-9) : 9

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | X

Joueur O, choisis une case (1-9) : 6

 1 | 2 | 3
---+---+---
 4 | 5 | O
---+---+---
 7 | 8 | X

Joueur X, choisis une case (1-9) : 4

 1 | 2 | 3
---+---+---
 X | 5 | O
---+---+---
 7 | 8 | X

Joueur O, choisis une case (1-9) : 9
Case déjà prise. Choisis une autre case.
Joueur O, choisis une case (1-9) : 3

 1 | 2 | O
---+---+---
 X | 5 | O
---+---+---
 7 | 8 | X

Joueur X, choisis une case (1-9) : 2

 1 | X | O
---+---+---
 X | 5 | O
---+---+---
 7 | 8 | X

Joueur O, choisis une case (1-9) : 1

 O | X | O
---+---+---
 X | 5 | O
---+---+---
 7 | 8 | X

Joueur X, choisis une case (1-9) : 7

 O | X | O
---+---+---
 X | 5 | O
---+---+---
 X | 8 | X

Joueur O, choisis une case (1-9) : 5

 O | X | O
---+---+---
 X | O | O
---+---+---
 X | 8 | X

Joueur X, choisis une case (1-9) : 8

 O | X | O
---+---+---
 X | O | O
---+---+---
 X | X | X

🎉 Joueur X a gagné !
Rejouer ? (o/n) : n
À bientôt !
FRPARMAC0036980:programation mbachir$ pip3 install pygame
Defaulting to user installation because normal site-packages is not writeable
Collecting pygame
  Downloading pygame-2.6.1-cp39-cp39-macosx_10_9_x86_64.whl.metadata (12 kB)
Downloading pygame-2.6.1-cp39-cp39-macosx_10_9_x86_64.whl (13.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.0/13.0 MB 16.1 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.6.1

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
FRPARMAC0036980:programation mbachir$ vi morpion2.py
FRPARMAC0036980:programation mbachir$ python3 morpion2.py
pygame 2.6.1 (SDL 2.28.4, Python 3.9.6)
Hello from the pygame community. https://www.pygame.org/contribute.html
FRPARMAC0036980:programation mbachir$ pip3 install streamlit yfinance pandas plotly
Defaulting to user installation because normal site-packages is not writeable
Collecting streamlit
  Downloading streamlit-1.50.0-py3-none-any.whl.metadata (9.5 kB)
Collecting yfinance
  Downloading yfinance-1.0-py2.py3-none-any.whl.metadata (6.0 kB)
Requirement already satisfied: pandas in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (2.3.3)
Collecting plotly
  Downloading plotly-6.5.2-py3-none-any.whl.metadata (8.5 kB)
Collecting altair!=5.4.0,!=5.4.1,<6,>=4.0 (from streamlit)
  Downloading altair-5.5.0-py3-none-any.whl.metadata (11 kB)
Collecting blinker<2,>=1.5.0 (from streamlit)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cachetools<7,>=4.0 (from streamlit)
  Downloading cachetools-6.2.4-py3-none-any.whl.metadata (5.6 kB)
Requirement already satisfied: click<9,>=7.0 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from streamlit) (8.1.8)
Requirement already satisfied: numpy<3,>=1.23 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from streamlit) (1.26.4)
Collecting packaging<26,>=20 (from streamlit)
  Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pillow<12,>=7.1.0 (from streamlit)
  Downloading pillow-11.3.0-cp39-cp39-macosx_10_10_x86_64.whl.metadata (9.0 kB)
Requirement already satisfied: protobuf<7,>=3.20 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from streamlit) (4.25.8)
Collecting pyarrow>=7.0 (from streamlit)
  Downloading pyarrow-21.0.0-cp39-cp39-macosx_12_0_x86_64.whl.metadata (3.3 kB)
Requirement already satisfied: requests<3,>=2.27 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from streamlit) (2.32.5)
Collecting tenacity<10,>=8.1.0 (from streamlit)
  Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
Collecting toml<2,>=0.10.1 (from streamlit)
  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from streamlit) (4.12.2)
Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)
  Downloading gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit)
  Downloading tornado-6.5.4-cp39-abi3-macosx_10_9_x86_64.whl.metadata (2.8 kB)
Collecting multitasking>=0.0.7 (from yfinance)
  Downloading multitasking-0.0.12.tar.gz (19 kB)
  Preparing metadata (setup.py) ... done
Collecting platformdirs>=2.0.0 (from yfinance)
  Downloading platformdirs-4.4.0-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: pytz>=2022.5 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from yfinance) (2025.2)
Collecting frozendict>=2.3.4 (from yfinance)
  Downloading frozendict-2.4.7-cp39-cp39-macosx_10_9_x86_64.whl.metadata (23 kB)
Collecting peewee>=3.16.2 (from yfinance)
  Downloading peewee-3.19.0-py3-none-any.whl.metadata (7.0 kB)
Requirement already satisfied: beautifulsoup4>=4.11.1 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from yfinance) (4.14.3)
Collecting curl_cffi<0.14,>=0.7 (from yfinance)
  Downloading curl_cffi-0.13.0-cp39-abi3-macosx_10_9_x86_64.whl.metadata (13 kB)
Collecting websockets>=13.0 (from yfinance)
  Downloading websockets-15.0.1-cp39-cp39-macosx_10_9_x86_64.whl.metadata (6.8 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: tzdata>=2022.7 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from pandas) (2025.3)
Collecting narwhals>=1.15.1 (from plotly)
  Downloading narwhals-2.15.0-py3-none-any.whl.metadata (13 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Downloading jsonschema-4.25.1-py3-none-any.whl.metadata (7.6 kB)
Requirement already satisfied: soupsieve>=1.6.1 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.8.3)
Collecting cffi>=1.12.0 (from curl_cffi<0.14,>=0.7->yfinance)
  Downloading cffi-2.0.0-cp39-cp39-macosx_10_13_x86_64.whl.metadata (2.6 kB)
Requirement already satisfied: certifi>=2024.2.2 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from curl_cffi<0.14,>=0.7->yfinance) (2026.1.4)
Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Requirement already satisfied: six>=1.5 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas) (1.15.0)
Requirement already satisfied: charset_normalizer<4,>=2 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (2.6.3)
Collecting pycparser (from cffi>=1.12.0->curl_cffi<0.14,>=0.7->yfinance)
  Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Downloading smmap-5.0.2-py3-none-any.whl.metadata (4.3 kB)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Downloading attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Downloading referencing-0.36.2-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.7.1 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Downloading rpds_py-0.27.1-cp39-cp39-macosx_10_12_x86_64.whl.metadata (4.2 kB)
Downloading streamlit-1.50.0-py3-none-any.whl (10.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.1 MB 67.7 MB/s eta 0:00:00
Downloading yfinance-1.0-py2.py3-none-any.whl (127 kB)
Downloading plotly-6.5.2-py3-none-any.whl (9.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.9/9.9 MB 72.0 MB/s eta 0:00:00
Downloading altair-5.5.0-py3-none-any.whl (731 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 731.2/731.2 kB 16.3 MB/s eta 0:00:00
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading cachetools-6.2.4-py3-none-any.whl (11 kB)
Downloading curl_cffi-0.13.0-cp39-abi3-macosx_10_9_x86_64.whl (5.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.7/5.7 MB 63.7 MB/s eta 0:00:00
Downloading frozendict-2.4.7-cp39-cp39-macosx_10_9_x86_64.whl (38 kB)
Downloading gitpython-3.1.46-py3-none-any.whl (208 kB)
Downloading narwhals-2.15.0-py3-none-any.whl (432 kB)
Downloading packaging-25.0-py3-none-any.whl (66 kB)
Downloading peewee-3.19.0-py3-none-any.whl (411 kB)
Downloading pillow-11.3.0-cp39-cp39-macosx_10_10_x86_64.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 64.2 MB/s eta 0:00:00
Downloading platformdirs-4.4.0-py3-none-any.whl (18 kB)
Downloading pyarrow-21.0.0-cp39-cp39-macosx_12_0_x86_64.whl (32.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.7/32.7 MB 86.0 MB/s eta 0:00:00
Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 61.4 MB/s eta 0:00:00
Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Downloading tornado-6.5.4-cp39-abi3-macosx_10_9_x86_64.whl (442 kB)
Downloading websockets-15.0.1-cp39-cp39-macosx_10_9_x86_64.whl (173 kB)
Downloading cffi-2.0.0-cp39-cp39-macosx_10_13_x86_64.whl (184 kB)
Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading jsonschema-4.25.1-py3-none-any.whl (90 kB)
Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading referencing-0.36.2-py3-none-any.whl (26 kB)
Downloading rpds_py-0.27.1-cp39-cp39-macosx_10_12_x86_64.whl (372 kB)
Downloading smmap-5.0.2-py3-none-any.whl (24 kB)
Downloading pycparser-2.23-py3-none-any.whl (118 kB)
Building wheels for collected packages: multitasking
  Building wheel for multitasking (setup.py) ... done
  Created wheel for multitasking: filename=multitasking-0.0.12-py3-none-any.whl size=15550 sha256=f023d738844a55544973fd6bf57bd583fc43c254c747d5ccf5b211f99fafeca7
  Stored in directory: /Users/mbachir/Library/Caches/pip/wheels/98/75/bc/9eaa3cdeaaca347bab26c7e83a7e2f365d82584d65a2d48e7a
Successfully built multitasking
Installing collected packages: peewee, multitasking, websockets, tornado, toml, tenacity, smmap, rpds-py, pycparser, pyarrow, platformdirs, pillow, packaging, narwhals, jinja2, frozendict, cachetools, blinker, attrs, referencing, pydeck, plotly, gitdb, cffi, jsonschema-specifications, gitpython, curl_cffi, yfinance, jsonschema, altair, streamlit
  WARNING: The script pwiz is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script websockets is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Attempting uninstall: packaging
    Found existing installation: packaging 26.0
    Uninstalling packaging-26.0:
      Successfully uninstalled packaging-26.0
  WARNING: The script plotly_get_chrome is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script sample is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script jsonschema is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script streamlit is installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed altair-5.5.0 attrs-25.4.0 blinker-1.9.0 cachetools-6.2.4 cffi-2.0.0 curl_cffi-0.13.0 frozendict-2.4.7 gitdb-4.0.12 gitpython-3.1.46 jinja2-3.1.6 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 multitasking-0.0.12 narwhals-2.15.0 packaging-25.0 peewee-3.19.0 pillow-11.3.0 platformdirs-4.4.0 plotly-6.5.2 pyarrow-21.0.0 pycparser-2.23 pydeck-0.9.1 referencing-0.36.2 rpds-py-0.27.1 smmap-5.0.2 streamlit-1.50.0 tenacity-9.1.2 toml-0.10.2 tornado-6.5.4 websockets-15.0.1 yfinance-1.0

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
FRPARMAC0036980:programation mbachir$ vi finance.py
FRPARMAC0036980:programation mbachir$ python3 finance.py
/Users/mbachir/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Traceback (most recent call last):
  File "/Users/mbachir/programation/finance.py", line 3, in <module>
    import yfinance as yf
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/yfinance/__init__.py", line 26, in <module>
    from .calendars import Calendars
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/yfinance/calendars.py", line 16, in <module>
    class CalendarQuery:
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/yfinance/calendars.py", line 33, in CalendarQuery
    def __init__(self, operator: str, operand: list[Any] | list["CalendarQuery"]):
TypeError: unsupported operand type(s) for |: 'types.GenericAlias' and 'types.GenericAlias'
FRPARMAC0036980:programation mbachir$ vi finance2.py
FRPARMAC0036980:programation mbachir$ python3 finance2.py
/Users/mbachir/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Traceback (most recent call last):
  File "/Users/mbachir/programation/finance2.py", line 3, in <module>
    import yfinance as yf
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/yfinance/__init__.py", line 26, in <module>
    from .calendars import Calendars
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/yfinance/calendars.py", line 16, in <module>
    class CalendarQuery:
  File "/Users/mbachir/Library/Python/3.9/lib/python/site-packages/yfinance/calendars.py", line 33, in CalendarQuery
    def __init__(self, operator: str, operand: list[Any] | list["CalendarQuery"]):
TypeError: unsupported operand type(s) for |: 'types.GenericAlias' and 'types.GenericAlias'
FRPARMAC0036980:programation mbachir$ vi data_regression.py
FRPARMAC0036980:programation mbachir$ python3 data_regression.py
[12.5]
16.499999999999993
FRPARMAC0036980:programation mbachir$ vi shop.sql
FRPARMAC0036980:programation mbachir$ sqlite3 shop.db < shop.sql
FRPARMAC0036980:programation mbachir$ ls
calculatrice.py				jobs_chef_de_projet_integration.csv
chatbot.py				morpion.py
data_regression.py			morpion2.py
debug_page_1.html			shop.db
debug_page_1.png			shop.sql
finance.py				test.py
finance2.py				webscraping_imp.py
jeu_donnees_mnist.py			webscraping.py
job_searching.py
FRPARMAC0036980:programation mbachir$ vi commande.sql
FRPARMAC0036980:programation mbachir$ vi commande.sql
FRPARMAC0036980:programation mbachir$ sqlite3 shop.db 
SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.
sqlite> .tables
orders
sqlite> SELECT
   ...>   order_date,
   ...>   SUM(visits)  AS visits,
   ...>   SUM(orders)  AS orders,
   ...>   SUM(revenue) AS revenue,
   ...>   ROUND(1.0 * SUM(orders) / SUM(visits), 4) AS conversion_rate,
   ...>   ROUND(1.0 * SUM(revenue) / SUM(orders), 2) AS aov
   ...> FROM orders
   ...> GROUP BY order_date
   ...> ORDER BY order_date;
2026-01-19|1660|76|7600.0|0.0458|100.0
2026-01-20|1760|83|8300.0|0.0472|100.0
2026-01-21|1740|79|7900.0|0.0454|100.0
2026-01-22|1745|63|6300.0|0.0361|100.0
2026-01-23|1745|60|6000.0|0.0344|100.0
sqlite> SELECT
   ...>   order_date,
   ...>   device,
   ...>   SUM(visits)  AS visits,
   ...>   SUM(orders)  AS orders,
   ...>   SUM(revenue) AS revenue,
   ...>   ROUND(1.0 * SUM(orders) / SUM(visits), 4) AS conversion_rate,
   ...>   ROUND(1.0 * SUM(revenue) / SUM(orders), 2) AS aov
   ...> FROM orders
   ...> GROUP BY order_date, device
   ...> ORDER BY order_date, device;
2026-01-19|desktop|900|53|5300.0|0.0589|100.0
2026-01-19|mobile|760|23|2300.0|0.0303|100.0
2026-01-20|desktop|970|57|5700.0|0.0588|100.0
2026-01-20|mobile|790|26|2600.0|0.0329|100.0
2026-01-21|desktop|930|54|5400.0|0.0581|100.0
2026-01-21|mobile|810|25|2500.0|0.0309|100.0
2026-01-22|desktop|915|45|4500.0|0.0492|100.0
2026-01-22|mobile|830|18|1800.0|0.0217|100.0
2026-01-23|desktop|885|43|4300.0|0.0486|100.0
2026-01-23|mobile|860|17|1700.0|0.0198|100.0
sqlite> SELECT
   ...>   device,
   ...>   CASE
   ...>     WHEN order_date <= '2026-01-21' THEN 'before'
   ...>     ELSE 'after'
   ...>   END AS period,
   ...>   SUM(visits)  AS visits,
   ...>   SUM(orders)  AS orders,
   ...>   SUM(revenue) AS revenue,
   ...>   ROUND(1.0 * SUM(orders) / SUM(visits), 4) AS conversion_rate,
   ...>   ROUND(1.0 * SUM(revenue) / SUM(orders), 2) AS aov
   ...> FROM orders
   ...> GROUP BY device, period
   ...> ORDER BY device, period;
desktop|after|1800|88|8800.0|0.0489|100.0
desktop|before|2800|164|16400.0|0.0586|100.0
mobile|after|1690|35|3500.0|0.0207|100.0
mobile|before|2360|74|7400.0|0.0314|100.0
sqlite> q
   ...> exit
   ...> quit
   ...> .quit
   ...> exit
   ...> .exit
   ...> ^D
Parse error: near "q": syntax error
  q exit quit .quit exit .exit
  ^--- error here
FRPARMAC0036980:programation mbachir$ sqlite3 shop.db 
SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.
sqlite> .tables
orders
sqlite> .exit
FRPARMAC0036980:programation mbachir$ vi calculKPI.py
FRPARMAC0036980:programation mbachir$ python3 calculKPI.py
  order_date  visits  orders  revenue  conversion_rate    aov
0 2026-01-19    1660      76   7600.0         0.045783  100.0
1 2026-01-20    1760      83   8300.0         0.047159  100.0
2 2026-01-21    1740      79   7900.0         0.045402  100.0
3 2026-01-22    1745      63   6300.0         0.036103  100.0
4 2026-01-23    1745      60   6000.0         0.034384  100.0
FRPARMAC0036980:programation mbachir$ vi calculKPI.py
FRPARMAC0036980:programation mbachir$ vi calculKPI.py
FRPARMAC0036980:programation mbachir$ python3 calculKPI.py
  order_date  visits  orders  revenue  conversion_rate    aov
0 2026-01-19    1660      76   7600.0         0.045783  100.0
1 2026-01-20    1760      83   8300.0         0.047159  100.0
2 2026-01-21    1740      79   7900.0         0.045402  100.0
3 2026-01-22    1745      63   6300.0         0.036103  100.0
4 2026-01-23    1745      60   6000.0         0.034384  100.0
  order_date   device  visits  orders  revenue  conversion_rate    aov
0 2026-01-19  desktop     900      53   5300.0         0.058889  100.0
1 2026-01-19   mobile     760      23   2300.0         0.030263  100.0
2 2026-01-20  desktop     970      57   5700.0         0.058763  100.0
3 2026-01-20   mobile     790      26   2600.0         0.032911  100.0
4 2026-01-21  desktop     930      54   5400.0         0.058065  100.0
5 2026-01-21   mobile     810      25   2500.0         0.030864  100.0
6 2026-01-22  desktop     915      45   4500.0         0.049180  100.0
7 2026-01-22   mobile     830      18   1800.0         0.021687  100.0
8 2026-01-23  desktop     885      43   4300.0         0.048588  100.0
9 2026-01-23   mobile     860      17   1700.0         0.019767  100.0
Traceback (most recent call last):
  File "/Users/mbachir/programation/calculKPI.py", line 27, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
FRPARMAC0036980:programation mbachir$ pip3 install matplotlib
Defaulting to user installation because normal site-packages is not writeable
Collecting matplotlib
  Downloading matplotlib-3.9.4-cp39-cp39-macosx_10_12_x86_64.whl.metadata (11 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Downloading contourpy-1.3.0-cp39-cp39-macosx_10_9_x86_64.whl.metadata (5.4 kB)
Collecting cycler>=0.10 (from matplotlib)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib)
  Downloading fonttools-4.60.2-cp39-cp39-macosx_10_9_x86_64.whl.metadata (113 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Downloading kiwisolver-1.4.7-cp39-cp39-macosx_10_9_x86_64.whl.metadata (6.3 kB)
Requirement already satisfied: numpy>=1.23 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from matplotlib) (1.26.4)
Requirement already satisfied: packaging>=20.0 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from matplotlib) (25.0)
Requirement already satisfied: pillow>=8 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from matplotlib) (11.3.0)
Collecting pyparsing>=2.3.1 (from matplotlib)
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Requirement already satisfied: python-dateutil>=2.7 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from matplotlib) (2.9.0.post0)
Collecting importlib-resources>=3.2.0 (from matplotlib)
  Downloading importlib_resources-6.5.2-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: zipp>=3.1.0 in /Users/mbachir/Library/Python/3.9/lib/python/site-packages (from importlib-resources>=3.2.0->matplotlib) (3.23.0)
Requirement already satisfied: six>=1.5 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from python-dateutil>=2.7->matplotlib) (1.15.0)
Downloading matplotlib-3.9.4-cp39-cp39-macosx_10_12_x86_64.whl (7.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 47.2 MB/s eta 0:00:00
Downloading contourpy-1.3.0-cp39-cp39-macosx_10_9_x86_64.whl (265 kB)
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.60.2-cp39-cp39-macosx_10_9_x86_64.whl (2.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 37.1 MB/s eta 0:00:00
Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Downloading kiwisolver-1.4.7-cp39-cp39-macosx_10_9_x86_64.whl (65 kB)
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Installing collected packages: pyparsing, kiwisolver, importlib-resources, fonttools, cycler, contourpy, matplotlib
  WARNING: The scripts fonttools, pyftmerge, pyftsubset and ttx are installed in '/Users/mbachir/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed contourpy-1.3.0 cycler-0.12.1 fonttools-4.60.2 importlib-resources-6.5.2 kiwisolver-1.4.7 matplotlib-3.9.4 pyparsing-3.3.2

[notice] A new release of pip is available: 24.3.1 -> 25.3
[notice] To update, run: /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
FRPARMAC0036980:programation mbachir$ python3 calculKPI.py
  order_date  visits  orders  revenue  conversion_rate    aov
0 2026-01-19    1660      76   7600.0         0.045783  100.0
1 2026-01-20    1760      83   8300.0         0.047159  100.0
2 2026-01-21    1740      79   7900.0         0.045402  100.0
3 2026-01-22    1745      63   6300.0         0.036103  100.0
4 2026-01-23    1745      60   6000.0         0.034384  100.0
  order_date   device  visits  orders  revenue  conversion_rate    aov
0 2026-01-19  desktop     900      53   5300.0         0.058889  100.0
1 2026-01-19   mobile     760      23   2300.0         0.030263  100.0
2 2026-01-20  desktop     970      57   5700.0         0.058763  100.0
3 2026-01-20   mobile     790      26   2600.0         0.032911  100.0
4 2026-01-21  desktop     930      54   5400.0         0.058065  100.0
5 2026-01-21   mobile     810      25   2500.0         0.030864  100.0
6 2026-01-22  desktop     915      45   4500.0         0.049180  100.0
7 2026-01-22   mobile     830      18   1800.0         0.021687  100.0
8 2026-01-23  desktop     885      43   4300.0         0.048588  100.0
9 2026-01-23   mobile     860      17   1700.0         0.019767  100.0
Matplotlib is building the font cache; this may take a moment.
FRPARMAC0036980:programation mbachir$ projet MVP
-bash: projet: command not found
FRPARMAC0036980:programation mbachir$ mkdir MVP_Project
FRPARMAC0036980:programation mbachir$ cd MVP_Project/
FRPARMAC0036980:MVP_Project mbachir$ python -m venv .venv
-bash: python: command not found
FRPARMAC0036980:MVP_Project mbachir$ source .venv/bin/activate  # Windows: .venv\Scripts\activate
-bash: .venv/bin/activate: No such file or directory
FRPARMAC0036980:MVP_Project mbachir$ pip install streamlit pymupdf python-docx pydantic
-bash: pip: command not found
FRPARMAC0036980:MVP_Project mbachir$ python3 -m venv .venv
FRPARMAC0036980:MVP_Project mbachir$ source .venv/bin/activate
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install streamlit pymupdf python-docx pydantic
^[[DCollecting streamlit
  Downloading streamlit-1.50.0-py3-none-any.whl (10.1 MB)
     |████████████████████████████████| 10.1 MB 14.7 MB/s 
^[[DCollecting pymupdf
  Downloading pymupdf-1.26.5-cp39-abi3-macosx_10_9_x86_64.whl (23.1 MB)
     |████████████████████████████████| 23.1 MB 28.3 MB/s 
Collecting python-docx
  Downloading python_docx-1.2.0-py3-none-any.whl (252 kB)
     |████████████████████████████████| 252 kB 62.7 MB/s 
Collecting pydantic
  Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
     |████████████████████████████████| 463 kB 66.5 MB/s 
Collecting click<9,>=7.0
  Downloading click-8.1.8-py3-none-any.whl (98 kB)
     |████████████████████████████████| 98 kB 22.2 MB/s 
Collecting pandas<3,>=1.4.0
  Downloading pandas-2.3.3-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
     |████████████████████████████████| 11.6 MB 21.6 MB/s 
Collecting toml<2,>=0.10.1
  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Collecting numpy<3,>=1.23
  Downloading numpy-2.0.2-cp39-cp39-macosx_14_0_x86_64.whl (6.9 MB)
     |████████████████████████████████| 6.9 MB 44.2 MB/s 
Collecting pillow<12,>=7.1.0
  Downloading pillow-11.3.0-cp39-cp39-macosx_10_10_x86_64.whl (5.3 MB)
     |████████████████████████████████| 5.3 MB 33.1 MB/s 
Collecting blinker<2,>=1.5.0
  Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting pyarrow>=7.0
  Downloading pyarrow-21.0.0-cp39-cp39-macosx_12_0_x86_64.whl (32.7 MB)
     |████████████████████████████████| 32.7 MB 36.2 MB/s 
Collecting requests<3,>=2.27
  Downloading requests-2.32.5-py3-none-any.whl (64 kB)
     |████████████████████████████████| 64 kB 7.3 MB/s 
Collecting packaging<26,>=20
  Downloading packaging-25.0-py3-none-any.whl (66 kB)
     |████████████████████████████████| 66 kB 12.6 MB/s 
Collecting cachetools<7,>=4.0
  Downloading cachetools-6.2.5-py3-none-any.whl (11 kB)
Collecting protobuf<7,>=3.20
  Downloading protobuf-6.33.4-cp39-abi3-macosx_10_9_universal2.whl (427 kB)
     |████████████████████████████████| 427 kB 65.2 MB/s 
Collecting gitpython!=3.1.19,<4,>=3.0.7
  Downloading gitpython-3.1.46-py3-none-any.whl (208 kB)
     |████████████████████████████████| 208 kB 74.0 MB/s 
Collecting tornado!=6.5.0,<7,>=6.0.3
  Downloading tornado-6.5.4-cp39-abi3-macosx_10_9_x86_64.whl (442 kB)
     |████████████████████████████████| 442 kB 69.9 MB/s 
Collecting altair!=5.4.0,!=5.4.1,<6,>=4.0
  Downloading altair-5.5.0-py3-none-any.whl (731 kB)
     |████████████████████████████████| 731 kB 68.9 MB/s 
Collecting typing-extensions<5,>=4.4.0
  Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
     |████████████████████████████████| 44 kB 6.1 MB/s 
Collecting tenacity<10,>=8.1.0
  Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
Collecting pydeck<1,>=0.8.0b4
  Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
     |████████████████████████████████| 6.9 MB 60.7 MB/s 
Collecting lxml>=3.1.0
  Downloading lxml-6.0.2-cp39-cp39-macosx_10_9_x86_64.whl (4.6 MB)
     |████████████████████████████████| 4.6 MB 71.0 MB/s 
Collecting pydantic-core==2.41.5
  Downloading pydantic_core-2.41.5-cp39-cp39-macosx_10_12_x86_64.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 28.7 MB/s 
Collecting annotated-types>=0.6.0
  Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Collecting typing-inspection>=0.4.2
  Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Collecting narwhals>=1.14.2
  Downloading narwhals-2.15.0-py3-none-any.whl (432 kB)
     |████████████████████████████████| 432 kB 58.1 MB/s 
Collecting jinja2
  Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
     |████████████████████████████████| 134 kB 37.6 MB/s 
Collecting jsonschema>=3.0
  Downloading jsonschema-4.25.1-py3-none-any.whl (90 kB)
     |████████████████████████████████| 90 kB 24.8 MB/s 
Collecting gitdb<5,>=4.0.1
  Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 4.8 MB/s 
Collecting smmap<6,>=3.0.1
  Downloading smmap-5.0.2-py3-none-any.whl (24 kB)
Collecting jsonschema-specifications>=2023.03.6
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Collecting rpds-py>=0.7.1
  Downloading rpds_py-0.27.1-cp39-cp39-macosx_10_12_x86_64.whl (372 kB)
     |████████████████████████████████| 372 kB 50.6 MB/s 
Collecting referencing>=0.28.4
  Downloading referencing-0.36.2-py3-none-any.whl (26 kB)
Collecting attrs>=22.2.0
  Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
     |████████████████████████████████| 67 kB 15.3 MB/s 
Collecting python-dateutil>=2.8.2
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting tzdata>=2022.7
  Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
     |████████████████████████████████| 348 kB 61.5 MB/s 
Collecting pytz>=2020.1
  Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
     |████████████████████████████████| 509 kB 58.3 MB/s 
Collecting MarkupSafe>=2.0
  Downloading markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl (11 kB)
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
     |████████████████████████████████| 131 kB 28.9 MB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
     |████████████████████████████████| 152 kB 49.4 MB/s 
Collecting idna<4,>=2.5
  Downloading idna-3.11-py3-none-any.whl (71 kB)
     |████████████████████████████████| 71 kB 14.7 MB/s 
Collecting charset_normalizer<4,>=2
  Downloading charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl (209 kB)
     |████████████████████████████████| 209 kB 57.9 MB/s 
Installing collected packages: typing-extensions, rpds-py, attrs, referencing, smmap, six, MarkupSafe, jsonschema-specifications, urllib3, tzdata, pytz, python-dateutil, packaging, numpy, narwhals, jsonschema, jinja2, idna, gitdb, charset-normalizer, certifi, typing-inspection, tornado, toml, tenacity, requests, pydeck, pydantic-core, pyarrow, protobuf, pillow, pandas, lxml, gitpython, click, cachetools, blinker, annotated-types, altair, streamlit, python-docx, pymupdf, pydantic
Successfully installed MarkupSafe-3.0.3 altair-5.5.0 annotated-types-0.7.0 attrs-25.4.0 blinker-1.9.0 cachetools-6.2.5 certifi-2026.1.4 charset-normalizer-3.4.4 click-8.1.8 gitdb-4.0.12 gitpython-3.1.46 idna-3.11 jinja2-3.1.6 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 lxml-6.0.2 narwhals-2.15.0 numpy-2.0.2 packaging-25.0 pandas-2.3.3 pillow-11.3.0 protobuf-6.33.4 pyarrow-21.0.0 pydantic-2.12.5 pydantic-core-2.41.5 pydeck-0.9.1 pymupdf-1.26.5 python-dateutil-2.9.0.post0 python-docx-1.2.0 pytz-2025.2 referencing-0.36.2 requests-2.32.5 rpds-py-0.27.1 six-1.17.0 smmap-5.0.2 streamlit-1.50.0 tenacity-9.1.2 toml-0.10.2 tornado-6.5.4 typing-extensions-4.15.0 typing-inspection-0.4.2 tzdata-2025.3 urllib3-2.6.3
WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
You should consider upgrading via the '/Users/mbachir/programation/MVP_Project/.venv/bin/python3 -m pip install --upgrade pip' command.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi app.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ str
streamlit      streamzip      stringdups     strip          
streamlit.cmd  streamzip5.34  strings        
(.venv) FRPARMAC0036980:MVP_Project mbachir$ streamlit run app.py

      👋 Welcome to Streamlit!

      If you'd like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email:  bmoonira@gmail.com
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.45:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
^C  Stopping...
(.venv) FRPARMAC0036980:MVP_Project mbachir$ ls
app.py	data.db
(.venv) FRPARMAC0036980:MVP_Project mbachir$ sqlite3 data.db 
SQLite version 3.43.2 2023-10-10 13:08:14
Enter ".help" for usage hints.
sqlite> .tables
candidate_profiles
sqlite> PRAGMA table_info(candidate_profiles);
0|id|INTEGER|0||1
1|created_at|TEXT|1||0
2|full_name|TEXT|0||0
3|email|TEXT|0||0
4|phone|TEXT|0||0
5|location|TEXT|0||0
6|skills_json|TEXT|1||0
7|raw_text|TEXT|1||0
sqlite> SELECT * FROM candidate_profiles 
   ...> 
   ...> 
   ...> .exit
   ...> .quit
   ...> ^CProgram interrupted.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ mv app.py old_app.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi app.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ streamlit run app.py 

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.45:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
^C  Stopping...
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install python-docx pypdf requests scikit-learn
Requirement already satisfied: python-docx in ./.venv/lib/python3.9/site-packages (1.2.0)
Collecting pypdf
  Downloading pypdf-6.6.2-py3-none-any.whl (329 kB)
     |████████████████████████████████| 329 kB 12.3 MB/s 
Requirement already satisfied: requests in ./.venv/lib/python3.9/site-packages (2.32.5)
Collecting scikit-learn
  Downloading scikit_learn-1.6.1-cp39-cp39-macosx_10_9_x86_64.whl (12.1 MB)
     |████████████████████████████████| 12.1 MB 40.9 MB/s 
Requirement already satisfied: typing_extensions>=4.9.0 in ./.venv/lib/python3.9/site-packages (from python-docx) (4.15.0)
Requirement already satisfied: lxml>=3.1.0 in ./.venv/lib/python3.9/site-packages (from python-docx) (6.0.2)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.9/site-packages (from requests) (2026.1.4)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.9/site-packages (from requests) (3.4.4)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.9/site-packages (from requests) (2.6.3)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.9/site-packages (from requests) (3.11)
Requirement already satisfied: numpy>=1.19.5 in ./.venv/lib/python3.9/site-packages (from scikit-learn) (2.0.2)
Collecting joblib>=1.2.0
  Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
     |████████████████████████████████| 309 kB 57.6 MB/s 
Collecting scipy>=1.6.0
  Downloading scipy-1.13.1-cp39-cp39-macosx_10_9_x86_64.whl (39.4 MB)
     |████████████████████████████████| 39.4 MB 58.0 MB/s 
Collecting threadpoolctl>=3.1.0
  Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn, pypdf
Successfully installed joblib-1.5.3 pypdf-6.6.2 scikit-learn-1.6.1 scipy-1.13.1 threadpoolctl-3.6.0
WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
You should consider upgrading via the '/Users/mbachir/programation/MVP_Project/.venv/bin/python3 -m pip install --upgrade pip' command.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi recherche_profil.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ py recherche_profil.py
pymupdf    python     python3    python3.9  
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 recherche_profil.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/recherche_profil.py", line 208, in <module>
    matches = find_matching_jobs(
  File "/Users/mbachir/programation/MVP_Project/recherche_profil.py", line 171, in find_matching_jobs
    cv_text = read_cv(cv_path)
  File "/Users/mbachir/programation/MVP_Project/recherche_profil.py", line 40, in read_cv
    return read_pdf(path)
  File "/Users/mbachir/programation/MVP_Project/recherche_profil.py", line 25, in read_pdf
    reader = PdfReader(path)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/pypdf/_reader.py", line 144, in __init__
    self._initialize_stream(stream)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/pypdf/_reader.py", line 163, in _initialize_stream
    with open(stream, "rb") as fh:
FileNotFoundError: [Errno 2] No such file or directory: 'mon_cv.pdf'
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pwd
/Users/mbachir/programation/MVP_Project
(.venv) FRPARMAC0036980:MVP_Project mbachir$ cp 
(.venv) FRPARMAC0036980:MVP_Project mbachir$ cp /Users/mbachir/
.anyconnect               .npm/                     Documents/
.bash_history             .sqlite_history           Downloads/
.bash_sessions/           .ssh/                     Library/
.CFUserTextEncoding       .streamlit/               Movies/
.cisco/                   .Trash/                   Music/
.config/                  .vim/                     nltk_data/
.cups/                    .viminfo                  OneDrive - Vivendi Group/
.DS_Store                 .vpn/                     Pictures/
.gitconfig                Applications/             Postman/
.keras/                   Code/                     programation/
.local/                   Desktop/                  Public/
.matplotlib/              Dev/                      yocto/
(.venv) FRPARMAC0036980:MVP_Project mbachir$ cp /Users/mbachir/Documents/Mounira/CV_TEST.pdf mon_cv.pdf
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 recherche_profil.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/recherche_profil.py", line 208, in <module>
    matches = find_matching_jobs(
  File "/Users/mbachir/programation/MVP_Project/recherche_profil.py", line 178, in find_matching_jobs
    offers = fetch_jobs_france_travail(
  File "/Users/mbachir/programation/MVP_Project/recherche_profil.py", line 104, in fetch_jobs_france_travail
    raise RuntimeError("France Travail: access_token manquant (OAuth2).")
RuntimeError: France Travail: access_token manquant (OAuth2).
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install requests scikit-learn python-docx pypdf
Requirement already satisfied: requests in ./.venv/lib/python3.9/site-packages (2.32.5)
Requirement already satisfied: scikit-learn in ./.venv/lib/python3.9/site-packages (1.6.1)
Requirement already satisfied: python-docx in ./.venv/lib/python3.9/site-packages (1.2.0)
Requirement already satisfied: pypdf in ./.venv/lib/python3.9/site-packages (6.6.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.9/site-packages (from requests) (2.6.3)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.9/site-packages (from requests) (3.11)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.9/site-packages (from requests) (3.4.4)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.9/site-packages (from requests) (2026.1.4)
Requirement already satisfied: threadpoolctl>=3.1.0 in ./.venv/lib/python3.9/site-packages (from scikit-learn) (3.6.0)
Requirement already satisfied: joblib>=1.2.0 in ./.venv/lib/python3.9/site-packages (from scikit-learn) (1.5.3)
Requirement already satisfied: scipy>=1.6.0 in ./.venv/lib/python3.9/site-packages (from scikit-learn) (1.13.1)
Requirement already satisfied: numpy>=1.19.5 in ./.venv/lib/python3.9/site-packages (from scikit-learn) (2.0.2)
Requirement already satisfied: lxml>=3.1.0 in ./.venv/lib/python3.9/site-packages (from python-docx) (6.0.2)
Requirement already satisfied: typing_extensions>=4.9.0 in ./.venv/lib/python3.9/site-packages (from python-docx) (4.15.0)
WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
You should consider upgrading via the '/Users/mbachir/programation/MVP_Project/.venv/bin/python3 -m pip install --upgrade pip' command.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ export ADZUNA_APP_ID="..."
(.venv) FRPARMAC0036980:MVP_Project mbachir$ export ADZUNA_APP_KEY="..."
(.venv) FRPARMAC0036980:MVP_Project mbachir$ export JOOBLE_API_KEY="..."
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 270, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 245, in find_jobs_for_cv
    offers += fetch_adzuna_jobs(query, location=location, country=country,
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 129, in fetch_adzuna_jobs
    r.raise_for_status()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/requests/models.py", line 1026, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=...&app_key=...&results_per_page=50&what=projets+num%C3%A9riques+services+pilotage+analyse+projet+fonctionnelle+solutions&content-type=application%2Fjson&where=Paris
(.venv) FRPARMAC0036980:MVP_Project mbachir$ echo $ADZUNA_APP_ID
...
(.venv) FRPARMAC0036980:MVP_Project mbachir$ echo $ADZUNA_APP_KEY
...
(.venv) FRPARMAC0036980:MVP_Project mbachir$ export ADZUNA_APP_ID="cd778784"
(.venv) FRPARMAC0036980:MVP_Project mbachir$ export ADZUNA_APP_KEY="c02ddbf9bf93a57df2f952e2a589face"
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 270, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 247, in find_jobs_for_cv
    offers += fetch_jooble_jobs(query, location=location,
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 178, in fetch_jooble_jobs
    r.raise_for_status()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/requests/models.py", line 1026, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://jooble.org/api/...
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 248
    pages=pages_each, results_per_page=results_per_page)
IndentationError: unexpected indent
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 270, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 251, in find_jobs_for_cv
    scored = score_offers(cv_text, offers)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 205, in score_offers
    sims = cosine_similarity(X[0:1], X[1:]).flatten()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/_param_validation.py", line 216, in wrapper
    return func(*args, **kwargs)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 1741, in cosine_similarity
    X, Y = check_pairwise_arrays(X, Y)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 209, in check_pairwise_arrays
    Y = check_array(
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 1130, in check_array
    raise ValueError(
ValueError: Found array with 0 sample(s) (shape=(0, 628)) while a minimum of 1 is required by check_pairwise_arrays.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ ls -l
total 408
-rw-r--r--  1 mbachir  staff    8281 27 jan 20:19 app.py
-rw-r--r--  1 mbachir  staff    8328 27 jan 22:38 cv_to_job.py
-rw-r--r--  1 mbachir  staff   20480 27 jan 20:20 data.db
-rw-r--r--@ 1 mbachir  staff  145915 27 jan 22:06 mon_cv.pdf
-rw-r--r--  1 mbachir  staff    4829 27 jan 20:05 old_app.py
-rw-r--r--  1 mbachir  staff    6529 27 jan 22:02 recherche_profil.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 276
    return results
    ^
SyntaxError: 'return' outside function
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 271, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 251, in find_jobs_for_cv
    scored = score_offers(cv_text, offers)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 205, in score_offers
    sims = cosine_similarity(X[0:1], X[1:]).flatten()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/_param_validation.py", line 216, in wrapper
    return func(*args, **kwargs)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 1741, in cosine_similarity
    X, Y = check_pairwise_arrays(X, Y)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 209, in check_pairwise_arrays
    Y = check_array(
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 1130, in check_array
    raise ValueError(
ValueError: Found array with 0 sample(s) (shape=(0, 628)) while a minimum of 1 is required by check_pairwise_arrays.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 271, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 251, in find_jobs_for_cv
    scored = score_offers(cv_text, offers)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 205, in score_offers
    sims = cosine_similarity(X[0:1], X[1:]).flatten()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/_param_validation.py", line 216, in wrapper
    return func(*args, **kwargs)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 1741, in cosine_similarity
    X, Y = check_pairwise_arrays(X, Y)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 209, in check_pairwise_arrays
    Y = check_array(
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 1130, in check_array
    raise ValueError(
ValueError: Found array with 0 sample(s) (shape=(0, 628)) while a minimum of 1 is required by check_pairwise_arrays.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 237
    print("\n===== CONTENU DU CV (début) =====")
TabError: inconsistent use of tabs and spaces in indentation
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 241
    if not cv_text.strip():
IndentationError: unexpected indent
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)

===== CONTENU DU CV (début) =====
    Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la maintenance. Habituée à travailler dans des environnements exigeants et réglementés, je dispose d’une solide ex-périence en gouvernance de projets, coordination d’acteurs multiples (métiers, équipes techniques, prestataires), analyse fonctionnelle des besoins, pilotage budgétaire et planning, et conduite du changement. Souhaitant aujourd’hui mettre mon expertise au service de projets numériques à fort impact public et orientés usagers, je candidate à un poste de Cheffe de projet numérique au sein de la DNUM des Ministères sociaux. COMPÉTENCES CLÉS • Pilotage de projets numériques stratégiques • Gouvernance de projets et animation des parties prenantes • Analyse fonctionnelle et expression des besoins métiers • Pilotage de prestataires et coordination multi-acteurs • Organisation du cycle de vie projet (cadrage, réalisation, déploiement, maintenance) • Méthodes de travail itératives / agiles • Conduite du changement et accompagnement des usages • Continuité de service, qualité et sécurité des SI • Reporting, communication et rédactionnel structuré  EXPÉRIENCES PROFESSIONNELLES  CANAL+ GROUP – Chef de projets / Delivery Manager  Pilotage opérationnel de projets numériques et services stratégiques à fort impact utilisateur.  Définition et mise en œuvre de la gouvernance projet • Coordination des parties prenantes (équipes métiers, équipes techniques, prestataires) • Analyse fonctionnelle des besoins et cadrage des solutions • Pilotage de la réalisation confiée à des partenaires externes • Suivi des plannings, des risques, de la qualité et des livrables • Organisation des phases de recette, déploiement et mise en production • Organisation du support et du suivi post-déploiement  C
===== CONTENU DU CV (fin) =====

Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 275, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 255, in find_jobs_for_cv
    scored = score_offers(cv_text, offers)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 205, in score_offers
    sims = cosine_similarity(X[0:1], X[1:]).flatten()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/_param_validation.py", line 216, in wrapper
    return func(*args, **kwargs)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 1741, in cosine_similarity
    X, Y = check_pairwise_arrays(X, Y)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 209, in check_pairwise_arrays
    Y = check_array(
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 1130, in check_array
    raise ValueError(
ValueError: Found array with 0 sample(s) (shape=(0, 628)) while a minimum of 1 is required by check_pairwise_arrays.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Query envoyée aux APIs: projets numériques services pilotage analyse projet fonctionnelle solutions
Adzuna offers: 0
⚠️ Jooble erreur: Jooble HTTP 403: accès refusé. Détail: <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:
Total offers récupérées (après dédup): 0
❌ Aucune offre récupérée. Corrigez les clés API (401/403) ou force_query trop spécifique.

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Query envoyée aux APIs: projets numériques services pilotage analyse projet fonctionnelle solutions
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
Adzuna offers: 0
⚠️ Jooble erreur: Jooble HTTP 403: accès refusé. Détail: <!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:
Total offers récupérées (après dédup): 0
❌ Aucune offre récupérée. Corrigez les clés API (401/403) ou force_query trop spécifique.

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Query envoyée aux APIs: projets numériques services pilotage analyse projet fonctionnelle solutions
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
Adzuna offers: 0
Total offers récupérées (après dédup): 0
❌ Aucune offre récupérée. Corrigez les clés API (401/403) ou force_query trop spécifique.

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Query envoyée aux APIs: projets numériques services pilotage analyse projet fonctionnelle solutions
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
Adzuna offers: 0
Total offers récupérées (après dédup): 0
❌ Aucune offre récupérée. Corrigez les clés API (401/403) ou force_query trop spécifique.

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Query envoyée aux APIs: projets numériques services pilotage analyse projet fonctionnelle solutions
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
Adzuna offers: 0
Total offers récupérées (après dédup): 0
❌ Aucune offre récupérée. Corrigez les clés API (401/403) ou force_query trop spécifique.

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install "urllib3<2"
Collecting urllib3<2
  Downloading urllib3-1.26.20-py2.py3-none-any.whl (144 kB)
     |████████████████████████████████| 144 kB 6.3 MB/s 
Installing collected packages: urllib3
  Attempting uninstall: urllib3
    Found existing installation: urllib3 2.6.3
    Uninstalling urllib3-2.6.3:
      Successfully uninstalled urllib3-2.6.3
Successfully installed urllib3-1.26.20
WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
You should consider upgrading via the '/Users/mbachir/programation/MVP_Project/.venv/bin/python3 -m pip install --upgrade pip' command.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Query envoyée aux APIs: projets numériques services pilotage analyse projet fonctionnelle solutions
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=projets+num
[Adzuna] results returned: 0
Adzuna offers: 0
Total offers récupérées (après dédup): 0
❌ Aucune offre récupérée. Corrigez les clés API (401/403) ou force_query trop spécifique.

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job_2.py", line 257, in <module>
    results = find_jobs_for_cv(..., force_query=force)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job_2.py", line 196, in find_jobs_for_cv
    cv_text = read_cv(cv_path)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job_2.py", line 36, in read_cv
    if not os.path.exists(path):
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/genericpath.py", line 19, in exists
    os.stat(path)
TypeError: stat: path should be string, bytes, os.PathLike or integer, not ellipsis
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.17989030911817502
Top 5 scores: [np.float64(0.1799), np.float64(0.1662), np.float64(0.1629), np.float64(0.1513), np.float64(0.1413)]

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.17989030911817502
Top 5 scores: [np.float64(0.1799), np.float64(0.1662), np.float64(0.1629), np.float64(0.1513), np.float64(0.1413)]

Top résultats:
[]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.17989030911817502
Top 5 scores: [np.float64(0.1799), np.float64(0.1662), np.float64(0.1629), np.float64(0.1513), np.float64(0.1413)]

Top résultats:
[
  {
    "score": 0.1799,
    "title": "chef de projet RIM / Pharma",
    "company": "INFOGENE",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591125824?se=TGU1tlX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=B9853296C0A13DDEB0AC21E9C76BE25B00A0604A",
    "source": "Adzuna"
  },
  {
    "score": 0.1662,
    "title": "Chef de projets congrès",
    "company": "Overcome",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135240?se=TGU1tlX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=8AAA459461431A3C926AF00FA5806796AA9C3944",
    "source": "Adzuna"
  },
  {
    "score": 0.1629,
    "title": "Chef de Projet MOA H/F",
    "company": "BEHIVE",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/details/5598520330?utm_medium=api&utm_source=cd778784",
    "source": "Adzuna"
  },
  {
    "score": 0.1513,
    "title": "Chef de Projets MOA H/F",
    "company": "Spirica",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558788247?se=TGU1tlX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=2500286DA081D84DB9992CA949C44A35DA72E9B0",
    "source": "Adzuna"
  },
  {
    "score": 0.1413,
    "title": "Chef de Projet Applicatif H/F",
    "company": "Michael Page",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5584105850?se=TGU1tlX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=49C02CA9FB39CE5C31E38D25FE374BDE1C9B7697",
    "source": "Adzuna"
  },
  {
    "score": 0.141,
    "title": "Chef de Projet IT Hispanophone H/F",
    "company": "LUSIS",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5503097463?se=TGU1tlX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=7A55263E1AD8368574F39DD975A606639CB2AA7B",
    "source": "Adzuna"
  },
  {
    "score": 0.1407,
    "title": "Chef de Projet MOE H/F",
    "company": "Nexton",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5588993476?se=YH8ut1X88BGMYN1f0Fm0ig&utm_medium=api&utm_source=cd778784&v=51C38CA680532CE1351B4ABD0E9839BC5F7252B5",
    "source": "Adzuna"
  }
]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.17989030911817502
Top 5 scores: [np.float64(0.1799), np.float64(0.1662), np.float64(0.1629), np.float64(0.1513), np.float64(0.1413)]

Top résultats:
[
  {
    "score": 0.1799,
    "title": "chef de projet RIM / Pharma",
    "company": "INFOGENE",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591125824?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=B9853296C0A13DDEB0AC21E9C76BE25B00A0604A",
    "source": "Adzuna"
  },
  {
    "score": 0.1662,
    "title": "Chef de projets congrès",
    "company": "Overcome",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135240?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=8AAA459461431A3C926AF00FA5806796AA9C3944",
    "source": "Adzuna"
  },
  {
    "score": 0.1629,
    "title": "Chef de Projet MOA H/F",
    "company": "BEHIVE",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/details/5598520330?utm_medium=api&utm_source=cd778784",
    "source": "Adzuna"
  },
  {
    "score": 0.1513,
    "title": "Chef de Projets MOA H/F",
    "company": "Spirica",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558788247?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=2500286DA081D84DB9992CA949C44A35DA72E9B0",
    "source": "Adzuna"
  },
  {
    "score": 0.1413,
    "title": "Chef de Projet Applicatif H/F",
    "company": "Michael Page",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5584105850?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=49C02CA9FB39CE5C31E38D25FE374BDE1C9B7697",
    "source": "Adzuna"
  },
  {
    "score": 0.141,
    "title": "Chef de Projet IT Hispanophone H/F",
    "company": "LUSIS",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5503097463?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=7A55263E1AD8368574F39DD975A606639CB2AA7B",
    "source": "Adzuna"
  },
  {
    "score": 0.1407,
    "title": "Chef de Projet MOE H/F",
    "company": "Nexton",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5588993476?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=51C38CA680532CE1351B4ABD0E9839BC5F7252B5",
    "source": "Adzuna"
  },
  {
    "score": 0.1371,
    "title": "Chef de Projet en Assurance Data & IA H/F",
    "company": "MNCAP",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5569576212?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=7FF767B9410CD0A80BFA371576BE708D55ECF87A",
    "source": "Adzuna"
  },
  {
    "score": 0.1363,
    "title": "Chef de Projet Moex H/F",
    "company": "Michael Page",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5590178621?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=A3D040F13C07DE994F6975D64708E9D17C6C6118",
    "source": "Adzuna"
  },
  {
    "score": 0.1347,
    "title": "Chef de Projet Marketing Digital H/F",
    "company": "People&Baby",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5525326968?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=DF408B3F9E442D0517730714C0DEC333DAFA273E",
    "source": "Adzuna"
  },
  {
    "score": 0.1336,
    "title": "Chef de Projet Radio H/F",
    "company": "Extia Ingénierie",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5571091181?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=D1F00AA6E65AE6DF7004920E6110EC25AB0CA2B7",
    "source": "Adzuna"
  },
  {
    "score": 0.1316,
    "title": "Chef de Projet Douane H/F",
    "company": "Chronopost",
    "location": "14ème Arrondissement, Paris",
    "url": "https://www.adzuna.fr/land/ad/5601749597?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=504F9CD3D830DD94A8A5EE0D4DF467A584486625",
    "source": "Adzuna"
  },
  {
    "score": 0.1309,
    "title": "Chef de projet moex h/f (CDD)",
    "company": "MICHAEL PAGE",
    "location": "1er Arrondissement, Paris",
    "url": "https://www.adzuna.fr/land/ad/5587106552?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=B18881274CB60E0B4A2479E9BE5F7EBBCA85D84F",
    "source": "Adzuna"
  },
  {
    "score": 0.1302,
    "title": "Chef de projet utilisateur - crm - h/f (CDI)",
    "company": "BANQUE DE FRANCE",
    "location": "1er Arrondissement, Paris",
    "url": "https://www.adzuna.fr/land/ad/5512206912?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=A98F9B456F19DCF1D15F2D18AD6AF628EF3FDE54",
    "source": "Adzuna"
  },
  {
    "score": 0.127,
    "title": "Chef de projets – H/F",
    "company": "Fluxym",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135306?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=72744847A0DF6627DB144C665DDF1A51568D0E00",
    "source": "Adzuna"
  },
  {
    "score": 0.1266,
    "title": "Chef de Projets Travaux H/F",
    "company": "Viparis",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5569559201?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=7EAEF81C0B42BC5E3BF9DEEF4B463BCC30057C86",
    "source": "Adzuna"
  },
  {
    "score": 0.1264,
    "title": "Chef projet F/H",
    "company": "SARL GOBE",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/details/5592115801?utm_medium=api&utm_source=cd778784",
    "source": "Adzuna"
  },
  {
    "score": 0.1249,
    "title": "Chef de Projet Backbone H/F",
    "company": "W HUB",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5593702162?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=E9FC0C8D6D9B1836C3DCE30CD3D4CE747D9794B1",
    "source": "Adzuna"
  },
  {
    "score": 0.1247,
    "title": "Chef de projet/Cheffe de projet",
    "company": "Atyx",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5589015721?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=43BFB43E18D5ED50A06D50757448CA8E1DCCAE27",
    "source": "Adzuna"
  },
  {
    "score": 0.1235,
    "title": "Chef de Projet CVC H/F",
    "company": "New-E",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5125596702?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=EEB75573DEDC9A180B5C3D54AEAB49433DA0E889",
    "source": "Adzuna"
  },
  {
    "score": 0.1226,
    "title": "Chef de Projets Etudes Electricité H/F",
    "company": "CAP INGELEC",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5508692716?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=8DBA40840E246D1E40F411E4BE5D160DC4690F90",
    "source": "Adzuna"
  },
  {
    "score": 0.1223,
    "title": "CHEF DE PROJET",
    "company": "CreativLink",
    "location": "9ème Arrondissement, Paris",
    "url": "https://www.adzuna.fr/details/5574052611?utm_medium=api&utm_source=cd778784",
    "source": "Adzuna"
  },
  {
    "score": 0.1218,
    "title": "Chef de Projet Agencement Retail H/F",
    "company": "Vedaci Conseil",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558763264?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=3207E03D2D0B9B17362B9C73013B71AAAA88059D",
    "source": "Adzuna"
  },
  {
    "score": 0.1202,
    "title": "Chef de Projet Immobilier H/F",
    "company": "Robert Half",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5569528103?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=1C8CFDF34D55734A63020AEC6B0F826563DDD662",
    "source": "Adzuna"
  },
  {
    "score": 0.1199,
    "title": "Chef de Projet Électricité H/F",
    "company": "EURETUDES TRAVAIL TEMPORAIRE",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5602954570?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=304FCAC236347BB2FDA133405B8D00C8B2145B84",
    "source": "Adzuna"
  },
  {
    "score": 0.1195,
    "title": "Chef de projet/Cheffe de projet",
    "company": "Ministère de la Justice",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5601742392?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=0E6F9400BD2ECBA2BFF5C11B002375612581A6BA",
    "source": "Adzuna"
  },
  {
    "score": 0.1189,
    "title": "Chef de Projet AMOA H/F",
    "company": "Sciences Po",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5488973840?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=0885EDC04735ECB31AE913685096779CA009B31B",
    "source": "Adzuna"
  },
  {
    "score": 0.1182,
    "title": "Chef de projet Sénior Energie",
    "company": "Partenor Digital",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5462201780?se=0qZz51X88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=B8A120A18D324F67718F8609DF005064049EDCAB",
    "source": "Adzuna"
  },
  {
    "score": 0.118,
    "title": "Gestionnaire ADV - Chef de Projet H/F (CDI)",
    "company": "Page Personnel",
    "location": "1er Arrondissement, Paris",
    "url": "https://www.adzuna.fr/land/ad/5578713281?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=9ECBD1DAFB5396A4102B2D0DD8C929FF8B61CCA7",
    "source": "Adzuna"
  },
  {
    "score": 0.1168,
    "title": "Chef de projet catalogue de données - h/f (CDI)",
    "company": "BANQUE DE FRANCE",
    "location": "1er Arrondissement, Paris",
    "url": "https://www.adzuna.fr/land/ad/5530397832?se=KpxS6FX88BGMbc0SHM_Upw&utm_medium=api&utm_source=cd778784&v=D51A2F00E6B3D3C76A332F5508243745EC1A1C71",
    "source": "Adzuna"
  }
]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.13727878532413865
Top 5 scores: [np.float64(0.1373), np.float64(0.1089), np.float64(0.1056), np.float64(0.099), np.float64(0.0917)]

Top résultats:
[
  {
    "score": 0.1373,
    "title": "Chef de projets – H/F",
    "company": "Fluxym",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135306?se=RNl_Elf88BGMYN1f0Fm0ig&utm_medium=api&utm_source=cd778784&v=72744847A0DF6627DB144C665DDF1A51568D0E00",
    "source": "Adzuna"
  },
  {
    "score": 0.1089,
    "title": "Chef de projets congrès",
    "company": "Overcome",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135240?se=RNl_Elf88BGMYN1f0Fm0ig&utm_medium=api&utm_source=cd778784&v=8AAA459461431A3C926AF00FA5806796AA9C3944",
    "source": "Adzuna"
  },
  {
    "score": 0.1056,
    "title": "Chef de Projets MOA H/F",
    "company": "Spirica",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558788247?se=RNl_Elf88BGMYN1f0Fm0ig&utm_medium=api&utm_source=cd778784&v=2500286DA081D84DB9992CA949C44A35DA72E9B0",
    "source": "Adzuna"
  }
]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.1353552763261117
Top 5 scores: [np.float64(0.1354), np.float64(0.1081), np.float64(0.1067), np.float64(0.0934), np.float64(0.0925)]

Top résultats:
[
  {
    "score": 0.1354,
    "title": "Chef de projets – H/F",
    "company": "Fluxym",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135306?se=csQy0OD88BG069Cua8QVuw&utm_medium=api&utm_source=cd778784&v=72744847A0DF6627DB144C665DDF1A51568D0E00",
    "source": "Adzuna"
  },
  {
    "score": 0.1081,
    "title": "Chef de projets congrès",
    "company": "Overcome",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135240?se=csQy0OD88BG069Cua8QVuw&utm_medium=api&utm_source=cd778784&v=8AAA459461431A3C926AF00FA5806796AA9C3944",
    "source": "Adzuna"
  },
  {
    "score": 0.1067,
    "title": "Chef de Projets MOA H/F",
    "company": "Spirica",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558788247?se=csQy0OD88BG069Cua8QVuw&utm_medium=api&utm_source=cd778784&v=2500286DA081D84DB9992CA949C44A35DA72E9B0",
    "source": "Adzuna"
  }
]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.1282305785203011
Top 5 scores: [np.float64(0.1282), np.float64(0.1066), np.float64(0.1012), np.float64(0.1011), np.float64(0.0921)]

Top résultats:
[
  {
    "score": 0.1282,
    "title": "Chef de projets – H/F",
    "company": "Fluxym",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135306?se=Wpuf0-P88BGK_Nep8SMZLQ&utm_medium=api&utm_source=cd778784&v=72744847A0DF6627DB144C665DDF1A51568D0E00",
    "source": "Adzuna"
  },
  {
    "score": 0.1066,
    "title": "Chef de Projets Tranverses H/F",
    "company": "Antin Résidences",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5602906725?se=si2d0uP88BGvC8P-PoupKw&utm_medium=api&utm_source=cd778784&v=A6CFF14FAF5742397B3A707BC430F9175EFBCC66",
    "source": "Adzuna"
  },
  {
    "score": 0.1012,
    "title": "Chef de projets congrès",
    "company": "Overcome",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135240?se=si2d0uP88BGvC8P-PoupKw&utm_medium=api&utm_source=cd778784&v=8AAA459461431A3C926AF00FA5806796AA9C3944",
    "source": "Adzuna"
  },
  {
    "score": 0.1011,
    "title": "Chef de Projets MOA H/F",
    "company": "Spirica",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558788247?se=si2d0uP88BGvC8P-PoupKw&utm_medium=api&utm_source=cd778784&v=2500286DA081D84DB9992CA949C44A35DA72E9B0",
    "source": "Adzuna"
  }
]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.1282305785203011
Top 5 scores: [np.float64(0.1282), np.float64(0.1066), np.float64(0.1012), np.float64(0.1011), np.float64(0.0921)]

Top résultats:
[
  {
    "score": 0.1282,
    "title": "Chef de projets – H/F",
    "company": "Fluxym",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135306?se=8FJR_OP88BG069Cua8QVuw&utm_medium=api&utm_source=cd778784&v=72744847A0DF6627DB144C665DDF1A51568D0E00",
    "source": "Adzuna"
  },
  {
    "score": 0.1066,
    "title": "Chef de Projets Tranverses H/F",
    "company": "Antin Résidences",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5602906725?se=aDJQ--P88BGK_Nep8SMZLQ&utm_medium=api&utm_source=cd778784&v=A6CFF14FAF5742397B3A707BC430F9175EFBCC66",
    "source": "Adzuna"
  },
  {
    "score": 0.1012,
    "title": "Chef de projets congrès",
    "company": "Overcome",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135240?se=aDJQ--P88BGK_Nep8SMZLQ&utm_medium=api&utm_source=cd778784&v=8AAA459461431A3C926AF00FA5806796AA9C3944",
    "source": "Adzuna"
  },
  {
    "score": 0.1011,
    "title": "Chef de Projets MOA H/F",
    "company": "Spirica",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558788247?se=aDJQ--P88BGK_Nep8SMZLQ&utm_medium=api&utm_source=cd778784&v=2500286DA081D84DB9992CA949C44A35DA72E9B0",
    "source": "Adzuna"
  }
]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)

===== CONTENU DU CV (début) =====
    Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la maintenance. Habituée à travailler dans des environnements exigeants et réglementés, je dispose d’une solide ex-périence en gouvernance de projets, coordination d’acteurs multiples (métiers, équipes techniques, prestataires), analyse fonctionnelle des besoins, pilotage budgétaire et planning, et conduite du changement. Souhaitant aujourd’hui mettre mon expertise au service de projets numériques à fort impact public et orientés usagers, je candidate à un poste de Cheffe de projet numérique au sein de la DNUM des Ministères sociaux. COMPÉTENCES CLÉS • Pilotage de projets numériques stratégiques • Gouvernance de projets et animation des parties prenantes • Analyse fonctionnelle et expression des besoins métiers • Pilotage de prestataires et coordination multi-acteurs • Organisation du cycle de vie projet (cadrage, réalisation, déploiement, maintenance) • Méthodes de travail itératives / agiles • Conduite du changement et accompagnement des usages • Continuité de service, qualité et sécurité des SI • Reporting, communication et rédactionnel structuré  EXPÉRIENCES PROFESSIONNELLES  CANAL+ GROUP – Chef de projets / Delivery Manager  Pilotage opérationnel de projets numériques et services stratégiques à fort impact utilisateur.  Définition et mise en œuvre de la gouvernance projet • Coordination des parties prenantes (équipes métiers, équipes techniques, prestataires) • Analyse fonctionnelle des besoins et cadrage des solutions • Pilotage de la réalisation confiée à des partenaires externes • Suivi des plannings, des risques, de la qualité et des livrables • Organisation des phases de recette, déploiement et mise en production • Organisation du support et du suivi post-déploiement  C
===== CONTENU DU CV (fin) =====

Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 275, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 255, in find_jobs_for_cv
    scored = score_offers(cv_text, offers)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 205, in score_offers
    sims = cosine_similarity(X[0:1], X[1:]).flatten()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/_param_validation.py", line 216, in wrapper
    return func(*args, **kwargs)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 1741, in cosine_similarity
    X, Y = check_pairwise_arrays(X, Y)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 209, in check_pairwise_arrays
    Y = check_array(
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 1130, in check_array
    raise ValueError(
ValueError: Found array with 0 sample(s) (shape=(0, 628)) while a minimum of 1 is required by check_pairwise_arrays.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi cv_to_job_2.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)

===== CONTENU DU CV (début) =====
    Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la maintenance. Habituée à travailler dans des environnements exigeants et réglementés, je dispose d’une solide ex-périence en gouvernance de projets, coordination d’acteurs multiples (métiers, équipes techniques, prestataires), analyse fonctionnelle des besoins, pilotage budgétaire et planning, et conduite du changement. Souhaitant aujourd’hui mettre mon expertise au service de projets numériques à fort impact public et orientés usagers, je candidate à un poste de Cheffe de projet numérique au sein de la DNUM des Ministères sociaux. COMPÉTENCES CLÉS • Pilotage de projets numériques stratégiques • Gouvernance de projets et animation des parties prenantes • Analyse fonctionnelle et expression des besoins métiers • Pilotage de prestataires et coordination multi-acteurs • Organisation du cycle de vie projet (cadrage, réalisation, déploiement, maintenance) • Méthodes de travail itératives / agiles • Conduite du changement et accompagnement des usages • Continuité de service, qualité et sécurité des SI • Reporting, communication et rédactionnel structuré  EXPÉRIENCES PROFESSIONNELLES  CANAL+ GROUP – Chef de projets / Delivery Manager  Pilotage opérationnel de projets numériques et services stratégiques à fort impact utilisateur.  Définition et mise en œuvre de la gouvernance projet • Coordination des parties prenantes (équipes métiers, équipes techniques, prestataires) • Analyse fonctionnelle des besoins et cadrage des solutions • Pilotage de la réalisation confiée à des partenaires externes • Suivi des plannings, des risques, de la qualité et des livrables • Organisation des phases de recette, déploiement et mise en production • Organisation du support et du suivi post-déploiement  C
===== CONTENU DU CV (fin) =====

Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 275, in <module>
    results = find_jobs_for_cv(
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 255, in find_jobs_for_cv
    scored = score_offers(cv_text, offers)
  File "/Users/mbachir/programation/MVP_Project/cv_to_job.py", line 205, in score_offers
    sims = cosine_similarity(X[0:1], X[1:]).flatten()
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/_param_validation.py", line 216, in wrapper
    return func(*args, **kwargs)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 1741, in cosine_similarity
    X, Y = check_pairwise_arrays(X, Y)
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/metrics/pairwise.py", line 209, in check_pairwise_arrays
    Y = check_array(
  File "/Users/mbachir/programation/MVP_Project/.venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 1130, in check_array
    raise ValueError(
ValueError: Found array with 0 sample(s) (shape=(0, 628)) while a minimum of 1 is required by check_pairwise_arrays.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python3 cv_to_job_2.py 
Ignoring wrong pointing object 6 0 (offset 0)
Ignoring wrong pointing object 8 0 (offset 0)
Ignoring wrong pointing object 10 0 (offset 0)
Ignoring wrong pointing object 12 0 (offset 0)
Ignoring wrong pointing object 15 0 (offset 0)
Ignoring wrong pointing object 17 0 (offset 0)
Ignoring wrong pointing object 19 0 (offset 0)
Ignoring wrong pointing object 21 0 (offset 0)
Ignoring wrong pointing object 24 0 (offset 0)
Ignoring wrong pointing object 26 0 (offset 0)
Ignoring wrong pointing object 33 0 (offset 0)
Ignoring wrong pointing object 35 0 (offset 0)
CV length: 3973
CV preview:     Cheffe de projet numérique – Projets stratégiques & services aux usagers   Cheffe de projet numérique senior, avec plus de 14 ans d’expérience dans le pilotage opérationnel de projets et services numériques complexes, de la phase de cadrage jusqu’au déploiement et à l’or-ganisation de la mainten
Query envoyée aux APIs: chef de projet
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
[Adzuna] status: 200 | url: https://api.adzuna.com/v1/api/jobs/fr/search/2?app_id=cd778784&app_key=c02ddbf9bf93a57df2f952e2a589face&results_per_page=50&what=chef+de+pro
[Adzuna] results returned: 50
Adzuna offers: 100
Total offers récupérées (après dédup): 100
Max score: 0.1336740441687269
Top 5 scores: [np.float64(0.1337), np.float64(0.1326), np.float64(0.1107), np.float64(0.107), np.float64(0.1041)]

Top résultats:
[
  {
    "score": 0.1337,
    "title": "Chef de Projet Convergence des Ged H/F",
    "company": "SIAAP",
    "location": "12ème Arrondissement, Paris",
    "url": "https://www.adzuna.fr/land/ad/5605956908?se=FpCDUiEB8RGU3uAh3VBzrA&utm_medium=api&utm_source=cd778784&v=9A20B105B4F3F2FC04AA2B66EB4AB02A233A5FE8",
    "source": "Adzuna"
  },
  {
    "score": 0.1326,
    "title": "Chef de projets – H/F",
    "company": "Fluxym",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135306?se=7LA_VCEB8RG70K-BDHxp1g&utm_medium=api&utm_source=cd778784&v=72744847A0DF6627DB144C665DDF1A51568D0E00",
    "source": "Adzuna"
  },
  {
    "score": 0.1107,
    "title": "Chef de Projet H/F",
    "company": "Cecurity.com",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5611423536?se=FpCDUiEB8RGU3uAh3VBzrA&utm_medium=api&utm_source=cd778784&v=7B6ABA1F250F42F81F97092731F5B40AB0DF10B3",
    "source": "Adzuna"
  },
  {
    "score": 0.107,
    "title": "Chef de Projets Tranverses H/F",
    "company": "Antin Résidences",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5602906725?se=7LA_VCEB8RG70K-BDHxp1g&utm_medium=api&utm_source=cd778784&v=A6CFF14FAF5742397B3A707BC430F9175EFBCC66",
    "source": "Adzuna"
  },
  {
    "score": 0.1041,
    "title": "Chef de projets congrès",
    "company": "Overcome",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5591135240?se=FpCDUiEB8RGU3uAh3VBzrA&utm_medium=api&utm_source=cd778784&v=8AAA459461431A3C926AF00FA5806796AA9C3944",
    "source": "Adzuna"
  },
  {
    "score": 0.102,
    "title": "Chef de Projets MOA H/F",
    "company": "Spirica",
    "location": "Paris, Ile-de-France",
    "url": "https://www.adzuna.fr/land/ad/5558788247?se=FpCDUiEB8RGU3uAh3VBzrA&utm_medium=api&utm_source=cd778784&v=2500286DA081D84DB9992CA949C44A35DA72E9B0",
    "source": "Adzuna"
  }
]
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python -m venv .venv
(.venv) FRPARMAC0036980:MVP_Project mbachir$ source .venv/bin/activate   # Mac/Linux
(.venv) FRPARMAC0036980:MVP_Project mbachir$ # .venv\Scripts\activate    # Windows
(.venv) FRPARMAC0036980:MVP_Project mbachir$ 
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install requests
Requirement already satisfied: requests in ./.venv/lib/python3.9/site-packages (2.32.5)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.9/site-packages (from requests) (3.4.4)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.9/site-packages (from requests) (2026.1.4)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.9/site-packages (from requests) (1.26.20)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.9/site-packages (from requests) (3.11)
WARNING: You are using pip version 21.2.4; however, version 26.0.1 is available.
You should consider upgrading via the '/Users/mbachir/programation/MVP_Project/.venv/bin/python3 -m pip install --upgrade pip' command.
(.venv) FRPARMAC0036980:MVP_Project mbachir$ /Users/mbachir/programation/MVP_Project/.venv/bin/python3 -m pip install --upgrade pip
Requirement already satisfied: pip in ./.venv/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Downloading pip-26.0.1-py3-none-any.whl (1.8 MB)
     |████████████████████████████████| 1.8 MB 12.9 MB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-26.0.1
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install requests
Requirement already satisfied: requests in ./.venv/lib/python3.9/site-packages (2.32.5)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.9/site-packages (from requests) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.9/site-packages (from requests) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.9/site-packages (from requests) (1.26.20)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.9/site-packages (from requests) (2026.1.4)
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi agent_meteo.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python agent_meteo.py
📅 2026-02-23 (Paris)
🧠 Analyse: Températures 10–16°C, pluie 8%, vent 18 km/h.
👕 Je te conseille :
 - veste mi-saison
 - pull léger (ou sweat)
 - baskets / chaussures normales
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install streamlit
Requirement already satisfied: streamlit in ./.venv/lib/python3.9/site-packages (1.50.0)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker<2,>=1.5.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<7,>=4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.2.5)
Requirement already satisfied: click<9,>=7.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (8.1.8)
Requirement already satisfied: numpy<3,>=1.23 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging<26,>=20 in ./.venv/lib/python3.9/site-packages (from streamlit) (25.0)
Requirement already satisfied: pandas<3,>=1.4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.3.3)
Requirement already satisfied: pillow<12,>=7.1.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf<7,>=3.20 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.33.4)
Requirement already satisfied: pyarrow>=7.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (21.0.0)
Requirement already satisfied: requests<3,>=2.27 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.32.5)
Requirement already satisfied: tenacity<10,>=8.1.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml<2,>=0.10.1 in ./.venv/lib/python3.9/site-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (4.15.0)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in ./.venv/lib/python3.9/site-packages (from streamlit) (3.1.46)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in ./.venv/lib/python3.9/site-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.5.4)
Requirement already satisfied: jinja2 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)
Requirement already satisfied: narwhals>=1.14.2 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.15.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in ./.venv/lib/python3.9/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in ./.venv/lib/python3.9/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Requirement already satisfied: python-dateutil>=2.8.2 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.3)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (1.26.20)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (2026.1.4)
Requirement already satisfied: MarkupSafe>=2.0 in ./.venv/lib/python3.9/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)
Requirement already satisfied: attrs>=22.2.0 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.1)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi app.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi app_meteo.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ streamlit run app_meteo.py 

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.45:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
^C  Stopping...
(.venv) FRPARMAC0036980:MVP_Project mbachir$ python -m venv .venv
(.venv) FRPARMAC0036980:MVP_Project mbachir$ source .venv/bin/activate   # Mac/Linux
(.venv) FRPARMAC0036980:MVP_Project mbachir$ # .venv\Scripts\activate    # Windows
(.venv) FRPARMAC0036980:MVP_Project mbachir$ 
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pip install streamlit
Requirement already satisfied: streamlit in ./.venv/lib/python3.9/site-packages (1.50.0)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker<2,>=1.5.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<7,>=4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.2.5)
Requirement already satisfied: click<9,>=7.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (8.1.8)
Requirement already satisfied: numpy<3,>=1.23 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging<26,>=20 in ./.venv/lib/python3.9/site-packages (from streamlit) (25.0)
Requirement already satisfied: pandas<3,>=1.4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.3.3)
Requirement already satisfied: pillow<12,>=7.1.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf<7,>=3.20 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.33.4)
Requirement already satisfied: pyarrow>=7.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (21.0.0)
Requirement already satisfied: requests<3,>=2.27 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.32.5)
Requirement already satisfied: tenacity<10,>=8.1.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml<2,>=0.10.1 in ./.venv/lib/python3.9/site-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (4.15.0)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in ./.venv/lib/python3.9/site-packages (from streamlit) (3.1.46)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in ./.venv/lib/python3.9/site-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.5.4)
Requirement already satisfied: jinja2 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)
Requirement already satisfied: narwhals>=1.14.2 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.15.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in ./.venv/lib/python3.9/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in ./.venv/lib/python3.9/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Requirement already satisfied: python-dateutil>=2.8.2 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.3)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (1.26.20)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (2026.1.4)
Requirement already satisfied: MarkupSafe>=2.0 in ./.venv/lib/python3.9/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)
Requirement already satisfied: attrs>=22.2.0 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.1)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)
(.venv) FRPARMAC0036980:MVP_Project mbachir$ mkdir ia_kangourou
(.venv) FRPARMAC0036980:MVP_Project mbachir$ cd ia_kangourou/
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ python -m venv .venv
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ source .venv/bin/activate   # Mac/Linux
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ # .venv\Scripts\activate    # Windows
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ 
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ pip install streamlit
Collecting streamlit
  Using cached streamlit-1.50.0-py3-none-any.whl (10.1 MB)
Collecting packaging<26,>=20
  Using cached packaging-25.0-py3-none-any.whl (66 kB)
Collecting pyarrow>=7.0
  Using cached pyarrow-21.0.0-cp39-cp39-macosx_12_0_x86_64.whl (32.7 MB)
Collecting pandas<3,>=1.4.0
  Using cached pandas-2.3.3-cp39-cp39-macosx_10_9_x86_64.whl (11.6 MB)
Collecting toml<2,>=0.10.1
  Using cached toml-0.10.2-py2.py3-none-any.whl (16 kB)
Collecting pydeck<1,>=0.8.0b4
  Using cached pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
Collecting numpy<3,>=1.23
  Using cached numpy-2.0.2-cp39-cp39-macosx_14_0_x86_64.whl (6.9 MB)
Collecting blinker<2,>=1.5.0
  Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Collecting click<9,>=7.0
  Using cached click-8.1.8-py3-none-any.whl (98 kB)
Collecting protobuf<7,>=3.20
  Downloading protobuf-6.33.5-cp39-abi3-macosx_10_9_universal2.whl (427 kB)
     |████████████████████████████████| 427 kB 12.7 MB/s 
Collecting requests<3,>=2.27
  Using cached requests-2.32.5-py3-none-any.whl (64 kB)
Collecting cachetools<7,>=4.0
  Downloading cachetools-6.2.6-py3-none-any.whl (11 kB)
Collecting pillow<12,>=7.1.0
  Using cached pillow-11.3.0-cp39-cp39-macosx_10_10_x86_64.whl (5.3 MB)
Collecting tornado!=6.5.0,<7,>=6.0.3
  Using cached tornado-6.5.4-cp39-abi3-macosx_10_9_x86_64.whl (442 kB)
Collecting tenacity<10,>=8.1.0
  Using cached tenacity-9.1.2-py3-none-any.whl (28 kB)
Collecting altair!=5.4.0,!=5.4.1,<6,>=4.0
  Using cached altair-5.5.0-py3-none-any.whl (731 kB)
Collecting gitpython!=3.1.19,<4,>=3.0.7
  Using cached gitpython-3.1.46-py3-none-any.whl (208 kB)
Collecting typing-extensions<5,>=4.4.0
  Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Collecting jsonschema>=3.0
  Using cached jsonschema-4.25.1-py3-none-any.whl (90 kB)
Collecting jinja2
  Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Collecting narwhals>=1.14.2
  Downloading narwhals-2.17.0-py3-none-any.whl (444 kB)
     |████████████████████████████████| 444 kB 64.2 MB/s 
Collecting gitdb<5,>=4.0.1
  Using cached gitdb-4.0.12-py3-none-any.whl (62 kB)
Collecting smmap<6,>=3.0.1
  Using cached smmap-5.0.2-py3-none-any.whl (24 kB)
Collecting attrs>=22.2.0
  Using cached attrs-25.4.0-py3-none-any.whl (67 kB)
Collecting referencing>=0.28.4
  Using cached referencing-0.36.2-py3-none-any.whl (26 kB)
Collecting jsonschema-specifications>=2023.03.6
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Collecting rpds-py>=0.7.1
  Using cached rpds_py-0.27.1-cp39-cp39-macosx_10_12_x86_64.whl (372 kB)
Collecting tzdata>=2022.7
  Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Collecting python-dateutil>=2.8.2
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting pytz>=2020.1
  Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Collecting MarkupSafe>=2.0
  Using cached markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl (11 kB)
Collecting six>=1.5
  Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting charset_normalizer<4,>=2
  Using cached charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl (209 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2026.1.4-py3-none-any.whl (152 kB)
Collecting urllib3<3,>=1.21.1
  Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.11-py3-none-any.whl (71 kB)
Installing collected packages: typing-extensions, rpds-py, attrs, referencing, smmap, six, MarkupSafe, jsonschema-specifications, urllib3, tzdata, pytz, python-dateutil, packaging, numpy, narwhals, jsonschema, jinja2, idna, gitdb, charset-normalizer, certifi, tornado, toml, tenacity, requests, pydeck, pyarrow, protobuf, pillow, pandas, gitpython, click, cachetools, blinker, altair, streamlit
Successfully installed MarkupSafe-3.0.3 altair-5.5.0 attrs-25.4.0 blinker-1.9.0 cachetools-6.2.6 certifi-2026.1.4 charset-normalizer-3.4.4 click-8.1.8 gitdb-4.0.12 gitpython-3.1.46 idna-3.11 jinja2-3.1.6 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 narwhals-2.17.0 numpy-2.0.2 packaging-25.0 pandas-2.3.3 pillow-11.3.0 protobuf-6.33.5 pyarrow-21.0.0 pydeck-0.9.1 python-dateutil-2.9.0.post0 pytz-2025.2 referencing-0.36.2 requests-2.32.5 rpds-py-0.27.1 six-1.17.0 smmap-5.0.2 streamlit-1.50.0 tenacity-9.1.2 toml-0.10.2 tornado-6.5.4 typing-extensions-4.15.0 tzdata-2025.3 urllib3-2.6.3
WARNING: You are using pip version 21.2.4; however, version 26.0.1 is available.
You should consider upgrading via the '/Users/mbachir/programation/MVP_Project/ia_kangourou/.venv/bin/python -m pip install --upgrade pip' command.
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi app.py
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi app.py
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.45:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
^C  Stopping...
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ rm -f app.py
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi app.py
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.45:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
^C  Stopping...
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ rm -f app.py
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi app.py
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.45:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
2026-02-23 21:14:27.622 Uncaught app execution
Traceback (most recent call last):
  File "/Users/mbachir/programation/MVP_Project/ia_kangourou/.venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 128, in exec_func_with_error_handling
    result = func()
  File "/Users/mbachir/programation/MVP_Project/ia_kangourou/.venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
  File "/Users/mbachir/programation/MVP_Project/ia_kangourou/app.py", line 4, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
^C  Stopping...
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ pip install streamlit matplotlib
Requirement already satisfied: streamlit in ./.venv/lib/python3.9/site-packages (1.50.0)
Collecting matplotlib
  Downloading matplotlib-3.9.4-cp39-cp39-macosx_10_12_x86_64.whl (7.9 MB)
     |████████████████████████████████| 7.9 MB 9.6 MB/s 
Requirement already satisfied: blinker<2,>=1.5.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (1.9.0)
Requirement already satisfied: toml<2,>=0.10.1 in ./.venv/lib/python3.9/site-packages (from streamlit) (0.10.2)
Requirement already satisfied: pandas<3,>=1.4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.3.3)
Requirement already satisfied: packaging<26,>=20 in ./.venv/lib/python3.9/site-packages (from streamlit) (25.0)
Requirement already satisfied: tenacity<10,>=8.1.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (9.1.2)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (4.15.0)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in ./.venv/lib/python3.9/site-packages (from streamlit) (3.1.46)
Requirement already satisfied: pyarrow>=7.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (21.0.0)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in ./.venv/lib/python3.9/site-packages (from streamlit) (0.9.1)
Requirement already satisfied: requests<3,>=2.27 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.32.5)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.5.4)
Requirement already satisfied: cachetools<7,>=4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.2.6)
Requirement already satisfied: pillow<12,>=7.1.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (11.3.0)
Requirement already satisfied: numpy<3,>=1.23 in ./.venv/lib/python3.9/site-packages (from streamlit) (2.0.2)
Requirement already satisfied: protobuf<7,>=3.20 in ./.venv/lib/python3.9/site-packages (from streamlit) (6.33.5)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (5.5.0)
Requirement already satisfied: click<9,>=7.0 in ./.venv/lib/python3.9/site-packages (from streamlit) (8.1.8)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.60.2-cp39-cp39-macosx_10_9_x86_64.whl (2.4 MB)
     |████████████████████████████████| 2.4 MB 34.9 MB/s 
Requirement already satisfied: python-dateutil>=2.7 in ./.venv/lib/python3.9/site-packages (from matplotlib) (2.9.0.post0)
Collecting pyparsing>=2.3.1
  Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
     |████████████████████████████████| 122 kB 61.3 MB/s 
Collecting contourpy>=1.0.1
  Downloading contourpy-1.3.0-cp39-cp39-macosx_10_9_x86_64.whl (265 kB)
     |████████████████████████████████| 265 kB 41.1 MB/s 
Collecting importlib-resources>=3.2.0
  Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Collecting kiwisolver>=1.3.1
  Downloading kiwisolver-1.4.7-cp39-cp39-macosx_10_9_x86_64.whl (65 kB)
     |████████████████████████████████| 65 kB 10.5 MB/s 
Collecting cycler>=0.10
  Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Requirement already satisfied: jinja2 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)
Requirement already satisfied: narwhals>=1.14.2 in ./.venv/lib/python3.9/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.17.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in ./.venv/lib/python3.9/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in ./.venv/lib/python3.9/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Collecting zipp>=3.1.0
  Downloading zipp-3.23.0-py3-none-any.whl (10 kB)
Requirement already satisfied: rpds-py>=0.7.1 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.1)
Requirement already satisfied: referencing>=0.28.4 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)
Requirement already satisfied: attrs>=22.2.0 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.venv/lib/python3.9/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: tzdata>=2022.7 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.3)
Requirement already satisfied: pytz>=2020.1 in ./.venv/lib/python3.9/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: MarkupSafe>=2.0 in ./.venv/lib/python3.9/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)
Requirement already satisfied: six>=1.5 in ./.venv/lib/python3.9/site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (2.6.3)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: charset_normalizer<4,>=2 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.9/site-packages (from requests<3,>=2.27->streamlit) (2026.1.4)
Installing collected packages: zipp, pyparsing, kiwisolver, importlib-resources, fonttools, cycler, contourpy, matplotlib
Successfully installed contourpy-1.3.0 cycler-0.12.1 fonttools-4.60.2 importlib-resources-6.5.2 kiwisolver-1.4.7 matplotlib-3.9.4 pyparsing-3.3.2 zipp-3.23.0
WARNING: You are using pip version 21.2.4; however, version 26.0.1 is available.
You should consider upgrading via the '/Users/mbachir/programation/MVP_Project/ia_kangourou/.venv/bin/python -m pip install --upgrade pip' command.
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.45:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
^C  Stopping...
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ pwd
/Users/mbachir/programation/MVP_Project/ia_kangourou
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi requirements.txt
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi README.md
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi app.py 
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ cd ../ia_maison
-bash: cd: ../ia_maison: No such file or directory
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ cd ..
(.venv) FRPARMAC0036980:MVP_Project mbachir$ mkdir ia_maison
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi depenses-maison.html
(.venv) FRPARMAC0036980:MVP_Project mbachir$ pwd
/Users/mbachir/programation/MVP_Project
(.venv) FRPARMAC0036980:MVP_Project mbachir$ ls
agent_meteo.py		cv_to_job_2.py		depenses-maison.html	mon_cv.pdf
app_meteo.py		cv_to_job.py		ia_kangourou		old_app.py
app.py			data.db			ia_maison		recherche_profil.py
(.venv) FRPARMAC0036980:MVP_Project mbachir$ vi ia_maison/
(.venv) FRPARMAC0036980:MVP_Project mbachir$ cd ia_maison/
(.venv) FRPARMAC0036980:ia_maison mbachir$ vi depense.html
(.venv) FRPARMAC0036980:ia_maison mbachir$ ls
depense.html
(.venv) FRPARMAC0036980:ia_maison mbachir$ cd ../ia_
ia_kangourou/ ia_maison/    
(.venv) FRPARMAC0036980:ia_maison mbachir$ cd ../ia_kangourou/
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ ls
app.py			README.md		requirements.txt
(.venv) FRPARMAC0036980:ia_kangourou mbachir$ vi app.py 

import random
import time
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch

# ============================================================
# Config
# ============================================================

LABELS = ["A", "B", "C", "D", "E"]
SERIE_LEN = 10
DURATION_SEC = 20 * 60  # 20 min

# ============================================================
# Outils QCM
# ============================================================

def make_mcq(correct, wrongs, n=5):
    pool = [w for w in wrongs if w != correct]
    pool = list(dict.fromkeys(pool))  # unique
    while len(pool) < n - 1:
        pool.append(str(int(correct) + random.randint(2, 15)) if correct.isdigit() else random.choice(wrongs))

    choices = [correct] + random.sample(pool, n - 1)
    random.shuffle(choices)
    return choices, choices.index(correct)

def fig_base():
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    return fig, ax

# ============================================================
# EXERCICES AVEC IMAGES (Kangourou 6e un peu plus corsé)
# Chaque ex: question, choices(5), answer_index, explanation, (optional) draw(ax)
# ============================================================

def ex_grid_area_missing():
    """
    Grille 1x1 : rectangle pavé, un bloc manquant -> aire.
    Style Kangourou: compter vite, éviter de confondre périmètre/aire.
    """
    w = random.randint(6, 10)
    h = random.randint(4, 8)
    # un trou rectangulaire
    hole_w = random.randint(1, max(1, w // 3))
    hole_h = random.randint(1, max(1, h // 3))
    hx = random.randint(1, w - hole_w - 1) if w - hole_w - 1 >= 1 else 0
    hy = random.randint(1, h - hole_h - 1) if h - hole_h - 1 >= 1 else 0

    total = w * h
    hole = hole_w * hole_h
    correct = total - hole

    correct_s = str(correct)
    wrongs = [
        str(total),
        str(hole),
        str(total + hole),
        str((w + h) * 2),  # piège périmètre
        str(correct + 1),
        str(max(0, correct - 1)),
    ]
"app.py" 469L, 16004B
