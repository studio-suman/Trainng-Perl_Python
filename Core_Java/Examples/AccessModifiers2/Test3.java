package AccessModifiers2;

import AccessModifiers.Test1;
public class Test3 {
    public static void main(String[] args) {
        Test1 ob = new Test1();
        ob.display();
        System.out.println("From Main in different class in  different package");
        
        System.out.println("Public : "+ob.p1);
        /*
         * Except for the Public data other are not visible
        System.out.println("Protected : "+ob.p2);
        System.out.println("Default : "+ob.p3);
        System.out.println("Private : "+ob.p4);
        */
    }
}