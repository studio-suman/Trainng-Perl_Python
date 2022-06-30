package IOStreamEx;

import java.io.Serializable;
import java.util.Date;
public class Student implements Serializable{
    private int sid;
    private String sname;
    private String course;
    private Date creationDate;
    public Student() {
        
    }
    public Student(int sid, String sname, String course, Date creationDate) {
        this.sid = sid;
        this.sname = sname;
        this.course = course;
        this.creationDate = creationDate;
    }
    public int getSid() {
        return sid;
    }
    public void setSid(int sid) {
        this.sid = sid;
    }
    public String getSname() {
        return sname;
    }
    public void setSname(String sname) {
        this.sname = sname;
    }
    public String getCourse() {
        return course;
    }
    public void setCourse(String course) {
        this.course = course;
    }
    public Date getCreationDate() {
        return creationDate;
    }
    public void setCreationDate(Date creationDate) {
        this.creationDate = creationDate;
    }

    @Override
    public String toString() {
        return "Student [sid=" + sid + ", sname=" + sname + ", course=" + course + ", creationDate=" + creationDate
                + "]";
    }
    

    
}