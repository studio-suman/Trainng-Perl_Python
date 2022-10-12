package SyncThreads;

public class Account {
    int AccID;
    double balance = 10000;

    public void withdraw(int amt) {
        System.out.println("Opening Balace : "+balance);
        balance-=amt;
        System.out.println("Current Balance : "+balance);
    }
    
    public synchronized void withdraw2(int amt) {
        System.out.println("Opening Balace : "+balance);
        balance-=amt;
        System.out.println("Current Balance : "+balance);
    }
}
