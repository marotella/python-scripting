def createStory(adjective, noun , verb):
    story = "The " + adjective + noun + verb
    print(story)
    
    
def getElements():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    createStory(adjective, noun, verb)
    

getElements()