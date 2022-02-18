package com.aiden0xz.hopping;


public class ClassLevelSyncIncrease {
    static int count = 0;

    private static synchronized void syncIncreaseInClsLevel() {
        count++;
    }

    private static void increaseInClsLevel() {
        count++;
    }

    private synchronized void syncIncrease() {
        count++;
    }

    private void increase() {
        count++;
    }

    private static boolean foundConcurrentProblem(int testLoop, int threadCount, boolean classLevel, boolean sync) throws InterruptedException {

        Runnable increaseMethod;

        if (classLevel) {
            if (sync) {
                increaseMethod = ClassLevelSyncIncrease::syncIncreaseInClsLevel;
            } else {
                increaseMethod = ClassLevelSyncIncrease::increaseInClsLevel;
            }
        } else {
            // always create new instance to avoid lock on same object
            if (sync) {
                increaseMethod = () -> {
                    ClassLevelSyncIncrease app = new ClassLevelSyncIncrease(); app.syncIncrease();};
            } else {
                increaseMethod = () -> {
                    ClassLevelSyncIncrease app = new ClassLevelSyncIncrease(); app.increase();};
            }
        }

        Thread[] threads = new Thread[threadCount];
        int target = 1000;
        for (int i = 0; i < threadCount; i++) {
            Thread thread = new Thread(() -> {
                for (int j = 0; j < target; j++) {
                    increaseMethod.run();
                }
            });
            threads[i] = thread;
            thread.start();
        }

        for (Thread t : threads) {
            t.join();
        }

        return count != target * threadCount * testLoop;
    }

    public static void main(String[] args) throws InterruptedException {
        for (int clsLevel = 0; clsLevel < 2; clsLevel++) {
            for (int sync = 0; sync < 2; sync++) {

                // reset counter to run a new test
                ClassLevelSyncIncrease.count = 0;

                for (int i = 0; i < 10; i++) {

                    boolean classLevel = clsLevel == 1;
                    boolean synced = sync == 1;

                    if (foundConcurrentProblem(i+1, 100, classLevel, synced)) {
                        if (classLevel && synced) {
                            // should never have happened
                            System.out.printf("found concurrent problem, count: %d with class level lock\n", ClassLevelSyncIncrease.count);
                        }
                        System.out.printf("found concurrent problem with class level: %s and sync increase: %s!!\n", classLevel, synced);
                        break;
                    }
                }
            }
        }
    }
}
