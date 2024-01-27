#voting system for 30 marker questions

print("Welcome to the student voting system")
                                
class TutorGroup:
    def __init__(self, group_name, num_students, num_candidates):
        self.group_name = group_name
        self.num_students = num_students
        self.num_candidates = num_candidates
        self.candidates = []
        self.votes = {}
        self.voted_students = set()

    def enter_candidates(self):
        for _ in range(self.num_candidates):
            candidate = input("Enter the name of the candidate: ")
            self.candidates.append(candidate)
            self.votes[candidate] = 0
        self.votes['abstain'] = 0

    def vote(self):
        voter_number = input("Enter your unique voter number: ")
        if voter_number in self.voted_students:
            print("You have already voted.")
            return
        self.voted_students.add(voter_number)
        vote = input("Enter the name of the candidate you want to vote for, or 'abstain': ")
        self.votes[vote] += 1

    def display_results(self):
        total_votes = sum(self.votes.values()) - self.votes['abstain']
        for candidate, votes in self.votes.items():
            if candidate != 'abstain':
                percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
                print(f"Candidate: {candidate}, Votes: {votes}, Percentage: {percentage}%")
        print(f"Total votes: {total_votes}, Abstentions: {self.votes['abstain']}")

        winners = [candidate for candidate, votes in self.votes.items() if votes == max(self.votes.values())]
        if len(winners) > 1:
            print("There's a tie. The election will be run again with only the tied candidates.")
            self.candidates = winners
            self.votes = {candidate: 0 for candidate in winners}
            self.votes['abstain'] = 0
            self.voted_students.clear()
        else:
            print(f"The winner is: {winners[0]}")
            
def ask_stuff():
    print("Please enter the name of your tutor group")
    global Group_name 
    Group_name = input()
    print("Please enter the number of students in your tutor group")
    global Num_students 
    Num_students = int(input())
    print("Please enter the number of candidates")
    global Num_candidates 
    Num_candidates= int(input())
    print("Please enter the names of the candidates")
    global Name_candidates 
    Name_candidates = []
    Name_candidates = input()
    return Group_name, Num_students, Num_candidates


print("Welcome to the student voting system")
ask_stuff() 

# Create a TutorGroup instance
group = TutorGroup(Group_name, Num_students, Num_candidates)

# Enter candidates
group.enter_candidates()

# Simulate voting process
for _ in range(group.num_students):
    group.vote()

# Display results
group.display_results()
    










