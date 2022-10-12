package Introduction;

public class Demo1Static {
    public int nVar = 101;
    public static int sVar = 1001;
    
    public void display() {
        System.out.println("Non static method");
        System.out.println("SVar Value : "+sVar);
    }
    public void testCall() {
        display();
        staticCall();
        System.out.println("Test completed");
    }
    
    public static void staticCall() {
        System.out.println("It is Static method");
    }
    
    public static void testStaticCalls() {
        Demo1Static ob = new Demo1Static();
        ob.display();
        System.out.println("N Var : "+ob.nVar);
        System.out.println("Test completed");
    }
    
    public static void main(String[] args) {        //java Demo1Static  // Demo1Static.main(null);
        Demo1Static.testStaticCalls();
        //display();
        /*
         * Demo1Static ob1 = new Demo1Static(); Demo1Static ob2 = new Demo1Static();
         * System.out.println("ob1 nvar : " + ob1.nVar);
         * System.out.println("ob2 nvar : " + ob2.nVar);
         * System.out.println(Demo1Static.sVar); ob1 */

    }     
}    