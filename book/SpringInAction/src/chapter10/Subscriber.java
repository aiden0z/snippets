package chapter10;

public interface Subscriber<T> {
    void onSubscribe(Subscription sub);

    void onNext(T item);

    void onError(Throwable ex);

    void onComplete();

}
