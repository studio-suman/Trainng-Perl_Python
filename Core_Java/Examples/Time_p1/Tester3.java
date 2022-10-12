package Time_p1;
public class Tester3 { //Cosmic/Super Class Example
    public static void main(String[] args) {
        Student ob = new Student();
        System.out.println("HashCode : "+ob.hashCode());
        System.out.println("ToString : "+ob.toString());
        System.out.println("SYSO call : "+ob);
        String val = new String("My Data");
        System.out.println(val);
    }
    }