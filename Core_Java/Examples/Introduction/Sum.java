package Introduction;

/*
Write a program that will accept a 4 digit number(assume that the user enters only 4 digit nos.) and print the sum of all the 4 digits. For ex : 
If the number passed is 3629, the program should print “The sum of all the digits entered is 20”
*/

public class Sum {
    public static void main(String[] args) {

        System.out.print("Enter the number: ");
        String name = System.console().readLine();
        int sum = 0;
        int arr[] = new int[name.length()];
        int counter =0;
        for (int y =0; y<name.length(); y++) {
            arr[counter] = Integer.parseInt(name.charAt(y)+"");
            counter++;
            }
        for(int ele : arr) {
            sum+=ele;
            }
        System.out.println("Sum = "+sum);
    }
}
