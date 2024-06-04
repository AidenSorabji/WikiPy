import wikipedia as wiki
import time,os,sys
 
exitp = ["Exit", "exit"]

# Clear Terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Delay Print
def delay_print(ayo):
    for nak in ayo:
        sys.stdout.write(nak)
        sys.stdout.flush()
        time.sleep(0.6)

# Summery
def summery():
    sum_searcho = input("Search for Article: ")
    try:
        sum_article_chooser = "elbow"
        sumsum = wiki.summary(sum_searcho)
        print("")
        sum_article_chooser = sum_article_chooser.replace("elbow",sum_searcho)
    except wiki.exceptions.PageError as l:
        sum_search = wiki.search(sum_searcho)
        resulto = ', '.join(sum_search)
        print("""
    Search Results:""")
        print("      " + resulto)
        print("")
        sum_article_chooser = input("Choose a Article: ")
        print("")
    except wiki.exceptions.DisambiguationError as g:
        sum_search = wiki.search(sum_searcho)
        resulto = ', '.join(sum_search)
        print("""
    Search Results:""")
        print("      " + resulto)
        print("")
        sum_article_chooser = input("Choose a Article: ")
        print("")


    sum_sentence_amount = input("Amount of Summerized Sentences: ")

    time.sleep(1)
    print("")
    delay_print(". . .")
    time.sleep(1.3)

    clear()

    sum_output = wiki.summary(sum_article_chooser,sum_sentence_amount)

    print("      " + sum_output)
    after()

# Random
def random():
    time.sleep(1)
    print("")
    delay_print(". . .")
    time.sleep(1.3)

    clear()

    random_article = wiki.random()

    random_page = wiki.page(random_article)

    print(random_page.title)
    print("")
    print("     " + random_page.content)
    after()

# After
def after():
    print("")
    time.sleep(1)
    main()


# Title
print("""
██╗    ██╗██╗██╗  ██╗██╗██████╗ ██╗   ██╗
██║    ██║██║██║ ██╔╝██║██╔══██╗╚██╗ ██╔╝
██║ █╗ ██║██║█████╔╝ ██║██████╔╝ ╚████╔╝ 
██║███╗██║██║██╔═██╗ ██║██╔═══╝   ╚██╔╝  
╚███╔███╔╝██║██║  ██╗██║██║        ██║   
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                                         
""")
time.sleep(1.4)

# Intro
print("""
Welcome to WikiPy!

     This is a python program that uses the module "Wikipedia" to give access to all the articles of 
Wikipedia onto a python file!

    To search something up, type in the name of it; or alternativly, you can use the "summery()" 
command to summerize the article that you want showed into how little sentences you want.""")
time.sleep(0.7)
print("")

# Main
def main():
    prompt = input(">>> ")
    if prompt in "summery()":
        summery()
    elif prompt in "random()":
        random()
    elif prompt in exitp:
        exit
    else:
        try:
            actual_article = "oil"
            search = wiki.summary(prompt)
            actual_article = actual_article.replace("oil",prompt)
        except wiki.exceptions.PageError as a:
            searchy_search = wiki.search(prompt)
            small_search = ', '.join(searchy_search)
            print("""
Search Results:""")
            print("      " + small_search)
            print("")
            actual_article = input("Choose a Article: ")
        except wiki.exceptions.DisambiguationError as b:
            searchy_search = wiki.search(prompt)
            small_search = ', '.join(searchy_search)
            print("""
Search Results:""")
            print("      " + small_search)
            print("")
            actual_article = input("Choose a Article: ")
    
        time.sleep(1)
        print("")
        delay_print(". . .")
        time.sleep(1.3)

        categoriesp = ["categories", "Categories", "category", "Category"]
        contentp = ["content", "Content"]
        linkp = ["link", "Link", "links", "Links"]
        referencesp = ["references", "References", "reference", "Reference"]
        summaryp = ["summary", "Summary", "summery", "Summery"]
        page_spreadp = ["page_spread", "Page_spread", "Page_Spread", "page_Spread"]


        page = wiki.page(actual_article)

        clear()

        print(page.original_title)
        print("")

        ackrack = page.content

        print("      " + ackrack)

        def sec_prompt_activate():
            print("")
            time.sleep(2)

            print("")
            print("Secondary Commands: exit = exits, categories = shows categories, content = shows content")
            print("                    links = shows links, references = shows references, summary = summerizes")
            print("                    page_spread = goes to page spread")
            print("")
            third_prompt = input(">>> ")

            if third_prompt in exitp:
                main()

            elif third_prompt in categoriesp:
                clear()

                categorie = page.categories
                categorie = ', '.join(categorie)

                print(categorie)

                sec_prompt_activate()
            
            elif third_prompt in contentp:
                clear()

                contento = page.content
                contento = ', '.join(contento)

                print(contento)

                sec_prompt_activate()
            
            elif third_prompt in linkp:
                clear()

                linkso = page.links
                linkso = ', '.join(linkso)

                print(linkso)

                sec_prompt_activate()
            
            elif third_prompt in referencesp:
                clear()

                referenceo = page.references
                referenceo = ', '.join(referenceo)

                print(referenceo)

                sec_prompt_activate()

            elif third_prompt in summaryp:
                clear()

                summo = page.summary

                print("     " + summo)

                sec_prompt_activate()
            
            elif third_prompt in page_spreadp:
                clear()

                def suming():
                    print(page.original_title)
                    print("")

                    butoto = page.content

                    print("      " + butoto)

                    sec_prompt_activate()

                suming()

            else:
                print("bruh")

                sec_prompt_activate()

        print("")
        time.sleep(2)

        print("")
        print("Secondary Commands: exit = exits, categories = shows categories, content = shows content")
        print("                    links = shows links, references = shows references, summary = summerizes")
        print("                    page_spread = goes to page spread")
        print("")
        second_prompt = input(">>> ")

        if second_prompt in exitp:
            clear()

            print("""    To search something up, type in the name of it; or alternativly, you can use the "summery()" 
command to summerize the article that you want showed into how little sentences you want.""")
            print("")
            
            main()

        elif second_prompt in categoriesp:
            clear()

            categorie = page.categories
            categorie = ', '.join(categorie)

            print(categorie)

            sec_prompt_activate()
        
        elif second_prompt in contentp:
            clear()

            contento = page.content
            contento = ', '.join(contento)

            print(contento)

            sec_prompt_activate()
        
        elif second_prompt in linkp:
            clear()

            linkso = page.links
            linkso = ', '.join(linkso)

            print(linkso)

            sec_prompt_activate()
        
        elif second_prompt in referencesp:
            clear()

            referenceo = page.references
            referenceo = ', '.join(referenceo)

            print(referenceo)

            sec_prompt_activate()

        elif second_prompt in summaryp:
            clear()

            summo = page.summary

            print("     " + summo)

            sec_prompt_activate()
        
        elif second_prompt in page_spreadp:
            clear()

            def suming():
                print(page.original_title)
                print("")

                butoto = page.content

                print("      " + butoto)

                sec_prompt_activate()

            suming()

        else:
            print("bruh")

        def sec_prompt_activate():
            print("")
            time.sleep(2)

            print("")
            print("Secondary Commands: exit = exits, categories = shows categories, content = shows content")
            print("                    links = shows links, references = shows references, summary = summerizes")
            print("                    page_spread = goes to page spread")
            print("")
            third_prompt = input(">>> ")

            if third_prompt in exitp:
                clear()

                print("""    To search something up, type in the name of it; or alternativly, you can use the "summery()" 
command to summerize the article that you want showed into how little sentences you want.""")
                print("")
                
                main()

            elif third_prompt in categoriesp:
                clear()

                categorie = page.categories
                categorie = ', '.join(categorie)

                print(categorie)

                sec_prompt_activate()
            
            elif third_prompt in contentp:
                clear()

                contento = page.content
                contento = ', '.join(contento)

                print(contento)

                sec_prompt_activate()
            
            elif third_prompt in linkp:
                clear()

                linkso = page.links
                linkso = ', '.join(linkso)

                print(linkso)

                sec_prompt_activate()
            
            elif third_prompt in referencesp:
                clear()

                referenceo = page.references
                referenceo = ', '.join(referenceo)

                print(referenceo)

                sec_prompt_activate()

            elif third_prompt in summaryp:
                clear()

                summo = page.summary

                print("     " + summo)

                sec_prompt_activate()
            
            elif third_prompt in page_spreadp:
                clear()

                def suming():
                    print(page.original_title)
                    print("")

                    butoto = page.content

                    print("      " + butoto)

                    sec_prompt_activate()

                suming()

            else:
                print("bruh")

                sec_prompt_activate()
                    
        sec_prompt_activate()
main()
