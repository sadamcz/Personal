import tkinter as tk
import random
from googlesearch import search
import webbrowser

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

randomwordlist = ["Grammar", "Sign fluently", "Ready", "Sign/Signing", "No", "Worksheet", "Culture", "Tap/Tapping(for attention)", "Cilck", "Cool/Neat", "Download", "Dropdown menu", "Parameters", "Practice", "Record/Recording(video)", "Facial Expression", "World", "Spanish", "Gotcha/I see", "Join", "Learn/Learning", "Now/Current", "Hello", "Deaf", "Remember", "Watch", "Homework", "Movie", "Immersion/Immerse", "Yes", "Basic", "Sentence", "Type/Typing", "Grammar", "Sign fluently", "Part(s)/Section(s)", "Review", "Dictionary", "Perfect", "Sign/Signing", "Worksheet", "Attempt", "Click", "Download", "Dropdown Menu", "Handshape", "Non-manual markers (NMM)", "Palm orientation (PO)", "Proximalization", "Record/Recording(video)", "Snapshots", "Upload", "Film", "Move/Movement/Motion", "English", "Correct", "Again", "Forget", "Remember", "Same/Same as", "Different/Differences", "Location", "Watch", "Homework", "Example", "Discuss/Talk/Discussion/Talk about", "Basic", "Sentenece", "Verb", "Try/Tried", "Right", "Wrong", "Error", "Incorrect", "Object(grammar)", "Subject(grammar)", "Video", "Movie", "Place","You're Welcome", "How long?", "Question mark", "You and your group", "How do you spell your name?", "Two of you", "You", "I/me", "Her/Him/It/They(singular pronoun)", "Five of you", "Deafblind", "Days of the week", "DeafDisabled", "A to Z", "Feel/Feeling", "What kind/ What type?", "What!", "Computer", "Greetings", "How are you?", "Context", "Welcome to (welcoming the arrival, NOT responding to thanks)", "How many?", "Context", "Greetings", "How are you?", "A group of them", "A group of us", "Assignment is due on..", "Can you please fingerspell that again?", "Can you repeat that?", "Can you please say that again?", "Concept", "What are you doing?", "Don't know", "Don't want", "Eight of them", "Eight of us", "Excuse me", "Five of us", "Four of you", "Four of us", "Good afternoon", "Good evening", "Good morning", "Good night", "Hard of Hearing", "Hers/His/Its/Their", "Don't understand", "I'd like to introduce", "If/suppose", "It(singular pronoun)", "Know", "Later", "May I ask a question?", "Mine/My", "Nice to meet you, too", "Nice to meet you", "Nine of them", "Nine of us", "Not much/Nothing new really/Same as usual", "Internet/Online/Virtual", "Our/Ours", "Please", "Sad", "See you around", "See you on...", "See you soon", "Seven of them", "Seven of us", "He/She/They", "Six of them", "Six of us", "Sorry I don't understand", "Sorry/Apology", "Statement", "Thank you", "Their/Theirs", "They/Them(plural pronoun)", "Three of them", "Three of us", "Two of them", "Two of us", "Kind(category NOT personality)", "Video recording", "Us/We", "Whats new?/Whats happening/Whats up?", "Your/Yours", "Record/Recording (video)", "See you later", "Great(feeling)", "Test", "Fingerspell/Spell", "Class/Classes", "Question", "Error", "Correct", "Want/Want to", "Translate/translation", "Study/Studying", "Now/Current", "Like (positive feeling)", "Dislike/ Don't like", "Again", "Friday", "Monday", "Bye/Goodbye", "Sick/Sickness", "Tired", "Sort of", "Stress/Stressed", "Nervous", "Excited", "Happy", "What", "Good", "Fine", "Hello/Hi", "Night","Evening", "Afternoon", "Noon", "Morning", "Hearing deteriorated(late-deafened)", "Hearing", "Deaf", "How", "Which", "Why", "When", "Where", "Who", "Name", "Homework", "Movie", "Yes", "Done with/Finish", "Saturday", "Sunday", "Thursday", "Tuesday", "Understand", "Wednesday", "Three of you", "Basic", "Sentence", "Repeat", "Right", "Wrong", "Incorrect", "Book open", "Book close", "Pencil", "Pick up", "Put down", "Raise-hand", "Teacher", "Student", "Discuss/Talk/Talk about", "Look/Look at/watch", "Stand", "Get up/stand up", "Board", "Write on(board/wall)", "Copy from the board", "Sit/sit down/take a seat", "Word", "Next page/turn the page", "Go to the page/page", "Look it up", "Definition", "Read", "Translate/Translation", "Answer/repy/response", "Check", "Copy/copy to/ copy from", "Picture", "Draw", "Problem", "Brainstorm", "Solutions/solve", "Work", "Group", "Help/I help you/You help me", "Classmate/peer", "Ask", "Question", "Share", "Book", "Dictate", "Sentence", "Math", "Numbers", "Numbers 1-10", "Numbers 10-19", "Numbers 20-29", "Numbers 30-39", "Numbers 40-49", "Numbers 50-59", "Numbers 60-66", "Add/Addition", "Plus", "Altogether/total", "Equal", "Subtract", "con/disadvantage/minus/subtract", "Left/remainder", "Multiple/times", "What(is the answer)?", "Divide/divide by", "Answer", "How many?", "Altogether/total", "Calculating/figure out/figuring out", "Problem", "Nursery", "Child care center/Daycare", "Kindergarten", "Preschool", "Elementary", "Junior High", "Middle School", "High school", "Basic adult education/continuing education", "Vocational school", "Public school", "Charter school", "Parochial school (religious)", "Private school", "Boarding school", "Home school", "Residential school for the deaf", "Regional day school for the deaf", "Grade", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "Freshman", "Sophomore", "Junior", "Senior", "Community college", "College", "University", "Graduate/Graduated/Graduation", "Enroll/Enter", "Law school", "Medical school", "St.", "Gallaudet University","Gender neutral", "Wheelchair accessible", "Playground", "Class/Classes", "Chalkboard", "Door", "Window", "Chair", "Whiteboard", "Gym", "Admissions office", "Accessibility services", "Asl lab", "Auditorium", "Bathroom", "Bookstore", "Cafeteria", "Campus", "Campus police", "Career center", "Classroom", "Computer lab", "Advising/ Counseling office", "Deans office", "Financial aid office", "Hallway", "Health center", "Library", "Registrars office", "Science lab", "Track and field", "Calculator", "Clock", "Desk", "Eraser", "Paper clip", "Paper", "Pen", "Pencil", "Scissors", "Spiral notebook", "Stapler", "Textbook", "Workbook", "Check", "Label", "Unscramble","Sequence", "True or False", "Compare", "Color / Shade in", "Scribble", "Fill in the blank", "Multiple choice", "Circle (draw a circle)", "Circle (shape)", "Match", "Underline", "Cross out / Strike off", "Take out a piece of paper", "Take out your textbook", "Rip a page out of your notebook", "Put away", "Put back", "Put down", "Put there", "Put under", "Lift", "Carry", "Give", "Enter", "Turn on", "Walk", "Run / Running", "Break", "Buy", "Eat", "Drink", "Gossip", "Discussion / Talk about / Talk", "Go back", "Throw away", "Leave", "Turn off", "Sit / Sit down / Take a seat", "Car breakdown", "Broke (money)", "Spring break", "Class break", "Break up with someone", "Chair and sit", "Example and show", "Scissors and cut","Major", "Area of study", "Prime minister", "Coach", "Nurse/Nursing", "Cafeteria worker", "Science teacher", "Study/Studying", "Assistant Principal", "Black(color)", "Brown", "Chairperson", "Color", "Coordinator", "Counselor", "Dean", "Faculty", "Gold", "Gray", "Green", "Janitor", "Librarian", "Cream (Off-white color)", "Orange (Color)", "PE teacher", "Pink", "President", "Principal", "Purple", "Red", "Secretary", "Security officer", "Silver", "Staff", "Tan", "Race/Racing", "Vice President", "White(color)", "Worker", "Yellow", "Teacher", "Orange(fruit)", "Drop", "Psychiatry", "Many", "Numbers 100-109", "Numbers 90-99", "Numbers 80-89", "Numbers 70-79", "Numbers 60-69", "Ministry(Governement)", "Masters in Education", "Goal", "Business", "Nurse/Nursing", "English", "Class", "Music/Concert", "Plus", "Done/Finish/Then", "Math", "1 million", "One thousand", "Ten thousand", "One hundred", "One hundred thousand", "Anatomy", "Art", "Associates in arts", "Audiology", "Bachelors of Arts / BS / BSW / BA", "Biology", "Chemistry", "Communication studies", "Computer science", "Counseling", "Culinary arts", "ASL/Deaf studies", "Degree (education)", "PHD", "Drop out/ Dropped out", "Economics", "Education", "Engineering", "Environmental studies", "Full-time", "GED", "Geography", "Government", "Graduate / Graduation", "High school diploma", "History", "Law", "Literature", "Masters degree", "Medical", "On break / On hold", "Part time", "Physics", "Politics", "Psychology", "Reading", "Science", "Semester", "Sign language interpreting", "Social studies", "Sociology", "Speech pathology", "Acting/drama/theater", "Transfer", "Vocational", "Withdraw(school)", "Woodworking", "Writing", "Social work", "Minor", "Adult", "Woman", "Man", "Child", "Children", "Girl", "Boy", "Tall (cha)", "Average (mm)", "Short (po)", "Handsome / Nice looking", "Look different / Unique", "Look-alike/ Look similar", "Beautiful", "Cute", "Look same/ Not aged one bit", "Look great", "Age", "Compliments", "Height", "Fall in love", "Date / Dating", "In a relationship / Steady", "Affair / Cheat", "Argument", "Break up", "Propose", "Engaged", "Bachelor / Bachelorette", "Single", "Gay", "Lesbian", "Relationship on & off", "Wedding", "Marry", "Elope", "Family", "Relatives", "Immediate family", "Extended family", "Grandmother", "Grandfather", "Mother", "Father", "Aunt", "Uncle", "Sister", "Brother", "Cousin", "Mother-in-law", "Father-in-law", "Husband", "Wife", "Sister-in-law", "Brother-in-law", "Daughter", "Son", "Stepdaughter", "Stepson", "Daughter-in-law", "Son-in-law", "Niece", "Nephew", "Divorce", "Single mother", "Single father", "Remarry", "Stepfather", "Stepmother", "Half sister", "Half brother", "Stepsister", "Stepbrother", "Great grandparents", "Godparents", "Pregnant", "Give birth", "Foster", "Adopt", "Weight", "Pounds / Lbs.", "Ounces / Oz.", "Babies / Baby", "Children", "Kids", "Teenagers / Young adults", "Adults", "Senior citizens", "Twins", "Identical twins", "Fraternal twins", "No", "None", "Cat", "Kitten", "Dog", "Puppy", "Rabbit", "Hamster", "Bird", "Fish", "Lizard", "Snake", "Spider", "Turtle", "Ferret", "Pig", "Duck", "Chicken", "Cow", "Horse", "Monkey", "Sheep", "Goat", "Feed pets", "Play with pets", "Exercise with pets", "Sleep with pets", "Talk to your pets", "Hug and kiss your pets", "Pet your pets", "Best friends", "Close friends", "Colleagues", "Acquaintances", "Ex-friends", "CODA", "KODAs", "OHCODA", "SODA", "Age", "Number", "Bi",'Working', 'Internship', 'Student', 'Self employed', 'Part time', 'Full-time', 'Hourly', 'On-call', 'Transfer', 'Promote', 'Retired', 'Fired / Terminated', 'Laid off', 'Out of business', 'Jobless', 'Demote', 'Glass ceiling', 'Stuck', 'Dead-end', 'Quit / Quitter', 'Full', 'Enough', "Hard to say", "Birth Certificate", "Certificate/Certification/Certified", "Marines", "Air Force", "Army/Military", "Navy", "Learn to drive", "Drive from", "Drive to", "Certifacte of death", "School", "Put down roots", "Permanent resident card", "Need", "Must", "Marriage License", "As time go by / Later/ Next/Then", "Job", "Immigrant", "Home", "Go there/Go to", "Drive", "Passport", "Buy/Bought", "New", "Birth/born/Childbirth", "Photography/Take pictures", "Plans/Plans/Planned/Planning", "Marriage proposal", "Travel/Traveling/Traveled", "Learn/Learning", "Move (to a different place to live)", "Should", "Citzen/Citzenship", "Die/Pass away", "Driver License", "Get/Got", "Social security card", "Begin/Began", "Uproot", "Volunteer", "Year", "Have to / Had to", "Have/ Has/ Had to", "Retire/Retired", "Baby/Babies", "Marry/Married", "Engaged", "Propose(marriage)", "Start"]  

def random_new_frame():
    for widget in root.winfo_children():
        widget.destroy()

    i = random.randint(0, len(randomwordlist) - 1)
    search_query = randomwordlist[i] + " in ASL"

    rchosen = tk.Label(root, text=search_query, font=("Arial", 36))
    rchosen.place(x=470, y=150, height=100, width=1000)

    googlesearch = []

    for j in search(search_query, tld="co.in", num=1, stop=1, pause=1):
        googlesearch.append(j)

    # goggles = tk.Text(root, font=("Arial", 30))
    # goggles.insert(tk.END, "\n".join(googlesearch))
    # goggles.place(x=470, y=450, height=100, width=1000)

    seeanswer = tk.Button(root, text="SEE ANSWER", font=('Arial', 30), command=lambda: see_answer(googlesearch[0]))
    seeanswer.place(x=470, y=700, height=100, width=1000)

    backbutt = tk.Button(root,text="BACK", font=("Arial", 10), command=lambda: backfunction())
    backbutt.place(x=100, y=50, height= 50, width=60)

    exitbutt= tk.Button(root, text="EXIT", font=("Arial", 10), command=lambda: exit())
    exitbutt.place(x=200, y=50, height= 50, width=60)

def see_answer(search_url):
    webbrowser.open(search_url)

def search_new_frame():
    for widget in root.winfo_children():
        widget.destroy()

    myentry = tk.Entry(root, font=("Arial", 36))
    myentry.place(x=470, y=150, height=100, width=1000)

    enterbutton = tk.Button(root, text="ENTER", font=("Arial", 36),command=lambda: getinput(myentry))
    enterbutton.place(x=800, y=600, height=200, width=300)

    exitbutt= tk.Button(root, text="EXIT", font=("Arial", 10), command=lambda: exit())
    exitbutt.place(x=200, y=50, height= 50, width=60)
    

    

def getinput(myentry):
    search_query = myentry.get() + " in ASL"
    
    googlesearch = []

    for j in search(search_query, tld="co.in", num=1, stop=1, pause=1):
        googlesearch.append(j)

    # goggles = tk.Text(root, font=("Arial", 30))
    # goggles.insert(tk.END, "\n".join(googlesearch))
    # goggles.place(x=470, y=450, height=100, width=1000)

    seeanswer = tk.Button(root, text="SEE ANSWER", font=('Arial', 30), command=lambda: see_answer(googlesearch[0]))
    seeanswer.place(x=700, y=300, height=100, width=500)

    backbutt = tk.Button(root,text="BACK", font=("Arial", 10), command=lambda: backfunction())
    backbutt.place(x=100, y=50, height= 50, width=60)

    exitbutt= tk.Button(root, text="EXIT", font=("Arial", 10), command=lambda: exit())
    exitbutt.place(x=200, y=50, height= 50, width=60)

def backfunction():
    for widget in root.winfo_children():
        widget.destroy()

    start_label = tk.Label(root, text="ASL PRACTICE APPLICATION", font=("Arial", 48))
    start_label.pack()
    start_label.place(x=470, y=150, height=100, width=1000)

    randomword = tk.Button(root, text="RANDOM WORD", font=("Arial", 18), command=random_new_frame)
    searchword = tk.Button(root, text="SEARCH WORD", font=("Arial", 18), command=search_new_frame)
    randomword.place(x=800, y=350, height=200, width=300)
    searchword.place(x=800, y=600, height=200, width=300)

    exitbutt= tk.Button(root, text="EXIT", font=("Arial", 10), command=lambda: exit())
    exitbutt.place(x=200, y=50, height= 50, width=60)




root = tk.Tk()
root.title("ASL PRACTICE")
root.geometry("1920x1080")

start_label = tk.Label(root, text="ASL PRACTICE APPLICATION", font=("Arial", 48))
start_label.pack()
start_label.place(x=470, y=150, height=100, width=1000)

exitbutt= tk.Button(root, text="EXIT", font=("Arial", 10), command=lambda: exit())
exitbutt.place(x=200, y=50, height= 50, width=60)

randomword = tk.Button(root, text="RANDOM WORD", font=("Arial", 18), command=random_new_frame)
searchword = tk.Button(root, text="SEARCH WORD", font=("Arial", 18), command=search_new_frame)
randomword.place(x=800, y=350, height=200, width=300)
searchword.place(x=800, y=600, height=200, width=300)


root["bg"] = "#F1EB9C"
root.mainloop()