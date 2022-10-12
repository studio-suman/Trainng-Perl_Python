package Introduction;

public class ArgsDemo {
    public static void main(String s[]) {
        System.out.println("No of Arguments Passed: " + s.length);
        for (int i = 0; i < s.length; i++) {
            System.out.println(s[i]);
            System.out.println("Char is  : "+s[i].charAt(0));
        }
        int a = Integer.parseInt(s[0]);
        int b = Integer.parseInt(s[1]);
        System.out.println("Added Result = " + (a + b));
        boolean b1 = Boolean.parseBoolean("TRUE");
        System.out.println(b1);
    }
}