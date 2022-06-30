package SyncThreads;

public class Transaction implements Runnable {
    Account account;
    Thread thread;
    int wamt;
    public Transaction(Account account ,int wamt, String name) {
        thread = new Thread(this,name);
        this.account = account;
        this.wamt = wamt;
        thread.start();
    }
    
    @Override
    public void run() {
        synchronized (account) {
            account.withdraw(wamt);
        }
    /*
    @Override
    public void run() {
        //account.withdraw2(wamt);
        /*
         * Example of Synchronized block
         * 
         
        synchronized (account) 
        { 
            account.withdraw2(wamt);} */
    }

    }
    

