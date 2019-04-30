typedef struct
{
    union {
        unsigned int slock;
        struct __raw_tickets
        {
            unsigned short owner;
            unsigned short next;
        } tickets;
    };
} arch_spinlock_t;

static inline void arch_spin_lock(arch_spinlock_t *lock)
{
    arch_spinlock_t old_lock;

    old_lock.slock = lock->slock;                           // 1
    lock->tickets.next++;                                   // 2
    while (old_lock.tickets.next != old_lock.tickets.owner) // 3
    {
        wfe();                                        // 4
        old_lock.tickets.owner = lock->tickets.owner; // 5
    }
}

/**
* 
1. 继续上面的举例。顾客从取号机器得到排队号。
2. 取号机器更新下个顾客将要拿到的排队号。
3. 看一下显示屏，判断是否轮到自己了。
4. wfe()函数是指ARM64架构的WFE(wait for event)汇编指令。WFE是让ARM核进入低功耗模式的指令。
   当进程拿不到锁的时候，原地自旋不如cpu睡眠。节能。睡下去之后，什么时候醒来呢
   就是等到持有锁的进程释放的时候，醒过来判断是否可以持有锁。如果不能获得锁，继续睡眠即可。
   这里就相当于顾客先小憩一会，等到广播下一位排队者的时候，醒来看看是不是自己。
5. 前台已经为上一个顾客办理完成业务，剩下排队的顾客都要抬头看一下显示屏是不是轮到自己了。
*
**/

static inline void arch_spin_unlock(arch_spinlock_t *lock)
{
    lock->tickets.owner++; // 1
    sev();                 // 2
}

/**
sev()函数是指ARM64架构的SEV汇编指令。当进程无法获取锁的时候会使用WFE指令使CPU睡眠。
现在释放锁了，自然要唤醒所有睡眠的CPU醒来检查自己是不是可以获取锁。
**/