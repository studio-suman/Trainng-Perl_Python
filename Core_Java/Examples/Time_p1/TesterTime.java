package Time_p1;

/*
Create a class called Time (hh [0-23] , mi  [0 - 59], ss[0-59])
Time t = new Time(23,11,44) ;
syso (t) ; //    23:11:44
try : override equal method of Time class to check whether 2 time are same
Time t1 = new Time(23,11,44) ;
Time t2 = new Time(23,11,44) ;
t1.equals(t2) // return true
public boolean equals (Object ob);
*/
public class TesterTime {
    public static void main(String[] args) {
        Time t1 = new Time();
        Time t2 = new Time(21,65,75);
        Time t3 = new Time(22,6,15);
        System.out.println(t1); // calling the toString method
        //System.out.println(t1.toString());
        System.out.println(t2);
        System.out.println(t3);
        if(t2==t3)
            System.out.println("Both are Same objects");
        else
            System.out.println("They are not same");
        if(t2.equals(t3))
            System.out.println("Both are Same objects");
        else
            System.out.println("They are not same");
        
        /*
         * String h="Hello"; String h1 = "HelloWorld"; // String Constant pool String h2
         * = h+"World"; // "Hello"+"World" System.out.println(h1+ " : "+h2);
         * System.out.println("h1 == h2 : "+(h1==h2)); String h3 = new String("Hello");
         * //create a new memory System.out.println("h == h3 : "+(h==h3));
         * 
         * System.out.println("With Method : "+h.equals(h3));
         */
            
        
    }
}