package IOStreamEx;

import java.io.FileReader;
import java.io.IOException;

public class Demo3 {
    public static void main(String[] args) {
        try {
        FileReader fr = new FileReader("C:\\Users\\HSASS\\OneDrive - Wipro\\Desktop\\Trainng-Perl_Python\\Core_Java\\Examples\\IOStreamEx\\Source");
        int ch;
        while ((ch = fr.read()) != -1) {;
        System.out.print((char)ch);
        }
        fr.close();
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }

}
