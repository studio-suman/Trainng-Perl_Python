package LPTest1;



public class Test {

    public static String findtheOrderString (String input1, String input2) {
    
        /*
        input1 = ACZa
        input2 = CAZa
        output = Increasing
        */

        int a=0, counter = 0;
        char b;
        do {
            b = input1.charAt(a);
            if((int)b < (int)(b-1)) {
                counter++;
            }
            else counter = 0;
        a++;
        } while (a < input1.length());
        
        if(counter != 0) {return "True";}
        else return "False";
        
    }       


public static void main(String[] args) {
    
    //System.out.println("Please enter 2 inputs: \n"); //heading
    //String input = System.console().readLine(); //reading out key
    //int len = name.length();
    //String[] pinput = input.split(" ");

    //System.out.println(pinput[0]);
    //System.out.println(pinput[1]);

    String input1 = "ACZa";
    String input2 = "CAZa";

    String s = findtheOrderString(input1,input2);
    
    if (s == "True") {
        System.out.println("Increasing Order:");
    } else System.out.println("No Order");
}

}