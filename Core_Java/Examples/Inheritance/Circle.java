package Inheritance;
//import java.sql.Connection;

public class Circle implements IShape, IColor {

    int radius;

    public Circle() {
        this.radius = 1;
    }

    public Circle(int radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return PI * radius * radius;
    }

    @Override
    public double perimeter() {
        // TODOAuto-generated method stub
        return 2 * PI * radius;
    }

    @Override
    public void fill() {
        System.out.println("its filled with blue");

    }

    @Override
    public void border() {
        System.out.println("Border with red");
    }

/*    
    @Override
    public Connection getConnection() {
        System.out.println("method to connct to DB");
        return null;
    }
*/
}