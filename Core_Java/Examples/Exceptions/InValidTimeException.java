package Exceptions;

public class InValidTimeException extends RuntimeException {
    public InValidTimeException() {
        super("InValid Time");
    }
    public InValidTimeException(String msg) {
        super(msg);
    }
}