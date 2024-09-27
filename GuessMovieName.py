import random

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    tmp=[]
    for i in range(n):
        if(letters[i]==' '):
            tmp.append(' ')
        else:
            tmp.append('_')
    qn=''.join(str(i) for i in tmp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if(c==0):
        return False
    else:
        return True

def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    tmp=[]
    n=len(movie)
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            tmp.append(ref[i])
        else:
            if(qn_list[i]=='_'):
                tmp.append('_')
            else:
                tmp.append(ref[i])
    qn_new=''.join(str(i) for i in tmp)
    return qn_new
def play():
    p1name=input("Player 1,Please enter your name:")
    p2name=input("Player 2,Please enter your name:")
    pp1=0
    pp2=0
    turn =0
    willing=True
    while(willing):
        if(turn%2==0):
            print(p1name,' Your turn')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while(not_said):
                letter=input("Your letter: ")
                letter=letter.lower()
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to to guess the movie\nPress 2 to unlock another letter"))
                    if(d==1):
                        ans=input("The correct movie is:")
                        ans=ans.lower()
                        if(ans==picked_movie):
                            pp1+=10
                            print("That's the correct movie!!")
                            not_said=False
                            print(p1name,' Your score is:',pp1)

                        else:
                            print("That's not the correct movie!!\nTry again!!")
                            pp1 -= 5
                    elif(d==2):
                        pp1-=1
                        continue
                else:
                    print(letter,' not found!!')
                    pp1 -= 1
                c=int(input("Press 1 to continue\nPress 0 to quit"))
                if(c==0):
                    print(p1name,' your score :',pp1)
                    print(p2name,' your score :',pp2)
                    print("Thanks for playing!!")
                    willing=False
                    not_said = False
        else:
            print(p2name, ' Your turn')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while (not_said):
                letter = input("Your letter: ")
                letter=letter.lower()
                if (is_present(letter, picked_movie)):
                    modified_qn = unlock(modified_qn, picked_movie,letter)
                    print(modified_qn)
                    d = int(input("Press 1 to to guess the movie\nPress 2 to unlock another letter"))
                    if (d == 1):
                        ans = input("The correct movie is:")
                        ans=ans.lower()
                        if (ans == picked_movie):
                            pp2 += 10
                            print("That's the correct movie!!")
                            not_said = False
                            print(p2name, ' Your score is:', pp2)
                        else:
                            print("That's not the correct movie!!\nTry again!!")
                            pp2 -= 5

                    elif (d == 2):
                        pp2-=1
                        continue
                else:
                    print(letter, ' not found!!')
                    pp2 -= 1
                c = int(input("Press 1 to continue\nPress 0 to quit"))
                if (c == 0):
                    print(p1name, ' your score :', pp1)
                    print(p2name, ' your score :', pp2)
                    print("Thanks for playing!!")
                    willing = False
                    not_said = False

        turn+=1


movies_list = [
    'Baahubali The Conclusion',
    'Naa Peru Surya',
    'Mahanati',
    'Ala Vaikunthapurramuloo',
    'Jersey',
    'Sarileru Neekevvaru',
    'Geetha Govindam',
    'Rangasthalam',
    'Padi Padi Leche Manasu',
    'Radhe Shyam',
    'Fidaa',
    'Bharat Ane Nenu',
    'Sarrainodu',
    'Penguin',
    'Remo',
    'Dhruva',
    'Goodachari',
    'Bhale Bhale Magadivoy',
    'Shyam Singha Roy',
    'Jathi Ratnalu',
    'Varsham',
    'Darling'
]

movies=[]
for i in range(len(movies_list)):
    movies.append(movies_list[i].lower())
play()