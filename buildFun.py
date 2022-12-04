class Question:
    def __init__(self, question , answer, row, col, marked, image = None):
        self.question = question
        self.answer = answer
        self.row = row 
        self.image = image
        point = [100,200,300]
        self.rowpoints = point[self.row]
        self.col = col 
        cat = ["player", "world cup 2022", "leagues", "clubs", "icons"]
        self.category = cat[self.col]
        self.mark = marked

Q1 = Question("Who is this player? ", "neymar", 0,0, True, "https://imageio.forbes.com/specials-images/imageserve/627bd53a3a4d3cd7729717cc/0x0.jpg?format=jpg&crop=1069,1070,x707,y83,safe&height=416&width=416&fit=bounds")
Q2 = Question("Who is this player? ", "france", 0,1,True, "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg" )
Q3 = Question("Who is this player? ", "premier league", 0,2, True, "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Lionel_Messi_20180626.jpg/640px-Lionel_Messi_20180626.jpg")
Q4 = Question("Who is this player? ", "ronaldo", 0,3, True, "https://img.fcbayern.com/image/upload/t_cms-1x1-seo/v1657983627/cms/public/images/fcbayern-com/homepage/saison-21-22/Profis/Lewandowski/220716-lewandowski-fc-barcelona.jpg")
Q5 = Question("Who is this player? ", "qatar", 0,4, True, "https://img.a.transfermarkt.technology/portrait/big/139208-1620651710.jpg?lm=1")
Q6 = Question("What country won the last world cup (2018)?", "france", 1,0, True)
Q7 = Question("What country is hosting this years world cup?", "qatar", 1,1, True)
Q8 = Question("What countries were playing in the first match of this years world cup? ", "qatar vs ecuador", 1,2, True)
Q9 = Question("What country has the most World Cups?", "brazil", 1,3, True)
Q10 = Question("What country is know as project blue lock?", "japan" , 1,4, True )
Q11 = Question("From what country is this league?","premier league", 2,0, True,"https://a1.espncdn.com/combiner/i?img=%2Fi%2Fleaguelogos%2Fsoccer%2F500%2F23.png")
Q12 = Question("From what country is this league?","liga mx", 2,1, True, "https://play-lh.googleusercontent.com/m9kMaKhGdSBusRBFKgXyPtJQ94oSYmvKLAMVjfXTeSBw2zgKbDSDohRP2nZHfURTvYA=w600-h300-pc0xffffff-pd")
Q13 = Question("From what country is this league?","liga santander", 2,2, True, "https://www.pngkey.com/png/detail/321-3214718_la-liga-logo.png")
Q14 = Question("From what country is this league?","bundesliga", 2,3, True, "https://1000logos.net/wp-content/uploads/2020/09/Bundesliga-Logo-2010.jpg")
Q15 = Question("From what country is this league?","liga nos",2,4, True, "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Liga_NOS_logo.png/764px-Liga_NOS_logo.png")
Q16 = Question("What club is this?", "paris saint germain",3,0, True, "https://m0.joe.co.uk/wp-content/uploads/2020/09/20203010/psg1.jpg")
Q17 = Question("What club is this?", "barcelona",3,1, True, "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/1200px-FC_Barcelona_%28crest%29.svg.png")
Q18 = Question("What club is this?", "manchester city",3,2, True, "https://cdn.thefootballlovers.com/wp-content/uploads/2021/04/manchester-city.jpg")
Q19 = Question("What club is this?", "borussia dortmant",3,3, True, "http://www.logosquizwalkthrough.com/images/bubble/borussia-dortmund.jpg")
Q20 = Question("What club is this?", "ac milan",3,4, True, "http://www.logosquizwalkthrough.com/images/bubble/ac-milan.jpg")
Q21 = Question("who is this icon?", "pele",4,0,True,"https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Pele_by_John_Mathew_Smith.jpg/1200px-Pele_by_John_Mathew_Smith.jpg")
Q22 = Question("who is this icon?", "maradona",4,1,True,"https://cdn.artphotolimited.com/images/5f60bc53bd40b8173f11e855/1000x1000/diego-maradona-playing-for-argentina-in-1986.jpg")
Q23 = Question("who is this icon?", "ronaldo",4,2,True,"https://cdn.britannica.com/48/142848-050-2A6FC569/Ronaldo-2004.jpg")
Q24 = Question("who is this icon?", "cruyff",4,3, True, "https://fcb-abj-pre.s3.amazonaws.com/img/jugadors/213_cruyff.jpg")
Q25 = Question("who is this icon?", "eusebio", 4,4, True, "https://footballmakeshistory.eu/wp-content/uploads/2020/08/Eusebio.jpg")


'''
#bigger grid if you need it 
realboard = [
             [[Q1], [ Q2], [Q3], [Q4], [Q5]],
             [[Q6], [Q7], [Q8], [Q9], [Q10]],
             [[Q11], [Q12], [Q13], [Q14], [Q15]],
             [[Q15], [Q17], [Q18], [Q19], [Q20]],
             [[Q21], [Q22], [Q23], [Q24], [Q25]]
             ]


'''