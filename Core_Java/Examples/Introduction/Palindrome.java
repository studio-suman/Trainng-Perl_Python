package Introduction;

/*
Write a program to accept a String from the command prompt and display whether the string is a palindrome or not.
[Hint :You have to extract each character from the beginning and end of the String 
and compare it with each other.  
String x=”Malayalam”; char c= x.charAt(i) where i is the index]
*/

public class Palindrome {
    
    public static void main(String[] args) {

        String x = "Malayalam", b="";
        for (int i =x.length()-1; i>=0; i--) {
            b = b + x.charAt(i);
            
        }
        if (x.equalsIgnoreCase(b))
            {  
                System.out.println("This String is Palindrome: "+x);

            }       
        else 
        {  
            System.out.println("This String is not a Palindrome: "+x);

        }    

    }
}   
