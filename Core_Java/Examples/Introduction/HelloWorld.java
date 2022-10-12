package Introduction;

import org.junit.Test;

// Write a program to print "Hello World" on Console.

public class HelloWorld{
    @Test
    public static void main(String s[]){
        System.out.println("Hello World !!! ");
        String name = System.console().readLine();
        System.out.println("Hello World !!! "+name);

        String x = "Malayalam";
        for (int i = 0; i<=x.length()-1; i++) {
            for (int j = x.length()-1;i<j ; j--) {
            if (x.charAt(i) == x.charAt(j)) {

                System.out.println("This String is Palindrome: "+x);
            }  
            }       
        }
        
    }
}