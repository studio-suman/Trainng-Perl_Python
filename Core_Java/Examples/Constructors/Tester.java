package Constructors;
public class Tester {
    public static void main(String[] args) {
        Participant participant;// created an object reference variable
        participant=null;
        System.out.println(participant);
        participant = new Participant(); // Instantiation : Object is created
        System.out.println(participant);
        /*
         * It Private Data members are not accessible ouside the class
         * participant.pId = 1001; participant.pName="Scott"; participant.course="Java";
         * participant.displayData();
         */
        participant.acceptData(2002, "Allen", "Oracle SQL");
        participant.displayData();
        participant.setCourse("Java");
        participant.displayData();
    }
}