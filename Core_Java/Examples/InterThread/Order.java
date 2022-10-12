package InterThread;

public class Order {
    int id;
    public synchronized void cook(int id) {
        while(this.id!=0) {
            try {
                wait();
            } catch (InterruptedException e) {
                // Auto-generated catch block
                e.printStackTrace();
            }
        }
        this.id=id;
        System.out.println("Cooked : "+id);
        notify();
    }
    
    public synchronized void serve() {
        while(id==0) {
            try {
                wait();
            } catch (InterruptedException e) {
                // Auto-generated catch block
                e.printStackTrace();
            }
        }
        System.out.println("Served : "+id);
        id=0;
        notify();
    }
}
