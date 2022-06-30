package Constructors;
public class Participant {
    private int pId;
    private String pName;
    private String course;
    
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
        System.out.println("This is the object: " +this);
    }
}