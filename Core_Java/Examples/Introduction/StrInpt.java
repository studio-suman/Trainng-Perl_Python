package Introduction;

/* Write a Program to accept two Strings Wipro Bangalore as command line  arguments and print the output 
“Wipro Technologies Bangalore” If the command line is “ABC Mumbai”, 
then it should print “ABC Technologies Mumbai” .
*/
public class StrInpt {
    
    public static void main(String s[]){
        System.out.println("Please enter the sentence: \n"); //heading
        String name = System.console().readLine(); //reading out key
        //int len = name.length();
        String[] pname = name.split(" "); // split function
        System.out.println("New Combined Sentence is: "+ pname[0]+" Technologies "+pname[1]);
        //System.console().readLine(); // pause break
    }

}
