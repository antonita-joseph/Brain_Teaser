//This is the prototype file for the game in JAVA
import java.util.*;
public class Main
{
	public static void main(String[] args) {
		char choice, numb, lett;
		String[] choices = {"L", "N"};
		int count = 5, corr = 0, input;
    Scanner s = new Scanner(System.in);
    Random r = new Random();
    
		for(int i = 0; i<count; i++){
		    System.out.println("Letter: Vowel - 1, Consonant - 2");
		    System.out.println("Number: Even - 1, Odd - 2");

        // Random generation of alphabets and numbers
		    lett = (char) (r.nextInt(26) + 'A');
		    numb = (char) (r.nextInt(9) + '1');

        // Recording choices for future verifications
		    if(choices[r.nextInt(choices.length)] == "L"){
		        choice = 'L';
		        System.out.println("LETTER");
		    }
		    else{
		        System.out.println("NUMBER");
		        choice = 'N';
		    }
      
        // Changing the order of alphabet and number 
        // Not yet randomized
		    if((int)numb % (i+1) == 0)
		        System.out.println(numb+" "+lett);
		    else 
		        System.out.println(lett+" "+numb);

        // Getting the input from user
		    input = s.nextInt();
        //Matching the question and the user input
		    if(choice == 'L'){
		        if(input == 1 ){
		            if(lett == 'A' || lett == 'E' || lett == 'I' || lett == 'O' || lett == 'U')
		                corr++;
		        }
		        else if(input == 2 ){
		            if(lett != 'A' && lett != 'E' && lett != 'I' && lett != 'O' && lett != 'U')
		                corr++;
		        }
		    }
		    else if(choice == 'N'){
		        if(input == 1 ){
		            if(numb % 2 == 0)
		                corr++;
		        }
		        else if(input == 2 ){
		            if(numb % 2 == 1)
		                corr++;
		        }
		    }
        //A pause before cleaning the screen for a new question
		    try{ Thread.sleep(500);} 
        catch(Exception e){
          System.out.println("There is an error is Thread.Sleep");
        }
		    System.out.print("\033[H\033[2J");
        System.out.flush();
		}
    // Final Verdict of the test
		System.out.println("You have completed your test !");
		System.out.println("Your score is:" + corr);
		System.out.println("Your attention percent is:" + (((double)corr/count)*100) + "%");

    // FUTURE ASPECTS:
    // Can make the number of rounds dynamic
    // Can claculate time taken for each
    // Can list the time taken 
    // Modify accuracy based on both time and correctness
    // Can include a DB to maintain score of each trial
	}
}
