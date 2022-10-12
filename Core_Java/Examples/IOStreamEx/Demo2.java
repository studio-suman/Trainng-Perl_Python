package IOStreamEx;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Demo2 {
    public static void main(String[] args) {
        try {
        FileReader fr = new FileReader("C:\\Users\\HSASS\\OneDrive - Wipro\\Desktop\\Trainng-Perl_Python\\Core_Java\\Examples\\IOStreamEx\\Source");
        FileWriter fw = new FileWriter("Target");
        int ch;
        while ((ch = fr.read()) != -1) {;
        System.out.print((char)ch);
        fw.write(ch);
        //System.out.print((char)ch);
        }
        fr.close();
        fw.close();
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
