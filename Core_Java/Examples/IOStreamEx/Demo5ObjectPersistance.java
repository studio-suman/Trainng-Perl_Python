package IOStreamEx;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.Date;
public class Demo5ObjectPersistance {
public static void main(String[] args) {
    Student st = new Student(103, "Raman", "Java", new Date());
    System.out.println(st);
    try {
    FileOutputStream fos = new FileOutputStream("Student.txt",true);
    ObjectOutputStream oos = new ObjectOutputStream(fos);
    oos.writeObject(st);
    oos.close();
    fos.close();
    }catch(IOException e) {
        e.printStackTrace();
    }
    
    
}
}
