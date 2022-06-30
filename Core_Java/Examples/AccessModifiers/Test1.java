package AccessModifiers;

public class Test1 {
    public int p1;
    protected int p2;
    int p3; // default
    private int p4;
    
    public void display() {
        System.out.println("From Class Method");
        System.out.println("Public : "+p1);
        System.out.println("Protected : "+p2);
        System.out.println("Default : "+p3);
        System.out.println("Private : "+p4);
    }
    
    public static void main(String[] args) {
        Test1 ob = new Test1();
        ob.display();
        System.out.println("From Main in same class");
        
        System.out.println("Public : "+ob.p1);
        System.out.println("Protected : "+ob.p2);
        System.out.println("Default : "+ob.p3);
        System.out.println("Private : "+ob.p4);
    }
}