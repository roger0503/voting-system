
nominee_1 = input("Enter nominee 1 name:")
nominee_2 = input("Enter nominee 2 name:")

vote_1 = 0
vote_2 = 0

voters = [1,2,3,4,5,6,7,8,9,10,11]

num_of_voters = len(voters)

while True:
    if voters == []:
        print("Voting session over")
        if vote_1 > vote_2:
            percent_1 = (vote_1 / num_of_voters) * 100
            print(nominee_1,"has won with",percent_1,"% votes")
            break
        elif vote_2 > vote_1:
            percent_2 = (vote_2 / num_of_voters) * 100
            print(nominee_1,"has won with",percent_2,"% votes")
            break
    else:
        vote = int(input("Enter your voter id:"))
        if vote in voters:
            voters.remove(vote)
            print("You are eligible to vote")
            cast_vote = int(input("Enter your choice(1/2):"))
            if cast_vote == 1:
                vote_1 += 1
            elif cast_vote == 2:
                vote_2 += 1
            else:
                print("Nominee doesn't exist!")
        else:
            print("You are not eligible to vote or already voted")
