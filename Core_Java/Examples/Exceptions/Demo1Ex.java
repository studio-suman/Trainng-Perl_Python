package Exceptions;
public class Demo1Ex { //Exception Handling
    public static void main(String[] args) {
        try {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            int c = a / b;
            System.out.println("Result = " + c);
        }catch(ArithmeticException e) {
            System.out.println(e.getMessage());
            System.out.println("Please Enter non zero for denominator");
        }catch(ArrayIndexOutOfBoundsException e) {
            System.out.println("Please enter values @ Command Line");
        }catch(Exception e) {
            System.out.println("Something went wrong : "+e.getMessage());
        }
        finally {
            System.out.println("Program Terminated");
        }
    }
}
/*
 * catch(Exception e){ System.out.println(e.getMessage()); //to handle the
 * exception System.out.println(e); e.printStackTrace();//to learn the exception
 * }
 */