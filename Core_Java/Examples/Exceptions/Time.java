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

public class Time {
    private int hh; 
    private int mi;
    private int ss;
    public int getHh() {
        return hh;
    }
    public void setHh(int hh)throws Exception{
        if(hh >=0 && hh <=23)
            this.hh = hh;
        else {
            this.hh = 0;
            InValidTimeException e = new InValidTimeException("invalid Hour");
            throw e; 
        }   
    }
    public int getMi() {
        return mi;
    }
    public void setMi(int mi) throws Exception {
        if(mi >=0 && mi <=59)
        this.mi = mi;
        else if (mi > 59) {
            //hh=hh+(mi/60);
            setHh(hh+(mi/60));
            this.mi=mi%60;
        }
        else {
            this.mi = 0;
            InValidTimeException e = new InValidTimeException("Invalid Minutes");
            throw e; 
        }     
    }
    public int getSs() {
        return ss;
    }
    public void setSs(int ss) throws Exception {
        if(ss >=0 && ss <=59)
        this.ss = ss;
        else if(ss > 59) {
            //mi=mi+(ss/60);
            setMi(mi+(ss/60));
            this.ss=ss%60;
        }
        else {
            this.ss = 0;
            InValidTimeException e = new InValidTimeException("Invalid Seconds");
            throw e; 
        }     
    }
    public Time() {
        hh=0;mi=0;ss=0;
    }
    public Time(int hh, int mi, int ss) throws Exception {
        setHh(hh);
        setMi(mi);
        setSs(ss);
    }
    @Override
    public String toString() {
        return hh+":"+mi+":"+ss;
    }
    
    public boolean equals(Object o) { 
        if( this == o) // t1.equals(t1)
        {
            return true;
        }
        if (o instanceof Time) { //Time t = new Time() ; String s1="hello"; t.equals(s1)
            Time t = (Time)o;
            if(this.hh == t.hh && this.mi == t.mi && this.ss == t.ss) 
                return true;
            else
                return false;
            /*
             * if(this.hh != t.hh || this.mi != t.mi || this.ss != t.ss) return false; else
             * return true;
             */
        }
        return false;
    }
    
    
}
