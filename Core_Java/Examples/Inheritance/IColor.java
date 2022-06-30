package Inheritance;
import java.sql.Connection;
public interface IColor {
    public void fill();
    //public void border();//new addition
    default void border() {
        System.out.println("If required override this method");
    }
    //cannot override the static
    static Connection getConnection() {
        System.out.println("method to connct to DB");
        return null;
    }
}
