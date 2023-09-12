from textblob import TextBlob

def analyze_mood(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.5:
        return "😃 Super Happy!"
    elif 0.5 >= polarity > 0:
        return "😊 Happy!"
    elif polarity == 0:
        return "😐 Neutral."
    elif -0.5 < polarity < 0:
        return "😞 Sad!"
    else:
        return "😢 Very Sad!"

def main():
    print("Welcome to the Emoji Mood Analyzer!")
    while True:
        user_input = input("Enter a sentence to analyze (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        mood = analyze_mood(user_input)
        print(f"Your mood: {mood}")

if __name__ == "__main__":
    main()

