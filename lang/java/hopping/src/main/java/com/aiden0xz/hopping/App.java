package com.aiden0xz.hopping;


public class App {
    static int count = 0;


    private static synchronized void syncIncreaseInClassLevel() {
        count++;
    }

    private static void increaseInClassLevel() {
        count++;
    }

    private synchronized void syncIncrease() {
        count++;
    }

    private void increase() {
        count++;
    }

    private static boolean foundConcurrentProblem(int testLoop, int threadCount, boolean classLevel, boolean sync) throws InterruptedException {
        Thread[] threads = new Thread[threadCount];

        int target = 1000;
        for (int i = 0; i < threadCount; i++) {
            Thread thread =  new Thread(()->{
                for (int j = 0; j < target; j++) {
                    if (classLevel) {
                        if (sync) {
                            App.syncIncreaseInClassLevel();
                        } else {
                            App.increaseInClassLevel();
                        }
                    } else {
                        App app = new App();
                        if (sync) {
                            app.syncIncrease();
                        } else {
                            app.increase();
                        }
                    }
                }
            });
            threads[i] = thread;
            thread.start();
        }

        for (Thread t: threads) {
            t.join();
        }

        return count != 1000*threadCount*testLoop;
    }

    public static void main(String[] args) throws InterruptedException{
            for (int clsLevel =0; clsLevel < 2; clsLevel++) {
                for (int sync =0; sync < 2; sync++) {
                    for (int i = 0; i < 10; i++) {

                    boolean classLevel = clsLevel == 1;
                    boolean synced = sync == 1;

                    if (foundConcurrentProblem(i+1, 100, classLevel, synced)) {
                        if (classLevel && synced) {
                            // should never have happened
                            System.out.printf("found concurrent problem, count: %d with class level lock\n", App.count);
                        }
                        System.out.printf(
                                "found concurrent problem with class level: %s and sync increase: %s!!\n",
                                classLevel, synced);
                        break;
                    } else {
                        System.out.println("all works fine!!");
                    }
                }
            }
        }
    }
}
