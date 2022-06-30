package Constructors;

public class Book {
    public static void main(String[] args) {
        Author pobj = new Author(1021232434, "Mark Twain", "London","Kids");
        pobj.displayData();
        System.out.println("=============================");
        Author pobj2 = new Author("Gopalan");
        pobj2.displayData();
    }
}