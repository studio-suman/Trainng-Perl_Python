package Constructors;
public class ConstructorTester {
    public static void main(String[] args) {
        Participant2 pobj = new Participant2(102, "Martin", "Java");
        pobj.displayData();
        System.out.println("=============================");
        Participant2 pobj2 = new Participant2("Gopalan");
        pobj2.displayData();
    }
}

