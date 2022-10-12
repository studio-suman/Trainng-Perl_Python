package Introduction;

public class Demo1Final {
    final int check=10;
    final int v1;
    public Demo1Final() {
        //check=101;
        v1=10;
    }
    public Demo1Final(int v) {
        //this();
        v1=v;
    }
    
    public final void testMe() {
        System.out.println("From demo1");
    }
    
    public static void main(String[] args) {
        Demo1Final ob = new Demo1Final();
        //ob.check = 202;
        System.out.println(ob.check);
    }
}