package chapter8;

import java.util.*;

/**
 * Created by lxttx on 16/2/19.
 */

class Glyph {
    void draw() {
        System.out.println("Glyph.draw()");
    }

    Glyph() {
        System.out.println("Glyph() before draw()");
        draw();
        System.out.println("Glyph() after draw()");
    }

}

class RoundGlyph extends Glyph {
    private int radius = 1;

    RoundGlyph(int r) {
        radius = r;
        System.out.printf("RoundGlyph.RoundGlyph(), radius = %d\n", radius);
    }

    void draw() {
        System.out.printf("RoundGlyph.draw(), radius = %d\n", radius);
    }

}

public class PolyConstructors {
    public static void main(String[] args) {
        new RoundGlyph(5);
    }

}
/** output
 * Glyph() before draw()
 * RoundGlyph.draw(), radius = 0
 * Glyph() after draw()
 * RoundGlyph.RoundGlyph(), radius = 5
 */
