package InterThread;

public class Waiter extends Thread {
    Order order;
    public Waiter(Order order) {
        this.order = order;
        start();
    }
    
    public void run() {
        for(int i=1;i<=10;i++) {
            order.serve();
            try {
                sleep(150);
            }catch(InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}    