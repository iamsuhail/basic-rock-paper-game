import random
def play():
    user = input("what's ur choice? (r) for rock, (p) for paper,(s) for scissors: \n")
    computer = random.choice(['r','p','s'])
    print(f"your choice was : {user}")
    print(f"computer's choice was : {computer}")

    if user == computer:
        return 'tie'

    if is_win(user,computer):
        return 'you won!'
    
    return 'you lost!'

def is_win(player,opponent):
    #return true if player wins 
    # r>s s>p p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
    

print(play())