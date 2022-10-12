package Threads;

public class Demo2UsingThread extends Thread {
    public Demo2UsingThread() {
        start();
        setPriority(MAX_PRIORITY);
        try {
            join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void run() {
        for (int i = 1; i < 20; i++) {
            System.out.println("From Thread : " + i);
        }
    }
    public static void main(String[] args) {
        Demo2UsingThread ob = new Demo2UsingThread();
        
        ob.start(); try { ob.join(); } catch (InterruptedException e) 
        {
             e.printStackTrace(); 
            }
         
        System.out.println("Demo Completed");
        for (int i = 1; i < 20; i++) {
            System.out.println("From Main : " + i);
            
        }
        Demo2UsingThread ob2 = new Demo2UsingThread();
    }
}