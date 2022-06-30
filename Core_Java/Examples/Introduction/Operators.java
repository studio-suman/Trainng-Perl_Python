package Introduction;

public class Operators{
    public static void main(String s[]){
        System.out.println("Hello World !!! ");
        char ch = 'A'; //Char 'A' = 65
        int iVal1=10;
        String ename = "Suman";
        System.out.println(ch+" : "+iVal1+" : "+ename);
        iVal1+=20; // is same as => iVal1 = iVal1 + 20;
        ch++;
        ename+=" Saha";
        System.out.println(ch+" : "+iVal1+" : "+ename);
        int x = ch; //implicit Conversion
        System.out.println(x);
        ch = 103;
        x  = ch;
        System.out.println(x);
        x = 103;
        ch = (char)x; //Explicit Conversion
        System.out.println(x);
    }
}
