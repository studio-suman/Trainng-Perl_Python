package Constructors;
public class Participant2 {
    private int pId;
    private String pName;
    private String course;
    
    public Participant2() {
        //this("test");
        pId=100;
        pName="Empty";
        course="Not Assigned";
        System.out.println("Constructor is called");
    }


/**
     * Overloaded or parameterized Constructors
     */
    public Participant2(int pId, String pName, String course) {
        this.pId = pId;
        this.pName = pName;
        this.course = course;
        System.out.println("Parameterized Constructor Called");
    }
    public Participant2(String pName) {
        this();
        this.pName = pName;
        System.out.println("Parameterized Constructor Called");
    }
    public int getpId() {
        return pId;
    }
    public void setpId(int pId) {
        this.pId = pId;
    }
    public String getpName() {
        return pName;
    }
    public void setpName(String pName) {
        this.pName = pName;
    }
    public String getCourse() {
        return course;
    }
    public void setCourse(String course) {
        if(course.equalsIgnoreCase("java") || course.equalsIgnoreCase("oracle sql"))
            this.course = course;
        else
            System.out.println("Invalid Course");
    }
    public void acceptData(int id, String name, String crs) {
        pId=id;
        pName=name;
        course = crs;
    }
    public void displayData() {
        System.out.println("Participant ["+ pId+" : " +pName+ " : " +course+"]");
        System.out.println("this object : " +this);
    }
}