package AccessModifiers2;

import AccessModifiers.Test1;
public class Test5 extends Test1{
    public void mydisplay() {
        System.out.println("From child Class Method");
        System.out.println("Public : "+p1);
        System.out.println("Protected : "+p2);
        //System.out.println("Default : "+p3);//default is not accessible to child classes outside the package
        //System.out.println("Private : "+p4);
    }
    
    public static void main(String[] args) {
        Test5 ob = new Test5();
        ob.display();
        System.out.println("From Main in same class");
        
        System.out.println("Public : "+ob.p1);
        System.out.println("Protected : "+ob.p2);
        //System.out.println("Default : "+ob.p3);
        //System.out.println("Private : "+ob.p4);
    }
}