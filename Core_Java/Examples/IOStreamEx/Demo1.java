package IOStreamEx;

import java.util.Scanner;

public class Demo1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Output Mesage");
        System.err.println("Error Message");
        sc.close();
    }
}
