package chapter10;

public interface Subscription {
    void request(long n);

    void cancel();

}
