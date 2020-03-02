from Game import Game

if __name__ == "__main__":
	g = Game()
	g.play()
	winner = g.getWinner()
	if(winner == None):
		print("Game is a Tie")
	else:
		print("\nTHe Winner is", winner.getName() + "!")