package InterThread;

public class Hotel {
    public static void main(String[] args) {
        Order order = new Order();
        Chef c = new Chef(order);
        Waiter w = new Waiter(order);
    }
    
}
