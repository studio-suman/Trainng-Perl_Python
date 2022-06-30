package Threads;

public class Demo4Sleep extends Thread{
    int sleeptime=0;
    public Demo4Sleep() {
        start();
    }
    public Demo4Sleep(String name) {
        super(name);
        start();
    }
    public Demo4Sleep(String name,int sl) {
        super(name);
        sleeptime = sl;
        start();
    }
    public void run() {
        for(int i=1;i<21;i++) {
            System.out.println("From "+getName()+" : "+i);
            try {
                sleep(sleeptime);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    public static void main(String[] args) {
        Demo4Sleep ob = new Demo4Sleep("T1",300);
        Demo4Sleep ob1 = new Demo4Sleep("T2" , 500);
    }
}