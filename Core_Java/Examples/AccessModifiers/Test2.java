package AccessModifiers;

public class Test2 {
    public static void main(String[] args) {
        Test1 ob = new Test1();
        ob.display();
        System.out.println("From Main Different class Same Package");
        
        System.out.println("Public : "+ob.p1);
        System.out.println("Protected : "+ob.p2);
        System.out.println("Default : "+ob.p3);
        //System.out.println("Private : "+ob.p4); private not accessible outside the class
    }
}