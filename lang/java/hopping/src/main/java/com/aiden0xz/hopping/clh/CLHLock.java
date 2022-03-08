package com.aiden0xz.hopping.clh;


import java.util.concurrent.atomic.AtomicReference;

public class CLHLock implements Lock {

    /**
     * 尾巴，所有线程共用的一个变量。每个线程进来后，把自己设置为tail，方便下一时刻线程获取前驱节点
     */
    private final AtomicReference<QNode> tail;
    /**
     * 用于线程保存前驱节点，每个线程独有一个。
     */
    private final ThreadLocal<QNode> predNodeThreadLocal;
    /**
     * 用户线程保存当前节点，每个线程独有一个。
     */
    private final ThreadLocal<QNode> myNodeThreadLocal;

    public CLHLock() {
        // 给一个初始值，此时既是尾巴也是头，默认false，所以第一个抢占的线程将直接执行，因为前驱是false
        this.tail = new AtomicReference<>(new QNode());
        // get时当前线程没有值则返回一个新的QNode
        this.myNodeThreadLocal = ThreadLocal.withInitial(QNode::new);
        // 初始化当前节点保存前驱节点的ThreadLocal
        this.predNodeThreadLocal = new ThreadLocal<>();
    }

    @Override
    public void lock() {
        // 获取当前线程的节点
        // ThreadLocal 操作，无线程竞争问题
        QNode node = this.myNodeThreadLocal.get();
        // 设置为 True 表示已锁状态
        node.locked = true;
        // 将自己设置到队列末尾，并且返回之前的末尾节点表示为前驱几点
        // !!! CAS 无锁操作，解决线程竞争问题
        QNode pred = tail.getAndSet(node);
        // 设置前驱节点
        // ThreadLocal 操作，无线程竞争问题
        this.predNodeThreadLocal.set(pred);
        // 自旋等待前驱节点解锁
        while(pred.locked) {
        }
    }

    @Override
    public void unlock() {
        QNode node = this.myNodeThreadLocal.get();
        node.locked = false;

        // 防止死锁。如果没有下一句，若当前线程unlock后迅速竞争到锁，由于当前线程还保存着自己的 node,
        // 所以`QNode node = this.myNodeThreadLocal.get();`获取的依旧是该线程的node(此时该node还被链表的下一个节点引用)，
        // 执行lock后把自己的locked = true然后把自己又加在尾部，然而链表的下一个节点还在等该线程的locked = false而当前节点还
        // 在等自己之前的节点locked = false，1->3->2 1在等2执行,2在等3执行,3又必须让1先执行完。
        // 所以防止上述事情的发生，释放锁时不能允许当前线程还保存自己的node，防止该线程再次抢占线程发生死锁。

        // 此时处理方式有三种：（问题出在该线程又竞争到锁的时候，也就是该线程连续两次抢到锁）
        // (1)、this.myNodeThreadLocal.set(null);
        // (2)、this.myNodeThreadLocal.set(new CLHNode());
        // (3)、this.myNodeThreadLocal.set(predNodeThreadLocal.get());
        // 三种比较，对于1、2中QNode node = this.myNodeThreadLocal.get();
        // 本线程都会获取新的node,然而在第二次抢到锁lock()时
        // QNode pred = tail.getAndSet(node);this.predNodeThreadLocal.set(pred);
        // 会设置新的前驱node导致该线程之前的旧前驱preNode对象没有任何引用，所以当下一次会被GC掉。
        // 因此在3中不用重新创建新的CLHNode节点对象，myNodeThreadLocal.set(predNodeThreadLocal.get());
        // 这句代码进行优化，提高GC效率和节省内存空间。
        this.myNodeThreadLocal.set(predNodeThreadLocal.get());
    }

    static class Kfc {
        private final Lock lock = new CLHLock();
        private int i = 0;
        public void takeout() {
            try {
                lock.lock();
                System.out.println(Thread.currentThread().getName() + ": 拿了第" + ++i + "份外卖");
            } finally {
                lock.unlock();
            }
        }
    }

    public static void main(String[] args) {
        final Kfc kfc = new Kfc();
        for (int i = 1; i <= 3; i++) {
            new Thread(kfc::takeout).start();
        }
    }
}
