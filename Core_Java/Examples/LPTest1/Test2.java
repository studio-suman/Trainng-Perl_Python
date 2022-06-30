package LPTest1;

public class Test2 {
    public static void main(String[] args) throws InterruptedException {
        
        String  str = new String("Hello World");
        str = null;
        System.gc();
        Thread.sleep(5000);

    }
}
