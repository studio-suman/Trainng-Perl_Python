package Introduction;

/*
Write a prWrite a program to find whether a number is Prime or not
[Hint: To convert a command line argument to integer you have to use int i=Integer.parseInt(args[0])]
*/
public class prWrite {

    public static void main(String[] args) {
        
        int i = Integer.parseInt(args[0]);
        int flag = 0;
        int m = 0,y;
        m = i/2;
        for (y = 2; y <= m; y++) {
            if (i%y == 0) {
            System.out.println("The entered no is not Prime: "+i);
            flag = 1;
            break;
            }
        }    
            if(flag == 0) { 
            System.out.println("The entered no is Prime: "+i);
        }  
    }
    
}
