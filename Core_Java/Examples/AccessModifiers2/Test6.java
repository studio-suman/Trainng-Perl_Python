package AccessModifiers2;

public class Test6 {
    public static void main(String[] args) {
        Test5 ob = new Test5();
        ob.display();
        System.out.println("From Main in same class");
        
        System.out.println("Public : "+ob.p1);
        //System.out.println("Protected : "+ob.p2); // not accessible outside the child class
        //System.out.println("Default : "+ob.p3);
        //System.out.println("Private : "+ob.p4);
    }
}