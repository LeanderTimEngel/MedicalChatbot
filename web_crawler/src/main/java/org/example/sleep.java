package org.example;
import java.util.Random;
public class sleep {
    public sleep(){

    // create a new instance of Random

    }
    static void sleeper(int x) {
        Random rand = new Random();

        // generate a random number between 2 and 7 (inclusive)
        int randomNum = rand.nextInt(6) + 2;
        try {
            Thread.sleep(x); // wait for the random number of seconds
        } catch (InterruptedException e) {
            // handle the exception
        }
    }
}
