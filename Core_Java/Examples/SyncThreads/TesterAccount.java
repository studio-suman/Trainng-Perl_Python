package SyncThreads;

public class TesterAccount {
    public static void main(String[] args) {
        Account base = new Account();
        Transaction tr1 = new Transaction(base, 2000, "mother");
        Transaction tr2 = new Transaction(base, 4000, "daughter");
    }
    }
