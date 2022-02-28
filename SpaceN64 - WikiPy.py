# ------------------------
# | WikiPy - By SpaceN64 |
# ------------------------

# Classifying
pysummary = ["pysum", "PySum", "Pysum"]
exit = ["Exit", "exit", "Exit()", "exit()", "Leave", "leave", "Leave()", "leave()"]

# Def - pysum
def pysum():
    sentence = int
    sentence = input("""Summarize into how many sentences?
    
>>> """)
    article = input("""What is the article name?
    
>>> """)
    try:
        wiki.summary(article, sentences=sentence)
        print(wiki.summary(article, sentences=sentence))
        t.sleep(0.5)
        main()
    except wiki.exceptions.DisambiguationError:
        search = wiki.search(article)
        print(article)
        main()
    except wiki.exceptions.PageError as l:
        print("""
Page not found! Try searching using a keyword!""")
        t.sleep(1)
        main()
    main()


#imports
import wikipedia as wiki
import time as t
import random as r

# Boot / joking around lmao
print("Booting up...")
t.sleep(1.6)
print("Indexing...")
t.sleep(1.6)
print("")

# Title
print("""
██╗    ██╗██╗██╗  ██╗██╗██████╗ ██╗   ██╗
██║    ██║██║██║ ██╔╝██║██╔══██╗╚██╗ ██╔╝
██║ █╗ ██║██║█████╔╝ ██║██████╔╝ ╚████╔╝ 
██║███╗██║██║██╔═██╗ ██║██╔═══╝   ╚██╔╝  
╚███╔███╔╝██║██║  ██╗██║██║        ██║   
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                                         
""")
t.sleep(1.4)

# Intro
print("""
Welcome to WikiPy!

     This is a python program that uses the module "Wikipedia" to give access to all the articles of 
Wikipedia onto a python file!

    To search something up, type in the name of it; or alternativly, you can use the "pysum" 
command to summerize the article that you want showed into how little sentences you want.""")
t.sleep(0.7)

def main():
    print("")
    prompt = input(">>> ")
    if prompt in pysummary:
        pysum()
    elif prompt in exit:
        print("""
Thanks for using WikiPy!""")
        t.sleep(1)
        exit()
    else:
        try:
            print("")
            wiki.summary(prompt)
        except wiki.exceptions.DisambiguationError as g:
            search = wiki.search(prompt)
            print(search)
            main()
        except wiki.exceptions.PageError as l:
            print("Page not found! Try searching using a keyword!")
            t.sleep(1)
            main()
        print(wiki.summary(prompt))
    main()
main()
