package LPTest1;

import java.util.Scanner;

public class Vowels {
   public static void main(String args[]){
      int count = 0;
      System.out.println("Enter a sentence :");
      Scanner sc = new Scanner(System.in);
      String sentence = sc.nextLine();

      for (int i=0 ; i<sentence.length(); i++){
         char ch = Character.toLowerCase(sentence.charAt(i));
         if(ch == 'a'|| ch == 'e'|| ch == 'i' ||ch == 'o' ||ch == 'u'||ch == 'v'){
            count ++;
         }
      }
      sc.close();
      System.out.println("Number of vowels in the given sentence is "+count);
   }
}