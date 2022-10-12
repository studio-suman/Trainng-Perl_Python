package Time_p1;

public class Student { //Super Class Example
    int StudID=101;
    String name = "Allen";
    
    @Override
    public String toString() {
        return StudID + " : "+name;
    }
}