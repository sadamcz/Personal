"""Gives a random asl term for me to practice."""

# Setting up random int
import random

# ~~~Unit 1.1~~~
unit_1_1: list[str] = ["Grammar", "Sign fluently", "Ready", "Sign/Signing", "No", "Worksheet", "Culture", "Tap/Tapping(for attention)", "Cilck", "Cool/Neat", "Download", "Dropdown menu", "Parameters", "Practice", "Record/Recording(video)", "Facial Expression", "World", "Spanish", "Gotcha/I see", "Join", "Learn/Learning", "Now/Current", "Hello", "Deaf", "Remember", "Watch", "Homework", "Movie", "Immersion/Immerse", "Yes", "Basic", "Sentence"]

length_unit_1_1: int = 31

# ~~~Unit 1.2~~~
unit_1_2: list[str] = ["Type/Typing", "Grammar", "Sign fluently", "Part(s)/Section(s)", "Review", "Dictionary", "Perfect", "Sign/Signing", "Worksheet", "Attempt", "Click", "Download", "Dropdown Menu", "Handshape", "Non-manual markers (NMM)", "Palm orientation (PO)", "Proximalization", "Record/Recording(video)", "Snapshots", "Upload", "Film", "Move/Movement/Motion", "English", "Correct", "Again", "Forget", "Remember", "Same/Same as", "Different/Differences", "Location", "Watch", "Homework", "Example", "Discuss/Talk/Discussion/Talk about", "Basic", "Sentenece", "Verb", "Try/Tried", "Right", "Wrong", "Error", "Incorrect", "Object(grammar)", "Subject(grammar)", "Video", "Movie", "Place"]

length_unit_1_2: int = 46

#  ~~~Unit 1.3~~~ (I believe this one also contains 1.1 and 1.2)
unit_1_3: list[str] = ["You're Welcome", "How long?", "Question mark", "You and your group", "How do you spell your name?", "Two of you", "You", "I/me", "Her/Him/It/They(singular pronoun)", "Five of you", "Deafblind", "Days of the week", "DeafDisabled", "A to Z", "Feel/Feeling", "What kind/ What type?", "What!", "Computer", "Greetings", "How are you?", "Context", "Welcome to (welcoming the arrival, NOT responding to thanks)", "How many?", "Context", "Greetings", "How are you?", "A group of them", "A group of us", "Assignment is due on..", "Can you please fingerspell that again?", "Can you repeat that?", "Can you please say that again?", "Concept", "What are you doing?", "Don't know", "Don't want", "Eight of them", "Eight of us", "Excuse me", "Five of us", "Four of you", "Four of us", "Good afternoon", "Good evening", "Good morning", "Good night", "Hard of Hearing", "Hers/His/Its/Their", "Don't understand", "I'd like to introduce", "If/suppose", "It(singular pronoun)", "Know", "Later", "May I ask a question?", "Mine/My", "Nice to meet you, too", "Nice to meet you", "Nine of them", "Nine of us", "Not much/Nothing new really/Same as usual", "Internet/Online/Virtual", "Our/Ours", "Please", "Sad", "See you around", "See you on...", "See you soon", "Seven of them", "Seven of us", "He/She/They", "Six of them", "Six of us", "Sorry I don't understand", "Sorry/Apology", "Statement", "Thank you", "Their/Theirs", "They/Them(plural pronoun)", "Three of them", "Three of us", "Two of them", "Two of us", "Kind(category NOT personality)", "Video recording", "Us/We", "Whats new?/Whats happening/Whats up?", "Your/Yours", "Record/Recording (video)", "See you later", "Great(feeling)", "Test", "Fingerspell/Spell", "Class/Classes", "Question", "Error", "Correct", "Want/Want to", "Translate/translation", "Study/Studying", "Now/Current", "Like (positive feeling)", "Dislike/ Don't like", "Again", "Friday", "Monday", "Bye/Goodbye", "Sick/Sickness", "Tired", "Sort of", "Stress/Stressed", "Nervous", "Excited", "Happy", "What", "Good", "Fine", "Hello/Hi", "Night","Evening", "Afternoon", "Noon", "Morning", "Hearing deteriorated(late-deafened)", "Hearing", "Deaf", "How", "Which", "Why", "When", "Where", "Who", "Name", "Homework", "Movie", "Yes", "Done with/Finish", "Saturday", "Sunday", "Thursday", "Tuesday", "Understand", "Wednesday", "Three of you", "Basic", "Sentence", "Repeat", "Right", "Wrong", "Incorrect", "Movie"]

length_unit_1_3: int = 150

# ~~~Unit 1.4~~~
unit_1_4: list[str] = ["Book open", "Book close", "Pencil", "Pick up", "Put down", "Raise-hand", "Teacher", "Student", "Discuss/Talk/Talk about", "Look/Look at/watch", "Stand", "Get up/stand up", "Board", "Write on(board/wall)", "Copy from the board", "Sit/sit down/take a seat", "Word", "Next page/turn the page", "Go to the page/page", "Look it up", "Definition", "Read", "Translate/Translation", "Answer/repy/response", "Check", "Copy/copy to/ copy from", "Picture", "Draw", "Problem", "Brainstorm", "Soultions/solve", "Work", "Group", "Help/I help you/You help me", "Classmate/peer", "Ask", "Question", "Share", "Book", "Dictate", "Sentence"]
length_unit_1_4: int = 40

# ~~~Unit 1.5~~~
unit_1_5: list[str] = ["Math", "Numbers", "Numbers 1-10", "Numbers 10-19", "Numbers 20-29", "Numbers 30-39", "Numbers 40-49", "Numbers 50-59", "Numbers 60-66", "Add/Addition", "Plus", "Altogether/total", "Equal", "Subtract", "con/disadvantage/minus/subtract", "Left/remainder", "Multiple/times", "What(is the answer)?", "Divide/divide by", "Answer", "How many?", "Altogether/total", "Calculating/figure out/figuring out", "Problem"]
length_unit_1_5: int = 23

# ~~~Unit 2.1~~~
unit_2_1: list[str] = ["Nursery", "Child care center/Daycare", "Kindergarten", "Preschool", "Elementary", "Junior High", "Middle School", "High school", "Basic adult education/continuing education", "Vocational school", "Public school", "Charter school", "Parochial school (religious)", "Private school", "Boarding school", "Home school", "Residential school for the deaf", "Regional day school for the deaf", "Grade", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "Freshman", "Sophomore", "Junior", "Senior", "Community college", "College", "University", "Graduate/Graduated/Graduation", "Enroll/Enter", "Law school", "Medical school", "St.", "Gallaudet University"]
length_unit_2_1: int = 40

# ~~~Unit 2.2~~~
unit_2_2: list[str] = ["Gender neutral", "Wheelchair accessible", "Playground", "Class/Classes", "Chalkboard", "Door", "Window", "Chair", "Whiteboard", "Gym", "Admissions office", "Accessibility services", "Asl lab", "Auditorium", "Bathroom", "Bookstore", "Cafeteria", "Campus", "Campus police", "Career center", "Classroom", "Computer lab", "Advising/ Counseling office", "Deans office", "Financial aid office", "Hallway", "Health center", "Library", "Registrars office", "Science lab", "Track and field", "Calculator", "Clock", "Desk", "Eraser", "Paper clip", "Paper", "Pen", "Pencil", "Scissors", "Spiral notebook", "Stapler", "Textbook", "Workbook"]
length_unit_2_2: int = 43

# ~~~Unit 2.3~~~
unit_2_3: list[str] = ["Check", "Label", "Unscramble","Sequence", "True or False", "Compare", "Color / Shade in", "Scribble", "Fill in the blank", "Multiple choice", "Circle (draw a circle)", "Circle (shape)", "Match", "Underline", "Cross out / Strike off", "Take out a piece of paper", "Take out your textbook", "Rip a page out of your notebook", "Put away", "Put back", "Put down", "Put there", "Put under", "Lift", "Carry", "Give", "Enter", "Turn on", "Walk", "Run / Running", "Break", "Buy", "Eat", "Drink", "Gossip", "Discussion / Talk about / Talk", "Go back", "Throw away", "Leave", "Turn off", "Sit / Sit down / Take a seat", "Car breakdown", "Broke (money)", "Spring break", "Class break", "Break up with someone", "Chair and sit", "Example and show", "Scissors and cut"]
length_unit_2_3: int = 48

# ~~~Unit 2.4~~~
unit_2_4: list[str] = ["Major", "Area of study", "Prime minister", "Coach", "Nurse/Nursing", "Cafeteria worker", "Science teacher", "Study/Studying", "Assistant Principal", "Black(color)", "Brown", "Chairperson", "Color", "Coordinator", "Counselor", "Dean", "Faculty", "Gold", "Gray", "Green", "Janitor", "Librarian", "Cream (Off-white color)", "Orange (Color)", "PE teacher", "Pink", "President", "Principal", "Purple", "Red", "Secretary", "Security officer", "Silver", "Staff", "Tan", "Race/Racing", "Vice President", "White(color)", "Worker", "Yellow", "Teacher", "Orange(fruit)"]
length_unit_2_4: int = 41

# ~~~Unit 2.4~~~
unit_2_5: list[str] = ["Drop", "Psychiatry", "Many", "Numbers 100-109", "Numbers 90-99", "Numbers 80-89", "Numbers 70-79", "Numbers 60-69", "Ministry(Governement)", "Masters in Education", "Goal", "Business", "Nurse/Nursing", "English", "Class", "Music/Concert", "Plus", "Done/Finish/Then", "Math", "1 million", "One thousand", "Ten thousand", "One hundred", "One hundred thousand", "Anatomy", "Art", "Associates in arts", "Audiology", "Bachelors of Arts / BS / BSW / BA", "Biology", "Chemistry", "Communication studies", "Computer science", "Counseling", "Culinary arts", "ASL/Deaf studies", "Degree (education)", "PHD", "Drop out/ Dropped out", "Economics", "Education", "Engineering", "Environmental studies", "Full-time", "GED", "Geography", "Government", "Graduate / Graduation", "High school diploma", "History", "Law", "Literature", "Masters degree", "Medical", "On break / On hold", "Part time", "Physics", "Politics", "Psychology", "Reading", "Science", "Semester", "Sign language interpreting", "Social studies", "Sociology", "Speech pathology", "Acting/drama/theater", "Transfer", "Vocational", "Withdraw(school)", "Woodworking", "Writing", "Social work", "Minor"]
length_unit_2_5: int = 73

# ~~~Unit 3.1~~~
unit_3_1: list[str] = ["Adult", "Woman", "Man", "Child", "Children", "Girl", "Boy", "Tall (cha)", "Average (mm)", "Short (po)", "Handsome / Nice looking", "Look different / Unique", "Look-alike/ Look similar", "Beautiful", "Cute", "Look same/ Not aged one bit", "Look great", "Age", "Compliments", "Height"]
length_unit_3_1: int = 19

# ~~~Unit 3.2~~~
unit_3_2: list[str] = ["Fall in love", "Date / Dating", "In a relationship / Steady", "Affair / Cheat", "Argument", "Break up", "Propose", "Engaged", "Bachelor / Bachelorette", "Single", "Gay", "Lesbian", "Relationship on & off", "Wedding", "Marry", "Elope", "Family", "Relatives", "Immediate family", "Extended family", "Grandmother", "Grandfather", "Mother", "Father", "Aunt", "Uncle", "Sister", "Brother", "Cousin", "Mother-in-law", "Father-in-law", "Husband", "Wife", "Sister-in-law", "Brother-in-law", "Daughter", "Son", "Stepdaughter", "Stepson", "Daughter-in-law", "Son-in-law", "Niece", "Nephew", "Divorce", "Single mother", "Single father", "Remarry", "Stepfather", "Stepmother", "Half sister", "Half brother", "Stepsister", "Stepbrother", "Great grandparents", "Godparents", "Pregnant", "Give birth", "Foster", "Adopt", "Weight", "Pounds / Lbs.", "Ounces / Oz.", "Babies / Baby", "Children", "Kids", "Teenagers / Young adults", "Adults", "Senior citizens", "Twins", "Identical twins", "Fraternal twins", "No", "None", "Cat", "Kitten", "Dog", "Puppy", "Rabbit", "Hamster", "Bird", "Fish", "Lizard", "Snake", "Spider", "Turtle", "Ferret", "Pig", "Duck", "Chicken", "Cow", "Horse", "Monkey", "Sheep", "Goat", "Feed pets", "Play with pets", "Exercise with pets", "Sleep with pets", "Talk to your pets", "Hug and kiss your pets", "Pet your pets", "Best friends", "Close friends", "Colleagues", "Acquaintances", "Ex-friends", "CODA", "KODAs", "OHCODA", "SODA", "Age", "Number", "Bi"]
length_unit_3_2: int = 112

# ~~~Unit 3.3~~~
unit_3_3: list[str] = ['Working', 'Internship', 'Student', 'Self employed', 'Part time', 'Full-time', 'Hourly', 'On-call', 'Transfer', 'Promote', 'Retired', 'Fired / Terminated', 'Laid off', 'Out of business', 'Jobless', 'Demote', 'Glass ceiling', 'Stuck', 'Dead-end', 'Quit / Quitter', 'Full', 'Enough']
length_unit_3_3: int = 21

# ~~~Unit 3.4~~~
unit_3_4: list[str] = ["Hard to say", "Birth Certificate", "Certificate/Certification/Certified", "Marines", "Air Force", "Army/Military", "Navy", "Learn to drive", "Drive from", "Drive to", "Certifacte of death", "School", "Put down roots", "Permanent resident card", "Need", "Must", "Marriage License", "As time go by / Later/ Next/Then", "Job", "Immigrant", "Home", "Go there/Go to", "Drive", "Passport", "Buy/Bought", "New", "Birth/born/Childbirth", "Photography/Take pictures", "Plans/Plans/Planned/Planning", "Marriage proposal", "Travel/Traveling/Traveled", "Learn/Learning", "Move (to a different place to live)", "Should", "Citzen/Citzenship", "Die/Pass away", "Driver License", "Get/Got", "Social security card", "Begin/Began", "Uproot", "Volunteer", "Year", "Have to / Had to", "Have/ Has/ Had to", "Retire/Retired", "Baby/Babies", "Marry/Married", "Engaged", "Propose(marriage)", "Start"  ]
length_unit_3_4: int = 50

# Change the second number to the correct length of the unit
i: int = random.randint(0, length_unit_3_3)

print("~~Here is your practice word:~~")
print(unit_3_3[i])
