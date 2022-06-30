package IOStreamEx;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
public class Demo5ObjectRead {
    public static void main(String[] args) {
        FileInputStream fis;
        try {
            fis = new FileInputStream("Student.txt");
            ObjectInputStream ois = new ObjectInputStream(fis);
            Student ob = (Student)ois.readObject();//James
            System.out.println(ob);
             ob = (Student)ois.readObject();//Raman
                System.out.println(ob);
            ois.close();
            fis.close();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        
        
    }
}