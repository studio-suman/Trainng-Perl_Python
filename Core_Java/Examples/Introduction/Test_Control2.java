package Introduction;

public class Test_Control2 {
    public static void main(String[] args) {
        boolean flag = false;
        while (flag) {
            System.out.println("Inside While");
        }
        
        //Unreachable Code Compiletime Error
        /*
         * while (false) { System.out.println("Inside While"); }
         */
        System.out.println("While Done");

            //temp variable i : life time is only with in the for loop block
            for(int i=0;i<11;i++) {
                System.out.println("i = "+i);
                for(int j=100;j<100;j+=5) {
                    System.out.println("i = "+i+j);
            }
        }  
    }
}     
