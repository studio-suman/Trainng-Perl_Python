package IOStreamEx;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Demo4Copy {

        public static void main(String[] args) {
            try {
            FileInputStream fis = new FileInputStream("Bird.jpg");
            FileOutputStream fos = new FileOutputStream("MyPet.jpg");
            int bt;
            while((bt = fis.read())!=-1) {
                //System.out.print(bt);
                fos.write(bt);
            }
            fis.close();
            fos.close();
            }catch(IOException e) {
                e.printStackTrace();
            }
            System.out.println("File copied");
            
        }
    }   
