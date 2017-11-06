/*
 * NewOrleansSolver.java
 * DESCRIPTION:
 * This program will allow its user to solve the "Great Big House in New Orleans" game,
 * played by the students of Miss Jenny Bowman at Scottish Corners Elementary School.
 * The program will give the user the exact position at which they must sit in order to win.
 * 
 * NOTE:
 * I realized an interesting detail while developing this program, which regards the initial
 * position of the "pumpkin". This program assumes that at the very start of the game, the
 * pumpkin is passed to the student at position 2. In other words, the student at position
 * 2 is the one who first sings "Great big...", and position 9 will be the first to get out
 * (if there are at least 9 students playing). In another version of the game, the person who
 * starts with the pumpkin will be the first to sing "Great big...", resulting in position 8
 * getting out first. That version is not simulated by this project.
 * 
 * @author Michael Zeng
 * @version 20170710
 */

import java.util.Scanner;

public class NewOrleansSolver {

	public static void main(String[] args) {
		printIntro();
		Scanner keyboard = new Scanner(System.in);
		boolean playAgain = true;
		while (playAgain) {
			
			int classSize = getClassSize(keyboard);
			int[] classArray = new int[classSize];
			for (int i = 0; i < classArray.length; i++) {
				classArray[i] = i+1;
			}
			int currentStudent = 1; //this is the student who currently has the ball
			int studentOut = 0;
			while (!isGameOver(classArray)) {
				studentOut = nextOut(classArray, currentStudent);
				classArray[studentOut-1] = 0;//sets the next student to get out to 0 in the class array
				currentStudent = studentOut;
			}
			
			final int WINNER = findWinner(classArray);
			final int POSITIONS_RIGHT = WINNER - 1;
			outputWinner(WINNER, POSITIONS_RIGHT);
			
			keyboard.nextLine();
			playAgain = promptPlayAgain(keyboard);
			
		}
		
		System.out.println("Have a great day!");
	}
	
	private static int getClassSize(Scanner in) {
		int sizeOfClass = 0;
		System.out.print("How many people will be playing today?: ");
		sizeOfClass = in.nextInt();
		while (sizeOfClass <= 1) {
			if (sizeOfClass < 0) {
				System.out.println("ERROR: Really? You can't have a negative class size.");
				System.out.println("I know you're in elementary school, but surely you must know this.");
			} else {
				System.out.println("ERROR: There must be at least 2 people in your class in order to play.");
			}
			
			System.out.print("How many people will be playing today?: ");
			sizeOfClass = in.nextInt();
		}
		return sizeOfClass;
	}
	
	private static boolean isGameOver(int[] theClass) {
		//checks whether only one student is left in the game, and if so, returns true
		boolean gameOver = false;
		int studentsLeft = 0;//number of students still in the game
		for (int i = 0; i < theClass.length; i++) {
			if (theClass[i] != 0) {//checks whether student is out or not ('0' means out)
				studentsLeft++;//if not out, increments number of students still in
			}
		}
		if (studentsLeft == 1) {//if only one student left in, the game is over
			gameOver = true;
		}
		return gameOver;
	}
	
	private static int nextStudent(int[] theClass, int current) {
		//returns the next nonzero (i.e. still "in") student
		int student = 0;
		int studentWithBall = current;
		while (student == 0) {
			if (studentWithBall < theClass.length) {
				studentWithBall = studentWithBall + 1;
				if (theClass[studentWithBall-1] != 0) {//is the next student still in? if so, return the number. if not, keep 0.
					student = studentWithBall;
				}
			}
			else if (studentWithBall >= theClass.length) {//if it's the last person in the circle...
				studentWithBall = 1;//...return to position 1
				if (theClass[studentWithBall-1] != 0) {//is the person at position 1 still in? if so, return their number.
					student = studentWithBall;
				}
			}	
		}
		return student;
	}
	
	private static int nextOut(int[] theClass, int current) {//returns the next student to get out
		int out = current;
		for (int i = 0; i < 8; i++) {
			out = nextStudent(theClass, out);
		}
		return out;
	}
	
	private static int findWinner(int[] theClass) {
		int winner = 0, i = 0;
		while (winner == 0) {
			if (theClass[i] != 0) {
				winner = theClass[i];
			}
			else {
				i++;
			}
		}
		return winner;
	}
	
	private static void printIntro() {
		System.out.println("*****");
		System.out.println("Great Big House in New Orleans,");
		System.out.println("Forty stories hi-gh,");
		System.out.println("Every room that I've been in,");
		System.out.println("Filled with pumpkin pi-e.");
		System.out.println("*****");
		System.out.println("Welcome! This program will tell you where you need "
				+ "to sit in order to win \"Great Big House in New Orleans\".");
		System.out.println("First, we'll need one piece of information from you.");
		System.out.println("*****");
	}
	
	private static void outputWinner(final int THEWINNER, final int POSITIONS) {
		System.out.println("Position " + THEWINNER + " will win.");
		System.out.println("You must sit " + POSITIONS + " position(s) to the right of the student who starts with the pumpkin to win.");
		System.out.println("(Assuming the pumpkin is passed to the right every time.)");
		System.out.println();
		System.out.println("Congratulations! You won a B.U.G. Award!!! :)");
	}
	
	private static boolean promptPlayAgain(Scanner in) {
		boolean play = false;
		System.out.print("Would you like to play again? (y/n): ");
		String nextPlay = in.nextLine();
		while (!nextPlay.equals("y") && !nextPlay.equals("n")) {
			System.out.println("Error detected. \""+nextPlay+"\" not recognized.");
			System.out.print("Would you like to play again? (y/n): ");
			nextPlay = in.nextLine();
		}
		if (nextPlay.equals("n")) {
			play = false;
		} else if (nextPlay.equals("y")) {
			play = true;
			System.out.println("Playing again...");
			System.out.println("*****");
		}
		return play;
	}

}
