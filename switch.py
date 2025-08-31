lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript" | "javascript" | "Javascript" | "Java Script":
        print("You can become a web developer.")

    case "Python" | "python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity" | "solidity":
        print("You can become a Blockchain developer")

    case "Java" | "java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
