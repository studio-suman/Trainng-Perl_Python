package InterThread;

public class Chef extends Thread{
    Order order;
    public Chef(Order order) {
        this.order = order;
        start();
    }
    public void run() {
        for(int i=1;i<=10;i++) {
            order.cook(i);
            try {
                sleep(300);
            }catch(InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
