package Inheritance;
@FunctionalInterface
public interface Adder {
    public void sum();
    int var = 12;
    default void test() {
        System.out.println("tested");
    }
    static void ontTime() {
        System.out.println("One time");
    }
    String toString(); //method of object 
}