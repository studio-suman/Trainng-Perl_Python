package Introduction;

public class Demo2StaticBlocks {
    static int count;
    static{
        System.out.println("static block 1");
    }
    {
        System.out.println("block 1");
    }
    
    public Demo2StaticBlocks() {
        count++;
        System.out.println("Constructor");
    }
    {
        System.out.println("block 2");
    }
    public void objectCount() {
        System.out.println("No od Objects are : "+count);
    }
    {
        System.out.println("block 3");
    }
    static{
        System.out.println("static block 2");
    }
    public static void main(String[] args) {
        System.out.println("This is Just the main");
        Demo2StaticBlocks ob1 = new Demo2StaticBlocks();
        ob1.objectCount();
        System.out.println("================================");
        Demo2StaticBlocks ob2 = new Demo2StaticBlocks();
        ob1.objectCount();
        ob2.objectCount();
        for(int i=0;i<4;i++) {
            new Demo2StaticBlocks().objectCount();
        }
        
    }
    {
        System.out.println("block 3");
    }
    static{
        System.out.println("static block 2");
    }
}