def convert(text):
    text = text.replace(":)", "☺️")
    text = text.replace(":(", "☹️")
    return text

def main():
     text = input("Enter emoticons: ")
     print(convert(text))

main()