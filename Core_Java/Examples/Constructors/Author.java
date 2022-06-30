package Constructors;

public class Author {
    
    private long authorid;
    private String authorName;
    private String city;
    private String genre;

    public Author() {
        //this("test");
        authorid=100;
        authorName="Empty";
        city="Not Assigned";
        genre="Not Assigned";
        System.out.println("Constructor is called");
    }

    public Author(long authorid, String authorName, String city, String genre) {
        this.authorid = authorid;
        this.authorName = authorName;
        this.city = city;
        System.out.println("Parameterized Constructor Called");
    }
    public Author(String authorName) {
        this();
        this.authorName = authorName;
        System.out.println("Parameterized Constructor Called");
    }
    public long getauthorid() {
        return authorid;
    }
    public void setauthorid(long authorid) {
        this.authorid = authorid;
    }
    public String getauthorName() {
        return authorName;
    }
    public void setauthorName(String authorName) {
        this.authorName = authorName;
    }
    public String getcity() {
        return city;
    }
    public void setcity(String city) {
       // if(course.equalsIgnoreCase("java") || course.equalsIgnoreCase("oracle sql"))
            this.city = city;
    }
    public void acceptData(long aid, String aName, String acity, String agenre) {
        authorid=aid;
        authorName=aName;
        city = acity;
        genre=agenre;
    }
    public void displayData() {
        System.out.println("Participant ["+ authorid+" : " +authorName+ " : " +city+" : " +genre+"]");
        System.out.println("this object : " +this);
    }


}
