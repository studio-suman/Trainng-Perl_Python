package Exceptions;

/*
Create a class called Time (hh [0-23] , mi  [0 - 59], ss[0-59])
Time t = new Time(23,11,44) ;
syso (t) ; //    23:11:44
try : override equal method of Time class to check whether 2 time are same
Time t1 = new Time(23,11,44) ;
Time t2 = new Time(23,11,44) ;
t1.equals(t2) // return true
public boolean equals (Object ob);
*/
public class TesterTime {
    public static void main(String[] args) {
        try {
            Time t1 = new Time(12,-45,44);
            System.out.println(t1);
        }catch(Exception e) {
            e.printStackTrace();
        }
        
    }
    }