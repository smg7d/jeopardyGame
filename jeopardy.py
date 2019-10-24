class player():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __repr__(self):
        return (str(self.name) + ": " + str(self.score))

class board():
    def __init__(self, categories, questions, answers):
        self.categories = categories #a dictionary of category names and positional columns 1-6
        self.questions = questions #a 5x6 matrix of questions in order from left to right, top to bottom
        self.answers = answers #a 5x6 matrix of answers in order from left to right, top to bottom
        self.values = [x for x in [100, 200, 300, 400, 500]]

    def setCategories(self, categories):
        #create the thing
        #categories should just be a list of strings of the various categories
        #self.categories = the thing

    def setQuestions(self, categories):
        #create the thing
        #self.categories = the thing

    def setanswers(self, categories):
        #create the thing
        #self.categories = the thing

class game():
    def __init__(self):
        #get the player names
        #get the API data
        #initialize the board
        #set gameOver = false
        #display categories
        #choose which player picks first

    def runTurn(self):
        #display score/status and board
        #get next question location
            #if out of range or selected, display out of range
        #display the question
            #if daily double
        #get the winner
        #add the score
        #mark the location as visited
        #

    def run(self):
        #while game over is not false
        #do another turn
        
        #at the end, display, game over, winner and stats
        


if __name__ == "__main__":
    #this is to test the module
    playerA = player("Shane")
    print(playerA)

    tempMatrix = [[]]
    columns = 6
    rows = 5
    values = [100, 200, 300, 400, 500]
    for i in range(columns):
        for j in range(rows):
            tempMatrix[i][j] = values[i]